import random
from typing import Dict, List, Any

# 1. COUPLE QUIZ QUESTIONS
COUPLE_QUIZ_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": 1,
        "question": "Who is more likely to fall asleep first during a cozy movie night? 🍿😴",
        "options": ["Hakim 😴", "Fatima 💤", "Both fall asleep at the same time! 😂"],
        "correct_index": 1,
        "comment": "Fatima gets so warm and comfortable that sleep wins every time! 🥰"
    },
    {
        "id": 2,
        "question": "What is Hakim's absolute favorite thing about Fatima? 💕",
        "options": [
            "Her gorgeous smile and laughing eyes ✨",
            "Her kindness and golden heart 🌸",
            "The way she hugs him like home 🫂",
            "Literally everything, trick question! 💖"
        ],
        "correct_index": 3,
        "comment": "It's impossible to pick just one — Hakim adores every single detail of Fatima! 🌹"
    },
    {
        "id": 3,
        "question": "Who takes longer to pick an outfit before going out? 👗👔",
        "options": ["Fatima taking her time to look stunning 💅", "Hakim being indecisive 🤷‍♂️", "Both are equally quick ⚡"],
        "correct_index": 0,
        "comment": "Perfection takes time, and Fatima always ends up looking breathtaking! 👑"
    },
    {
        "id": 4,
        "question": "If Hakim and Fatima are ordering food, who steals food from whose plate? 🍟👀",
        "options": [
            "Fatima: 'I'm not hungry' *steals Hakim's fries* 🍟",
            "Hakim sneakily stealing Fatima's dessert 🍰",
            "They share equally 50/50 🤝"
        ],
        "correct_index": 0,
        "comment": "The classic rule of romance: Hakim's fries are automatically community property! 😂🍟"
    },
    {
        "id": 5,
        "question": "Who said 'I love you' first, or who is the biggest romantic softie? 💌",
        "options": [
            "Hakim, the devoted hopeless romantic 🌹",
            "Fatima, the sweet soulmate 💕",
            "They both said it with their eyes first 👀✨"
        ],
        "correct_index": 0,
        "comment": "Hakim's heart was conquered from day one! 🤍"
    },
    {
        "id": 6,
        "question": "What is our ideal weekend getaway? 🌄",
        "options": [
            "A peaceful cabin in nature with hot tea & fireside cuddles 🪵☕",
            "A seaside beach resort with sunset walks by the water 🌊🌅",
            "A bustling city adventure trying new restaurants 🌆🍽️",
            "Staying at home ordering takeout in matching pajamas 🛋️🍕"
        ],
        "correct_index": 0,
        "comment": "Anywhere in the world is heaven as long as Hakim and Fatima are together! 🏡💕"
    }
]

# 2. WOULD YOU RATHER (COUPLE EDITION)
WOULD_YOU_RATHER_CARDS: List[Dict[str, str]] = [
    {
        "prompt": "⚖️ *Would you rather...*",
        "option_a": "Get an unexpected forehead kiss every 10 minutes 💋",
        "option_b": "Hold hands non-stop everywhere you walk 🤝"
    },
    {
        "prompt": "⚖️ *Would you rather...*",
        "option_a": "Spend a week in a cozy mountain cabin in the snow with Hakim ❄️🏔️",
        "option_b": "Spend a week in an overwater bungalow with turquoise waters 🏝️🌊"
    },
    {
        "prompt": "⚖️ *Would you rather...*",
        "option_a": "Have Hakim cook you a 3-course dinner every night 👨‍🍳🍝",
        "option_b": "Have Hakim give you a soothing 30-minute massage every evening 💆‍♀️✨"
    },
    {
        "prompt": "⚖️ *Would you rather...*",
        "option_a": "Never be able to stop smiling when looking at each other 😄",
        "option_b": "Always know exactly what the other is thinking without words 🧠💭"
    },
    {
        "prompt": "⚖️ *Would you rather...*",
        "option_a": "Wear cute matching pajamas together at home all day 🧸",
        "option_b": "Dress up like a royal couple for an ultra-fancy date night 👑✨"
    },
    {
        "prompt": "⚖️ *Would you rather...*",
        "option_a": "Dance together slowly in the kitchen under dim lights 🕯️💃",
        "option_b": "Stargaze in the bed of a truck with warm blankets until sunrise 🌌☕"
    }
]

# 3. TRUTH OR DARE (COUPLE EDITION)
TRUTHS: List[str] = [
    "What was the very first thought that crossed your mind the first time you saw Hakim? 👀💭",
    "What is one cute little habit of Hakim's that secretly makes you smile every time? 🥰",
    "If you could relive one single day we spent together, which day would it be? 📅✨",
    "What is the sweetest thing Hakim has ever done or said to you? 💌",
    "What song instantly reminds you of us whenever you hear it? 🎶",
    "Where is the place you feel closest and most at peace with Hakim? 🤍",
    "What is something you dream of doing together 5 years from now? 🏡"
]

DARES: List[str] = [
    "Send Hakim a 10-second voice note saying 'Je t'aime' in the sweetest voice you can do! 🎙️💕",
    "Take a cute silly selfie right now and send it to Hakim! 📸😜",
    "Promise Hakim that the next time you see him in person, you'll give him a 30-second silent hug without letting go! 🫂⏱️",
    "Send Hakim a text listing 3 things you find adorable about him! 📝✨",
    "Send Hakim your favorite song that makes you think of your love! 🎵🎧",
    "Close your eyes right now, think of your favorite memory of us, and smile for 15 seconds! 😊💭"
]

# 4. DAILY LOVE FORTUNE COOKIE
FORTUNES: List[str] = [
    "🥠 *Crack!* Today's Fortune: \n\n« _The universe conspired to bring Hakim and Fatima together. Good things are heading your way today, Hayati!_ » ✨",
    "🥠 *Crack!* Today's Fortune: \n\n« _A warm surprise and extra sweet cuddles are in your near future. Hakim loves you to infinity._ » 🌸",
    "🥠 *Crack!* Today's Fortune: \n\n« _Your smile has a 100% chance of making Hakim's heart flutter today. Wear it proudly, Fatima!_ » 💖",
    "🥠 *Crack!* Today's Fortune: \n\n« _No matter what challenge comes your way, you have a partner who will move mountains for you._ » ⛰️🤍",
    "🥠 *Crack!* Today's Fortune: \n\n« _An unexpected laugh and sweet memories are scheduled for today. Drink some water and stay glowing, Princess._ » 👑💧",
    "🥠 *Crack!* Today's Fortune: \n\n« _True love is not about never having storms; it's about knowing who holds your umbrella. Hakim is always by your side._ » ☔💕",
    "🥠 *Crack!* Today's Fortune: \n\n« _Your kind soul is lighting up people's lives today. Be proud of the wonderful woman you are, Fatima!_ » 🌟"
]

def get_random_quiz_question() -> Dict[str, Any]:
    return random.choice(COUPLE_QUIZ_QUESTIONS)

def get_random_would_you_rather() -> Dict[str, str]:
    return random.choice(WOULD_YOU_RATHER_CARDS)

def get_random_truth() -> str:
    return random.choice(TRUTHS)

def get_random_dare() -> str:
    return random.choice(DARES)

def get_random_fortune() -> str:
    return random.choice(FORTUNES)
