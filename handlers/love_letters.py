from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import config
from data.love_letters import generate_love_letter, LETTER_CATEGORIES

def get_letter_category_keyboard() -> InlineKeyboardMarkup:
    keyboard = []
    for cat_key, cat_label in LETTER_CATEGORIES.items():
        keyboard.append([InlineKeyboardButton(cat_label, callback_data=f"letter_cat_{cat_key}")])
    keyboard.append([InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")])
    return InlineKeyboardMarkup(keyboard)

async def handle_letters_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    nick = config.get_random_fatima_nickname()
    text = (
        f"📜 *The Romantic Love Letter Generator* 💌\n\n"
        f"Every word is written from *Hakim's* heart to you, *{nick}*.\n\n"
        f"Choose an occasion or mood to reveal your letter:"
    )

    await query.edit_message_text(
        text=text,
        reply_markup=get_letter_category_keyboard(),
        parse_mode="Markdown"
    )

async def handle_generate_letter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    cat_key = query.data.replace("letter_cat_", "")
    fatima_nick = config.get_random_fatima_nickname()
    
    letter_text = generate_love_letter(
        category=cat_key,
        fatima_name=config.GIRLFRIEND_NAME,
        nickname=fatima_nick
    )

    keyboard = [
        [InlineKeyboardButton("📜 Another Letter in this Mood", callback_data=f"letter_cat_{cat_key}")],
        [InlineKeyboardButton("🎭 Choose Different Mood", callback_data="menu_letters")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]

    await query.edit_message_text(
        text=letter_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
