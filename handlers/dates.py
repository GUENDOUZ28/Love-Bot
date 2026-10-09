from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import config
import database
from data.date_ideas import get_random_date_idea

def get_dates_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🎲 Spin the Date Wheel!", callback_data="date_spin_all")],
        [
            InlineKeyboardButton("🛋️ Cozy At-Home", callback_data="date_cat_cozy"),
            InlineKeyboardButton("🍽️ Foodie & Romantic", callback_data="date_cat_food")
        ],
        [InlineKeyboardButton("🌆 Outdoor Adventure", callback_data="date_cat_outdoor")],
        [
            InlineKeyboardButton("📋 View Our Saved Wishlist", callback_data="date_view_bucket"),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def handle_dates_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    nick = config.get_random_fatima_nickname()
    text = (
        f"🎡 *Couple Date Night Planner & Idea Generator* 💕\n\n"
        f"Never run out of romantic memories to make together, *{nick}*!\n\n"
        f"Choose how you want to discover your next date:"
    )

    await query.edit_message_text(
        text=text,
        reply_markup=get_dates_menu_keyboard(),
        parse_mode="Markdown"
    )

async def handle_date_spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    category_filter = None
    if "cozy" in query.data:
        category_filter = "cozy"
    elif "food" in query.data:
        category_filter = "food"
    elif "outdoor" in query.data:
        category_filter = "outdoor"

    idea = get_random_date_idea(category_filter)
    
    # Store currently displayed date in user_data so they can save it
    context.user_data["last_date_idea"] = idea

    text = (
        f"✨ *Date Idea:* {idea['title']}\n"
        f"📁 *Vibe:* _{idea['category']}_\n\n"
        f"📝 *The Plan:*\n{idea['desc']}\n\n"
        f"💡 *Sweet Tip for Hakim & Fatima:*\n{idea['tip']}"
    )

    keyboard = [
        [InlineKeyboardButton("📌 Save to Our Bucket List", callback_data="date_save_current")],
        [InlineKeyboardButton("🎲 Spin Again", callback_data=query.data)],
        [InlineKeyboardButton("🔙 Back to Date Menu", callback_data="menu_dates")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def handle_save_bucket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    idea = context.user_data.get("last_date_idea")

    if not idea:
        await query.answer("Idea already saved or expired!", show_alert=True)
        return

    user = update.effective_user
    sender = "Fatima" if config.identify_user(user.id, user.first_name) == "fatima" else "Hakim"
    database.add_bucket_item(title=idea["title"], category=idea["category"], added_by=sender)
    
    await query.answer("Added to your couple bucket list! ✨", show_alert=True)

async def handle_view_bucket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    items = database.get_bucket_items(status="pending")
    if not items:
        text = (
            "📋 *Our Couple Date Wishlist:* \n\n"
            "_The bucket list is currently empty! Spin the wheel and click 'Save to Our Bucket List' "
            "to build your dream date memories together!_ ✨"
        )
        keyboard = [
            [InlineKeyboardButton("🎲 Find Date Ideas", callback_data="menu_dates")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ]
    else:
        text = "📋 *Our Couple Date Wishlist (Pending Adventures):*\n\n"
        for i, item in enumerate(items[:10], 1):
            text += f"{i}. *{item['title']}*\n   _(Added by {item['added_by']})_\n\n"
        text += "_Ready to plan your next adventure?_ 💖"

        keyboard = [
            [InlineKeyboardButton("🎲 Spin the Wheel", callback_data="date_spin_all")],
            [InlineKeyboardButton("🔙 Back to Date Menu", callback_data="menu_dates")]
        ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
