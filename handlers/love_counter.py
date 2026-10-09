from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from datetime import datetime, date
import config
import database

async def handle_counter_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    anniv = config.get_anniversary_date()
    today = date.today()

    delta = today - anniv
    days = delta.days

    if days < 0:
        days = abs(days)
        time_desc = f"Countdown to our beginning: *{days} days* to go! ⏳"
    else:
        years = days // 365
        remaining_days = days % 365
        months = remaining_days // 30
        leftover_days = remaining_days % 30

        parts = []
        if years > 0:
            parts.append(f"*{years}* year{'s' if years > 1 else ''}")
        if months > 0:
            parts.append(f"*{months}* month{'s' if months > 1 else ''}")
        parts.append(f"*{leftover_days}* day{'s' if leftover_days > 1 else ''}")
        time_desc = ", ".join(parts)

    hours = days * 24
    minutes = hours * 60

    stats = database.get_counters()
    notes_count = database.get_all_notes_count()
    fatima_nick = config.get_random_fatima_nickname()

    text = (
        f"⏳ *Our Love Story & Journey* 💍\n\n"
        f"🗓️ *Our Anniversary:* `{anniv.strftime('%B %d, %Y')}`\n\n"
        f"✨ *Time In Love:* {time_desc} ({days:,} total days)\n"
        f"⏰ *Hours of Adoration:* ~{hours:,} hours\n"
        f"💓 *Heartbeats Shared:* Millions & counting\n\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"📊 *Our Private Sanctuary Stats:*\n"
        f"🫂 *Hugs Delivered:* {stats['hugs']}\n"
        f"💋 *Kisses Given:* {stats['kisses']}\n"
        f"💌 *Notes in Love Jar:* {notes_count}\n\n"
        f"_« With you, {fatima_nick}, every second is my favorite second. »_ 💕"
    )

    keyboard = [
        [
            InlineKeyboardButton("🫂 Send Hug", callback_data="menu_hug"),
            InlineKeyboardButton("💋 Send Kiss", callback_data="menu_kiss")
        ],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_info_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    role = config.identify_user(user.id, user.first_name)
    stats = database.get_counters()
    notes_count = database.get_all_notes_count()

    text = (
        f"ℹ️ *About Fatima & Hakim's Love Sanctuary* 💕\n\n"
        f"👤 *You are identified as:* `{role.upper()}` (ID: `{user.id}`)\n"
        f"👫 *Couple:* {config.BOYFRIEND_NAME} ❤️ {config.GIRLFRIEND_NAME}\n"
        f"🗓️ *Anniversary:* `{config.ANNIVERSARY_DATE_STR}`\n\n"
        f"📊 *Lifetime Counter:* \n"
        f"• Hugs: *{stats['hugs']}*\n"
        f"• Kisses: *{stats['kisses']}*\n"
        f"• Sealed Love Notes: *{notes_count}*\n\n"
        f"_Designed with pure love by Hakim for his favorite princess, Fatima._ 🌹"
    )

    keyboard = [
        [InlineKeyboardButton("⏳ Days Together Counter", callback_data="menu_counter")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
