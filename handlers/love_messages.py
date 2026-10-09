from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import config
import database
from data.love_reasons import get_random_reason, get_total_reasons_count
from data.love_messages import (
    get_random_morning,
    get_random_night,
    get_random_compliment,
    get_random_hug,
    get_random_kiss
)

async def handle_reasons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    nick = config.get_random_fatima_nickname()
    reason_text = get_random_reason(nick)
    total = get_total_reasons_count()

    keyboard = [
        [InlineKeyboardButton("🎲 Another Reason", callback_data="menu_reasons")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    await query.edit_message_text(
        text=f"{reason_text}\n\n_(Collection of {total}+ reasons and growing every day! 🌸)_",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_morning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    nick = config.get_random_fatima_nickname()
    text = get_random_morning(nick)

    keyboard = [
        [InlineKeyboardButton("☀️ Another Morning Whisper", callback_data="menu_morning")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    nick = config.get_random_fatima_nickname()
    text = get_random_night(nick)

    keyboard = [
        [InlineKeyboardButton("🌙 Another Night Whisper", callback_data="menu_night")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_compliment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    nick = config.get_random_fatima_nickname()
    compliment = get_random_compliment(nick)

    text = f"✨ *A little reminder for {nick}:*\n\n« _{compliment}_ » 💕"

    keyboard = [
        [InlineKeyboardButton("✨ Another Compliment", callback_data="menu_compliment")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_hug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("🫂 Sending you a big warm hug!")

    user = update.effective_user
    sender_name = "Fatima" if config.identify_user(user.id, user.first_name) == "fatima" else "Hakim"
    
    stats = database.increment_hug(sender_name)
    nick = config.get_random_fatima_nickname()
    hug_text = get_random_hug(nick)

    text = (
        f"{hug_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📊 *Couple Love Gauge:*\n"
        f"🫂 *Hugs Delivered:* {stats['hugs']}\n"
        f"💋 *Kisses Exchanged:* {stats['kisses']}\n"
    )

    keyboard = [
        [
            InlineKeyboardButton("🫂 Another Hug", callback_data="menu_hug"),
            InlineKeyboardButton("💋 Kiss Instead", callback_data="menu_kiss")
        ],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_kiss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("💋 Mwah! Virtual kiss delivered!")

    user = update.effective_user
    sender_name = "Fatima" if config.identify_user(user.id, user.first_name) == "fatima" else "Hakim"

    stats = database.increment_kiss(sender_name)
    nick = config.get_random_fatima_nickname()
    kiss_text = get_random_kiss(nick)

    text = (
        f"{kiss_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📊 *Couple Love Gauge:*\n"
        f"💋 *Kisses Exchanged:* {stats['kisses']}\n"
        f"🫂 *Hugs Delivered:* {stats['hugs']}\n"
    )

    keyboard = [
        [
            InlineKeyboardButton("💋 Another Kiss", callback_data="menu_kiss"),
            InlineKeyboardButton("🫂 Hug Instead", callback_data="menu_hug")
        ],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
