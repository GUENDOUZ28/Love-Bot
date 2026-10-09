from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from datetime import date
import config
import database
from data.couple_games import (
    COUPLE_QUIZ_QUESTIONS,
    WOULD_YOU_RATHER_CARDS,
    get_random_would_you_rather,
    get_random_truth,
    get_random_dare,
    get_random_fortune
)

def get_games_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🥠 Daily Love Fortune Cookie", callback_data="game_fortune")],
        [InlineKeyboardButton("❓ Couple Quiz: How Well Do You Know Us?", callback_data="game_quiz_start")],
        [InlineKeyboardButton("⚖️ Couples 'Would You Rather?'", callback_data="game_wyr")],
        [
            InlineKeyboardButton("🎯 Truth or Dare (Romantic)", callback_data="game_tod"),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def handle_games_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "🎮 *The Couple Play Room & Games* 💕\n\n"
        "Take a break, share a laugh, and connect on a deeper level!\n\n"
        "Pick a game to play together:"
    )

    await query.edit_message_text(
        text=text,
        reply_markup=get_games_menu_keyboard(),
        parse_mode="Markdown"
    )

# 1. Fortune Cookie
async def handle_fortune(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    today_str = date.today().isoformat()
    fortune = database.get_today_fortune(user_id, today_str)

    if not fortune:
        fortune = get_random_fortune()
        database.save_today_fortune(user_id, today_str, fortune)

    keyboard = [
        [InlineKeyboardButton("🥠 Crack Another Secret Fortune", callback_data="game_fortune_new")],
        [InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")]
    ]
    await query.edit_message_text(
        text=f"{fortune}\n\n_(A special daily sweet note from Hakim's heart to Fatima's.)_",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_fortune_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("🥠 Cracking a fresh fortune cookie...")

    fortune = get_random_fortune()
    keyboard = [
        [InlineKeyboardButton("🥠 Crack Another Fortune", callback_data="game_fortune_new")],
        [InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")]
    ]
    await query.edit_message_text(
        text=f"{fortune}\n\n_(Hakim's fortunes never run out! 💕)_",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# 2. Couple Quiz
async def handle_quiz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Reset quiz state in user_data
    context.user_data["quiz_index"] = 0
    context.user_data["quiz_score"] = 0
    await show_quiz_question(query, context, 0)

async def show_quiz_question(query, context, q_index: int):
    if q_index >= len(COUPLE_QUIZ_QUESTIONS):
        # Quiz completed!
        score = context.user_data.get("quiz_score", 0)
        total = len(COUPLE_QUIZ_QUESTIONS)
        nick = config.get_random_fatima_nickname()

        text = (
            f"🎉 *Quiz Completed, {nick}!* 🏆\n\n"
            f"Your Score: *{score} / {total}*\n\n"
            f"Whether 0 or 100%, Hakim loves you with 1000% of his heart every single day! 💕"
        )
        keyboard = [
            [InlineKeyboardButton("🔄 Play Again", callback_data="game_quiz_start")],
            [InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")]
        ]
        await query.edit_message_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )
        return

    q = COUPLE_QUIZ_QUESTIONS[q_index]
    context.user_data["current_question"] = q

    text = (
        f"❓ *Question {q_index + 1} of {len(COUPLE_QUIZ_QUESTIONS)}:*\n\n"
        f"*{q['question']}*"
    )

    keyboard = []
    for opt_idx, opt_text in enumerate(q["options"]):
        keyboard.append([InlineKeyboardButton(opt_text, callback_data=f"quiz_ans_{opt_idx}")])
    keyboard.append([InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")])

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    selected_idx = int(query.data.replace("quiz_ans_", ""))
    q = context.user_data.get("current_question")
    if not q:
        await handle_quiz_start(update, context)
        return

    is_correct = (selected_idx == q["correct_index"])
    if is_correct:
        context.user_data["quiz_score"] = context.user_data.get("quiz_score", 0) + 1
        result_header = "✨ *Spot on! Bingo!* 🎯"
    else:
        result_header = "😄 *Cute guess, but here is the truth:* 💕"

    feedback_text = (
        f"{result_header}\n\n"
        f"💡 {q['comment']}\n\n"
        f"Current Score: *{context.user_data['quiz_score']}*"
    )

    next_idx = context.user_data.get("quiz_index", 0) + 1
    context.user_data["quiz_index"] = next_idx

    keyboard = [
        [InlineKeyboardButton("➡️ Next Question", callback_data="quiz_next_q")],
        [InlineKeyboardButton("🔙 Exit Quiz", callback_data="menu_games")]
    ]
    await query.edit_message_text(
        text=feedback_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_quiz_next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    q_index = context.user_data.get("quiz_index", 0)
    await show_quiz_question(query, context, q_index)

# 3. Would You Rather
async def handle_wyr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    card = get_random_would_you_rather()
    context.user_data["current_wyr"] = card

    text = f"{card['prompt']}\n\n" f"🅰️ *Option A:* {card['option_a']}\n\n" f"🅱️ *Option B:* {card['option_b']}"

    keyboard = [
        [
            InlineKeyboardButton("Option 🅰️", callback_data="wyr_pick_A"),
            InlineKeyboardButton("Option 🅱️", callback_data="wyr_pick_B")
        ],
        [InlineKeyboardButton("🎲 Next Card", callback_data="game_wyr")],
        [InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_wyr_pick(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    pick = "Option A" if query.data == "wyr_pick_A" else "Option B"
    await query.answer(f"You chose {pick}! 🥰")

    card = context.user_data.get("current_wyr", {})
    choice_text = card.get("option_a") if query.data == "wyr_pick_A" else card.get("option_b")

    text = (
        f"💖 *Your choice:* _{choice_text}_\n\n"
        f"Hakim approves 100%! Whatever makes you happy makes Hakim happy. 💕"
    )

    keyboard = [
        [InlineKeyboardButton("🎲 Another Would You Rather", callback_data="game_wyr")],
        [InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# 4. Truth or Dare
async def handle_tod_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "🎯 *Truth or Dare: Romantic Couple Edition* 💋\n\n"
        "Dare to open your heart, or accept a cute romantic challenge!\n"
        "Which do you pick?"
    )

    keyboard = [
        [
            InlineKeyboardButton("🤍 Truth", callback_data="tod_pick_truth"),
            InlineKeyboardButton("🔥 Dare", callback_data="tod_pick_dare")
        ],
        [InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_tod_truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    truth = get_random_truth()
    text = (
        f"🤍 *Your Romantic Truth Question:*\n\n"
        f"« *{truth}* »\n\n"
        f"_Be completely honest from the heart!_ ✨"
    )

    keyboard = [
        [InlineKeyboardButton("🤍 Another Truth", callback_data="tod_pick_truth")],
        [InlineKeyboardButton("🔥 Switch to Dare", callback_data="tod_pick_dare")],
        [InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_tod_dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    dare = get_random_dare()
    text = (
        f"🔥 *Your Romantic Dare:*\n\n"
        f"« *{dare}* »\n\n"
        f"_No backing out! Send your proof or do it right now!_ 😉💋"
    )

    keyboard = [
        [InlineKeyboardButton("🔥 Another Dare", callback_data="tod_pick_dare")],
        [InlineKeyboardButton("🤍 Switch to Truth", callback_data="tod_pick_truth")],
        [InlineKeyboardButton("🔙 Back to Games", callback_data="menu_games")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
