import random

GOOD_MORNING_MESSAGES = [
    "☀️ *Good morning, {nickname}!* 🌸\nWaking up knowing that you are in my life makes every morning feel like a blessing. I hope today brings you as much joy, warmth, and smiles as you bring to my heart. Have a wonderful day, mon amour! Hakim is thinking of you. 💕",
    "☕ *Rise and shine, my gorgeous {nickname}!* ✨\nDrink your coffee/tea, take a deep breath, and remember that you are capable of amazing things today. Don't forget that someone out here loves you beyond words. Have the sweetest day! 🌹",
    "🌅 *Bonjour mon amour, {nickname}!* 💖\nJust wanted to be the first to remind you: you are the most precious part of my life. May your day be smooth, peaceful, and filled with little moments that make you smile. Sending you the warmest morning kisses! 💋",
    "🌷 *Good morning, my sweet {nickname}!* 🌤️\nEvery sunrise is a reminder of how lucky I am to have your love illuminating my world. Go conquer your day, beautiful — I am always right behind you, cheering for you! 🌟",
    "🍯 *Wake up, honey {nickname}!* 🥞\nThe world is waiting for your smile today! Take it easy, be kind to yourself, and know that my heart is holding yours all day long. Je t'aime tellement! 💕",
    "✨ *Good morning to the queen of my heart, {nickname}!* 👑\nI went to sleep thinking of you and woke up with you on my mind. May your day be as radiant and lovely as you are! 💐",
    "🌿 *A gentle good morning to my favorite person, {nickname}!* 🍃\nNo matter what today throws at you, remember you're strong, you're smart, and you're deeply, endlessly loved by Hakim. Have a blessed day! 🤍"
]

GOOD_NIGHT_MESSAGES = [
    "🌙 *Good night, my sweetest {nickname}...* 🌌\nClose your eyes and let go of all the worries from today. You did wonderful. Wrap yourself tightly in your blanket, imagine my arms around you, and drift into the sweetest dreams. Sleep well, my love. 🤍",
    "✨ *Bonne nuit, {nickname} de ma vie!* 💫\nLook up at the stars tonight — each one carries a gentle kiss and a prayer for your peace. May you rest peacefully and wake up refreshed. Hakim loves you forever and always. 😴💖",
    "🧸 *Tuck in time, {nickname}!* 🕯️\nSending you the softest virtual cuddles and a warm forehead kiss. You are my safe place, my peace, and my happiest dream. Good night, beautiful! 💋",
    "💤 *Sweet dreams, my princess {nickname}...* 👑\nMay angels watch over you while you sleep. Thank you for making my life so beautiful today, just by being you. See you in my dreams! 🌙🌹",
    "🌌 *Night night, my precious {nickname}!* 🌟\nRest your pretty mind and your gentle heart. Tomorrow is a brand new page, and I can't wait to love you even more tomorrow than I do today. Dormez bien mon amour. 💕",
    "🕊️ *Sleep peacefully, {nickname}...* 💭\nIf you feel a warm gentle breeze tonight, it's just my love whispering through the quiet. Good night, habibati. You are my everything. 🤍"
]

COMPLIMENTS = [
    "Has anyone told you today that your smile is literally breathtaking? Well, Hakim is here to make sure you never forget it! 😍",
    "You possess a grace, kindness, and intelligence that makes you truly one in a million, {nickname}. 💎",
    "The way you express yourself and care for others shows how exceptionally pure your heart is. 🌸",
    "You don't even have to try — you look absolutely stunning every second of the day. ✨",
    "Your laugh is my absolute favorite sound in the world; it turns any grey day into pure sunshine. ☀️",
    "You have this captivating energy that makes everything around you feel softer, warmer, and brighter. 🕯️",
    "You are so strong, resilient, and graceful under pressure. I admire you so much, {nickname}. 👑",
    "Everything about you, from your adorable quirks to your deep thoughts, makes me fall in love over and over. 🌹",
    "You make kindness look effortless and beauty look natural. I am the luckiest guy alive to call you mine. 💕",
    "You have the sweetest soul and the most mesmerizing presence, {nickname}. Never forget how special you are! 💖"
]

VIRTUAL_HUGS = [
    "🫂 *[ H U G   I N C O M I N G ]* 🫂\n\n*Hakim wraps both arms around you, pulls you in close, rests his chin softly on your head, and squeezes you tight.* 🤍\n\n_« Take a deep breath, my love. You are safe, you are cherished, and I'm right here with you. »_",
    "🧸 *Super Warm Teddy Bear Hug delivered!* 🧸\n\n*A tight, comforting embrace that melts all tension away and keeps you warm.* \n\n_« Just breathe and relax in my arms, {nickname}. Everything is going to be okay. »_ 💕",
    "🌧️➡️🌤️ *Comfort Hug for {nickname}:* \n\n*Holding your hands first, looking into your eyes, then wrapping you in a long, silent, peaceful hug until you smile.* 🌸\n\n_« I will always be your safe harbor. »_",
    "⚡ *Surprise Bear Hug from behind!* 🤗\n\n*Hakim sneaks up, wraps his arms around your waist, and gives you a sweet kiss on the cheek!* 💋\n\n_« Gotcha! You can't escape my love, {nickname}! »_"
]

VIRTUAL_KISSES = [
    "💋 *[ FOREHEAD KISS ]* 💋\n\nA gentle, tender kiss on your forehead that says: _« I respect you, I protect you, and I love you with all my soul, {nickname}. »_ 🤍",
    "😘 *[ SWEET CHEEK KISS ]* 😘\n\nA soft, lingering kiss on your cheek while smiling into your eyes. You are so cute! 💕",
    "✨ *[ HAND KISS ]* ✨\n\nTaking your gentle hand, holding it with care, and placing a soft kiss on your knuckles like the queen you are, {nickname}. 👑",
    "💖 *[ MILLION KISSES BLOWOUT ]* 💖\n\n*KISS! KISS! KISS! KISS! KISS!* 💋💋💋\nA whole storm of kisses landing all over your face until you can't stop laughing! 🥰"
]

def get_random_morning(nickname: str) -> str:
    msg = random.choice(GOOD_MORNING_MESSAGES)
    return msg.format(nickname=nickname)

def get_random_night(nickname: str) -> str:
    msg = random.choice(GOOD_NIGHT_MESSAGES)
    return msg.format(nickname=nickname)

def get_random_compliment(nickname: str) -> str:
    msg = random.choice(COMPLIMENTS)
    return msg.format(nickname=nickname)

def get_random_hug(nickname: str) -> str:
    msg = random.choice(VIRTUAL_HUGS)
    return msg.format(nickname=nickname)

def get_random_kiss(nickname: str) -> str:
    msg = random.choice(VIRTUAL_KISSES)
    return msg.format(nickname=nickname)
