from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import config
import database

def get_main_menu_keyboard(role: str = "guest") -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("💌 Why I Love You", callback_data="menu_reasons"),
            InlineKeyboardButton("📜 Love Letter", callback_data="menu_letters"),
        ],
        [
            InlineKeyboardButton("☀️ Good Morning", callback_data="menu_morning"),
            InlineKeyboardButton("🌙 Good Night", callback_data="menu_night"),
        ],
        [
            InlineKeyboardButton("🎡 Date Ideas & Spinner", callback_data="menu_dates"),
            InlineKeyboardButton("🎮 Couple Games & Fun", callback_data="menu_games"),
        ],
        [
            InlineKeyboardButton("🫙 The Love Jar", callback_data="menu_jar"),
            InlineKeyboardButton("⏳ Days Together", callback_data="menu_counter"),
        ],
        [
            InlineKeyboardButton("🫂 Virtual Hug", callback_data="menu_hug"),
            InlineKeyboardButton("💋 Virtual Kiss", callback_data="menu_kiss"),
        ],
        [
            InlineKeyboardButton("✨ Sweet Compliment", callback_data="menu_compliment"),
            InlineKeyboardButton("📊 Love Counter & Info", callback_data="menu_info"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    first_name = user.first_name or ""

    # Identification
    role = config.identify_user(user_id, first_name)
    fatima_nick = config.get_random_fatima_nickname()

    if role == "fatima":
        welcome_text = (
            f"👑 *Bienvenue, ma chère {fatima_nick}!* 💕\n\n"
            f"This is your private love sanctuary, created by *Hakim* just for you.\n\n"
            f"Every single button here was built to make you smile, remind you how precious "
            f"you are, and celebrate our love together. ✨\n\n"
            f"_What would you like to explore today, Hayati?_"
        )
    elif role == "hakim":
        welcome_text = (
            f"👋 *Welcome back, Hakim!* 👑\n\n"
            f"Here is your private bot for *{config.GIRLFRIEND_NAME}*.\n\n"
            f"You can test any features, leave sweet love notes in her Love Jar, "
            f"or see how much love you've shared! 💕"
        )
    else:
        welcome_text = (
            f"🌸 *Welcome to Fatima & Hakim's Love Sanctuary!* 💕\n\n"
            f"A private romantic sanctuary designed for *Fatima* from *Hakim*.\n\n"
            f"Here you'll find heartfelt love messages, date ideas, fun couple games, "
            f"and romantic surprises! ✨"
        )

    await update.message.reply_text(
        text=welcome_text,
        reply_markup=get_main_menu_keyboard(role),
        parse_mode="Markdown"
    )

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    role = config.identify_user(user.id, user.first_name or "")

    if query.data == "main_menu":
        fatima_nick = config.get_random_fatima_nickname()
        menu_text = (
            f"💖 *Fatima & Hakim's Love Sanctuary* 💖\n\n"
            f"Choose an option below to fill your day with smiles, {fatima_nick}! ✨"
        )
        try:
            await query.edit_message_text(
                text=menu_text,
                reply_markup=get_main_menu_keyboard(role),
                parse_mode="Markdown"
            )
        except Exception:
            await query.message.reply_text(
                text=menu_text,
                reply_markup=get_main_menu_keyboard(role),
                parse_mode="Markdown"
            )
