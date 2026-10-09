import os
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import config
import database
from handlers.start import start_command, menu_callback, get_main_menu_keyboard
from handlers.love_messages import (
    handle_reasons,
    handle_morning,
    handle_night,
    handle_compliment,
    handle_hug,
    handle_kiss,
)
from handlers.love_letters import (
    handle_letters_menu,
    handle_generate_letter,
)
from handlers.dates import (
    handle_dates_menu,
    handle_date_spin,
    handle_save_bucket,
    handle_view_bucket,
)
from handlers.games import (
    handle_games_menu,
    handle_fortune,
    handle_fortune_new,
    handle_quiz_start,
    handle_quiz_answer,
    handle_quiz_next,
    handle_wyr,
    handle_wyr_pick,
    handle_tod_menu,
    handle_tod_truth,
    handle_tod_dare,
)
from handlers.love_jar import (
    handle_jar_menu,
    handle_jar_draw,
    handle_jar_add_prompt,
    handle_jar_stats,
    handle_text_message_for_jar,
)
from handlers.love_counter import (
    handle_counter_menu,
    handle_info_menu,
)

# Logging configuration
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("LoveBot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    role = config.identify_user(user.id, user.first_name)
    fatima_nick = config.get_random_fatima_nickname()

    help_text = (
        f"📖 *Love Sanctuary Quick Guide* 💕\n\n"
        f"Hello {fatima_nick if role == 'fatima' else user.first_name}! Here are the available commands:\n\n"
        f"• `/start` or `/menu` — Open the main interactive menu\n"
        f"• `/hug` — Receive or send a warm virtual hug 🫂\n"
        f"• `/kiss` — Send a sweet virtual kiss 💋\n"
        f"• `/reason` — Discover a reason why Hakim loves Fatima 💌\n"
        f"• `/letter` — Generate a romantic love letter 📜\n"
        f"• `/date` — Get a surprise date idea 🎡\n"
        f"• `/days` — View how long you've been in love ⏳\n"
        f"• `/id` — See your Telegram user ID (useful for setup)\n\n"
        f"Enjoy your personal sanctuary!"
    )
    await update.message.reply_text(
        help_text,
        reply_markup=get_main_menu_keyboard(role),
        parse_mode="Markdown"
    )

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"🆔 *Your Telegram User ID:* `{user.id}`\n"
        f"👤 *Name:* {user.first_name} {user.last_name or ''}\n\n"
        f"_You can paste this ID into your `.env` file under `HAKIM_USER_ID` or `FATIMA_USER_ID`._",
        parse_mode="Markdown"
    )

async def generic_text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if this text was intended for the love jar
    if await handle_text_message_for_jar(update, context):
        return

    # Otherwise respond warmly
    user = update.effective_user
    role = config.identify_user(user.id, user.first_name)
    fatima_nick = config.get_random_fatima_nickname()

    if role == "fatima":
        reply = (
            f"Aw, Fatima! Hakim's bot is listening to you, {fatima_nick} 💕\n\n"
            f"Use the menu below to explore romantic surprises, play games, or draw love notes!"
        )
    elif role == "hakim":
        reply = (
            f"Hey Hakim! Ready to drop a secret note in Fatima's love jar or check the date ideas? 🌹"
        )
    else:
        reply = "Sending you warmth and smiles! 💕 Tap below to open the main menu:"

    keyboard = [[InlineKeyboardButton("💖 Open Love Menu", callback_data="main_menu")]]
    await update.message.reply_text(
        reply,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Exception while handling an update:", exc_info=context.error)

def main():
    token = config.TELEGRAM_BOT_TOKEN
    if not token or token == "your_bot_token_here":
        print("\n" + "=" * 60)
        print("⚠️  MISSING TELEGRAM_BOT_TOKEN!")
        print("=" * 60)
        print("Please create or edit the '.env' file and set your Telegram Bot token:")
        print("1. Open Telegram and search for @BotFather")
        print("2. Send /newbot and follow the prompts to create your bot")
        print("3. Copy the HTTP API token BotFather gives you")
        print("4. Add it to .env: TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjkl...")
        print("=" * 60 + "\n")
        sys.exit(1)

    print("💖 Starting Fatima & Hakim's Love & Games Telegram Bot...")
    app = ApplicationBuilder().token(token).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("menu", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", id_command))

    # Fast commands shortcuts
    app.add_handler(CommandHandler("hug", lambda u, c: handle_hug(u, c) if hasattr(u, 'callback_query') else generic_text_handler(u, c)))

    # Main Navigation Callbacks
    app.add_handler(CallbackQueryHandler(menu_callback, pattern="^main_menu$"))

    # Love Messages Callbacks
    app.add_handler(CallbackQueryHandler(handle_reasons, pattern="^menu_reasons$"))
    app.add_handler(CallbackQueryHandler(handle_morning, pattern="^menu_morning$"))
    app.add_handler(CallbackQueryHandler(handle_night, pattern="^menu_night$"))
    app.add_handler(CallbackQueryHandler(handle_compliment, pattern="^menu_compliment$"))
    app.add_handler(CallbackQueryHandler(handle_hug, pattern="^menu_hug$"))
    app.add_handler(CallbackQueryHandler(handle_kiss, pattern="^menu_kiss$"))

    # Love Letters Callbacks
    app.add_handler(CallbackQueryHandler(handle_letters_menu, pattern="^menu_letters$"))
    app.add_handler(CallbackQueryHandler(handle_generate_letter, pattern="^letter_cat_"))

    # Dates Callbacks
    app.add_handler(CallbackQueryHandler(handle_dates_menu, pattern="^menu_dates$"))
    app.add_handler(CallbackQueryHandler(handle_date_spin, pattern="^date_spin_|^date_cat_"))
    app.add_handler(CallbackQueryHandler(handle_save_bucket, pattern="^date_save_current$"))
    app.add_handler(CallbackQueryHandler(handle_view_bucket, pattern="^date_view_bucket$"))

    # Games Callbacks
    app.add_handler(CallbackQueryHandler(handle_games_menu, pattern="^menu_games$"))
    app.add_handler(CallbackQueryHandler(handle_fortune, pattern="^game_fortune$"))
    app.add_handler(CallbackQueryHandler(handle_fortune_new, pattern="^game_fortune_new$"))
    app.add_handler(CallbackQueryHandler(handle_quiz_start, pattern="^game_quiz_start$"))
    app.add_handler(CallbackQueryHandler(handle_quiz_answer, pattern="^quiz_ans_"))
    app.add_handler(CallbackQueryHandler(handle_quiz_next, pattern="^quiz_next_q$"))
    app.add_handler(CallbackQueryHandler(handle_wyr, pattern="^game_wyr$"))
    app.add_handler(CallbackQueryHandler(handle_wyr_pick, pattern="^wyr_pick_"))
    app.add_handler(CallbackQueryHandler(handle_tod_menu, pattern="^game_tod$"))
    app.add_handler(CallbackQueryHandler(handle_tod_truth, pattern="^tod_pick_truth$"))
    app.add_handler(CallbackQueryHandler(handle_tod_dare, pattern="^tod_pick_dare$"))

    # Love Jar Callbacks
    app.add_handler(CallbackQueryHandler(handle_jar_menu, pattern="^menu_jar$"))
    app.add_handler(CallbackQueryHandler(handle_jar_draw, pattern="^jar_draw_note$"))
    app.add_handler(CallbackQueryHandler(handle_jar_add_prompt, pattern="^jar_add_prompt$"))
    app.add_handler(CallbackQueryHandler(handle_jar_stats, pattern="^jar_stats$"))

    # Love Counter & Info Callbacks
    app.add_handler(CallbackQueryHandler(handle_counter_menu, pattern="^menu_counter$"))
    app.add_handler(CallbackQueryHandler(handle_info_menu, pattern="^menu_info$"))

    # Text message fallback & jar notes
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generic_text_handler))

    # Error handling
    app.add_error_handler(error_handler)

    print("✨ Bot is initialized and ready to run polling!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
