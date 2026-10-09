from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
import config
import database

WAITING_NOTE_TEXT = 1

PRESET_JAR_NOTES = [
    "Whenever you read this, know that Hakim is thinking of you and sending you all his love across any distance. 🕊️",
    "You are the most precious blessing in my life. Never doubt how cherished you are, Fatima. 🤍",
    "One day we will wake up in our own home, drink coffee together, and look back at this note with a smile. 🏡☕",
    "I love you not only for what you are, but for what I am when I am with you. 💕",
    "Remember that time we couldn't stop laughing? That's what happiness feels like to me. 😄✨",
    "If you're having a hard day: breathe, drink some water, and remember you have a whole army of love behind you. 🛡️💖"
]

def get_jar_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🫙 Draw a Secret Note", callback_data="jar_draw_note")],
        [InlineKeyboardButton("✍️ Drop a Note into the Jar", callback_data="jar_add_prompt")],
        [
            InlineKeyboardButton("📜 View Jar Memory Count", callback_data="jar_stats"),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def handle_jar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    total_notes = database.get_all_notes_count()
    nick = config.get_random_fatima_nickname()

    text = (
        f"🫙 *The Virtual Love Jar for Fatima & Hakim* 💕\n\n"
        f"A timeless jar filled with folded secret notes, promises, and sweet memories.\n\n"
        f"💌 *Notes currently in the jar:* {total_notes}\n\n"
        f"Draw a note whenever you miss each other, or drop a new message for {nick} or Hakim to find!"
    )

    await query.edit_message_text(
        text=text,
        reply_markup=get_jar_menu_keyboard(),
        parse_mode="Markdown"
    )

async def handle_jar_draw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("🫙 Unfolding a secret note...")

    note = database.get_random_love_note()

    if note:
        sender = note["sender"]
        msg = note["message"]
        created = note["created_at"][:10]
        text = (
            f"📜 *You unfolded a note from the Jar:* \n\n"
            f"« _{msg}_ »\n\n"
            f"— *Written with love by {sender}* ({created}) 💕"
        )
    else:
        import random
        preset = random.choice(PRESET_JAR_NOTES)
        text = (
            f"📜 *You unfolded a note from the Jar:* \n\n"
            f"« _{preset}_ »\n\n"
            f"— *From Hakim's heart to Fatima* 💕\n\n"
            f"_(Tip: You or Hakim can add custom personal notes into the jar using the button below!)_"
        )

    keyboard = [
        [InlineKeyboardButton("🫙 Draw Another Note", callback_data="jar_draw_note")],
        [InlineKeyboardButton("✍️ Drop a Note into the Jar", callback_data="jar_add_prompt")],
        [InlineKeyboardButton("🔙 Back to Jar Menu", callback_data="menu_jar")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_jar_add_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["awaiting_jar_note"] = True

    text = (
        "✍️ *Drop a Love Note into the Jar:*\n\n"
        "Please type your message in the chat and send it! It will be folded and sealed inside the Love Jar "
        "for your partner to discover anytime.\n\n"
        "_(Send /cancel or type 'cancel' to abort)_"
    )

    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data="menu_jar")]]
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_jar_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    total = database.get_all_notes_count()
    recent = database.get_recent_notes(limit=3)

    text = f"🫙 *Love Jar Memories:*\n\nTotal custom notes stored: *{total}*\n\n"
    if recent:
        text += "*Recent additions:*\n"
        for r in recent:
            preview = r["message"][:40] + ("..." if len(r["message"]) > 40 else "")
            text += f"• _{preview}_ (by {r['sender']})\n"
    else:
        text += "_No personal notes added yet. Be the first to drop one!_ ✨\n"

    keyboard = [
        [InlineKeyboardButton("🫙 Draw a Note", callback_data="jar_draw_note")],
        [InlineKeyboardButton("🔙 Back to Jar Menu", callback_data="menu_jar")]
    ]
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_text_message_for_jar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Checks if the user was writing a note for the love jar, returns True if handled"""
    if not context.user_data.get("awaiting_jar_note"):
        return False

    msg_text = update.message.text.strip()
    if msg_text.lower() in ("/cancel", "cancel"):
        context.user_data["awaiting_jar_note"] = False
        await update.message.reply_text("Note cancelled. Returning to main menu.", reply_markup=get_jar_menu_keyboard())
        return True

    user = update.effective_user
    role = config.identify_user(user.id, user.first_name)
    sender = "Fatima" if role == "fatima" else ("Hakim" if role == "hakim" else (user.first_name or "Anonymous Love"))
    recipient = "Hakim" if sender == "Fatima" else "Fatima"

    database.add_love_note(sender=sender, recipient=recipient, message=msg_text)
    context.user_data["awaiting_jar_note"] = False

    response = (
        f"💌 *Sealed with a kiss!* 💋\n\n"
        f"Your sweet note has been safely placed in the Love Jar for *{recipient}*!\n\n"
        f"« _{msg_text}_ »"
    )

    keyboard = [
        [InlineKeyboardButton("🫙 Open Love Jar", callback_data="menu_jar")],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
    ]
    await update.message.reply_text(
        text=response,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
    return True
