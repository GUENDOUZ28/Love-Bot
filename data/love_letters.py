import random
from datetime import datetime

LOVE_LETTERS = {
    "just_because": [
        """📜 *A Letter to My Beloved {fatima_name}* 💖
_{date}_

My dearest {nickname},

I am writing this to you not because it's a holiday, or because of any special occasion, but simply because my heart was overflowing with thoughts of you today.

Sometimes in the middle of a busy day, when the noise of the world gets too loud, all I have to do is think of your gentle smile, and suddenly everything falls into place. You have become my peace, my favorite thought, and the sweetest part of my reality.

I don't think I can ever put into exact words just how much you mean to me, but I want you to always remember this: having you in my life is the greatest gift God has ever blessed me with.

Thank you for being you, for your kindness, your warmth, and the way you hold my heart so gently. 

Forever and completely yours,
*Your Hakim* 💕""",
        """📜 *To the Girl Who Stole My Heart* 🌹
_{date}_

My sweetest {nickname},

If anyone had told me years ago that one person could completely change how I view the world, I wouldn't have believed them. Then you walked into my life.

Loving you is the easiest, most natural thing I have ever known. With you, I don't have to pretend or hide; I can just be myself, and you accept me with all your heart. 

I just wanted to take a moment today to remind you how deeply and genuinely you are loved. No matter where life takes us, my heart will always beat to the rhythm of your name.

With all my love and devotion,
*Hakim* 🤍"""
    ],
    "miss_you": [
        """📜 *To {fatima_name}, Across the Distance* 🕊️
_{date}_

My darling {nickname},

Every second spent away from you feels like an eternity. Distance is funny — it tests us, but at the same time, it proves how undeniable and unbreakable what we have truly is.

I find myself looking at my phone, wishing I could reach through the screen, hold your hand, and wrap you in a hug so tight that you'd feel every heartbeat beating for you. 

Close your eyes right now. Picture me sitting beside you, holding your fingers and whispering how much I adore you. I am counting down the moments until I see your beautiful face again.

Until then, know that my thoughts are with you every second.

With all my longing and love,
*Hakim* 💌"""
    ],
    "comfort": [
        """📜 *A Gentle Whisper for You, My {fatima_name}* 🌸
_{date}_

My precious {nickname},

I know days like this can feel heavy, overwhelming, or exhausting. I know that sometimes the world asks too much of you and leaves you feeling drained.

I want you to pause, take a deep breath, and let your shoulders drop. You don't have to carry the whole weight of the world on your shoulders. You are allowed to be tired. You are allowed to rest.

Remember how strong, brilliant, and resilient you are. But even more than that, remember that you are never alone. Whatever is worrying you, whatever is testing your patience — we will handle it together. I am your safe haven, always.

Rest your mind, my love. Better days are already on their way, and I'll be right beside you every step.

Holding you close in spirit,
*Your Hakim* 🧸🤍"""
    ],
    "anniversary": [
        """📜 *To My Forever Love, {fatima_name}* 💍
_{date}_

My Queen, my {nickname},

Looking back on our journey together fills my heart with an overwhelming sense of gratitude and pure happiness. Every single memory we've woven together — from our quietest giggles to our biggest milestones — is etched into my soul.

You have made every day brighter, every challenge easier, and every joy ten times sweeter. Being loved by you is an honor, and loving you is my life's greatest joy.

Thank you for choosing me. Thank you for walking beside me. I look at our past with pride, our present with pure contentment, and our future with endless excitement.

Happy anniversary, my beautiful love. Here is to a lifetime more.

Eternally yours,
*Hakim* ✨🌹"""
    ],
    "future": [
        """📜 *A Vision of Our Tomorrow, {fatima_name}* 🏡
_{date}_

My dearest {nickname},

Whenever I let my mind wander into the future, it's always you I see. 

I see us building our warm, cozy home together, filled with laughter, delicious food, inside jokes, and peaceful mornings. I see us drinking tea together by the window, supporting each other's dreams, holding hands as the years go by, and never losing the spark that we share today.

I promise you that I will work hard every single day to give you the life, respect, and happiness you deserve. You are my forever partner, and there is no one else I would rather share this life with.

Dreaming of our beautiful tomorrow,
*Hakim* 🌟💕"""
    ]
}

LETTER_CATEGORIES = {
    "just_because": "💖 Just Because I Love You",
    "miss_you": "🥺 When I Miss You",
    "comfort": "🌸 Comfort & Reassurance (Tough Day)",
    "anniversary": "💍 Our Anniversary & Milestones",
    "future": "🏡 Dreaming of Our Future"
}

def generate_love_letter(category: str, fatima_name: str = "Fatima", nickname: str = "Fatimati") -> str:
    templates = LOVE_LETTERS.get(category, LOVE_LETTERS["just_because"])
    template = random.choice(templates)
    today = datetime.now().strftime("%B %d, %Y")
    return template.format(
        fatima_name=fatima_name,
        nickname=nickname,
        date=today
    )
