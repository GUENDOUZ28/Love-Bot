import random
from typing import Dict, List, Any

DATE_IDEAS: List[Dict[str, Any]] = [
    # --- Cozy & At-Home ---
    {
        "id": "cozy_1",
        "title": "Blanket Fort Movie Night & Hot Cocoa 🏰☕",
        "category": "🛋️ Cozy & At-Home",
        "desc": "Build a giant living room blanket fort with pillows and fairy lights. Make gourmet hot chocolate with marshmallows and binge-watch a comforting movie series.",
        "tip": "Hakim is in charge of building the fort architecture; Fatima picks the movie snacks!"
    },
    {
        "id": "cozy_2",
        "title": "DIY Homemade Pizza or Pasta Challenge 🍕🍝",
        "category": "🛋️ Cozy & At-Home",
        "desc": "Cook a fresh Italian dinner together from scratch. Put on romantic Italian music in the background, make your own dough and toppings.",
        "tip": "Wear cute matching aprons and feed each other a taste test during cooking!"
    },
    {
        "id": "cozy_3",
        "title": "Paint & Sip (Mocktail / Tea) Night 🎨🍹",
        "category": "🛋️ Cozy & At-Home",
        "desc": "Get two small canvases or sketchbooks, acrylic paints, and follow a Bob Ross or cute couple painting tutorial while sipping fancy drinks.",
        "tip": "At the end, paint a portrait of each other without looking until the big reveal!"
    },
    {
        "id": "cozy_4",
        "title": "Late Night Video Game / Board Game Duel 🎮🎲",
        "category": "🛋️ Cozy & At-Home",
        "desc": "Play cooperative or friendly versus games (Mario Kart, Overcooked, Uno, or Scrabble). Loser owes the winner 10 forehead kisses!",
        "tip": "Winner gets their choice of breakfast in bed the next morning!"
    },
    {
        "id": "cozy_5",
        "title": "Couple Spa & Massage Evening 🕯️💆",
        "category": "🛋️ Cozy & At-Home",
        "desc": "Dim the lights, light scented candles, play soothing spa ambient music. Give each other relaxing shoulder and foot massages with lavender oil.",
        "tip": "Put on hydrating face masks together and snap silly couple selfies!"
    },

    # --- Foodie & Romantic ---
    {
        "id": "food_1",
        "title": "Golden Hour Sunset Picnic 🧺🌅",
        "category": "🍽️ Romantic & Foodie",
        "desc": "Pack a basket with Fatima's favorite treats, fresh fruits, sandwiches, and sparkling cider. Head to a scenic park or hill right as the sun sets.",
        "tip": "Bring a cozy speaker for a slow background playlist."
    },
    {
        "id": "food_2",
        "title": "Dessert Crawl Around Town 🍰🍦",
        "category": "🍽️ Romantic & Foodie",
        "desc": "Skip the main dinner and go on an adventure specifically hunting down the best pastries, crepes, gelato, and hot pastries at three different spots.",
        "tip": "Order different desserts and share every single bite."
    },
    {
        "id": "food_3",
        "title": "Candlelit Dressing-Up Dinner at Home 🕯️👗",
        "category": "🍽️ Romantic & Foodie",
        "desc": "Dress up in your finest elegant outfits as if going to a 5-star gala, but have a candlelit dinner right in your dining room with a customized handwritten menu.",
        "tip": "End the evening with a slow dance in the living room."
    },
    {
        "id": "food_4",
        "title": "Mystery Food Blindfold Taste Test 🙈🍓",
        "category": "🍽️ Romantic & Foodie",
        "desc": "Each partner secretly prepares 6 sweet, savory, or funny bites. Blindfold the other and see who guesses the most flavors correctly!",
        "tip": "Include chocolate, strawberries, and cute snacks!"
    },

    # --- Outdoor & Adventure ---
    {
        "id": "out_1",
        "title": "Stargazing & Midnight Deep Talk ✨🌌",
        "category": "🌆 Outdoor & Adventure",
        "desc": "Drive to a quiet spot away from bright city lights, recline the seats or spread a blanket on the hood of the car, and stargaze with warm tea.",
        "tip": "Download a sky constellation app and spot stars together."
    },
    {
        "id": "out_2",
        "title": "Retro Arcade / Bowling Night 🎳🕹️",
        "category": "🌆 Outdoor & Adventure",
        "desc": "Go to an arcade or bowling alley. Play air hockey, win plushies in claw machines, and eat carnival snacks.",
        "tip": "Hakim must win Fatima a plushie trophy!"
    },
    {
        "id": "out_3",
        "title": "Bookstore & Coffee Shop Romance Date 📚☕",
        "category": "🌆 Outdoor & Adventure",
        "desc": "Visit a cozy bookstore. Spend 30 minutes picking out a book that you think the other would love, then read the first chapter together over coffee.",
        "tip": "Leave a secret cute love sticky note hidden in a random book on the shelf!"
    },
    {
        "id": "out_4",
        "title": "Sunset Beach or Lakeside Walk 🌊🐚",
        "category": "🌆 Outdoor & Adventure",
        "desc": "Take a tranquil walk by the water, holding hands, listening to the waves, and collecting pretty sea stones or shells.",
        "tip": "Write your initials in the sand: 'H + F 💕'"
    },
    {
        "id": "out_5",
        "title": "Scenic Road Trip with a Couple Playlist 🚗🎶",
        "category": "🌆 Outdoor & Adventure",
        "desc": "Get in the car with no strict destination in mind, roll down the windows, blast your favorite songs, and stop at cute roadside viewpoints.",
        "tip": "Sing at the top of your lungs together!"
    }
]

def get_random_date_idea(category_filter: str = None) -> Dict[str, Any]:
    if category_filter:
        filtered = [d for d in DATE_IDEAS if category_filter.lower() in d["category"].lower()]
        if filtered:
            return random.choice(filtered)
    return random.choice(DATE_IDEAS)

def get_all_categories() -> List[str]:
    return list({d["category"] for d in DATE_IDEAS})
