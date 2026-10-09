import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import database
import config
from data.love_reasons import get_random_reason, get_total_reasons_count
from data.love_messages import get_random_morning, get_random_night, get_random_hug, get_random_kiss
from data.love_letters import generate_love_letter
from data.date_ideas import get_random_date_idea
from data.couple_games import get_random_quiz_question, get_random_would_you_rather, get_random_fortune

def test_all():
    print(f"Total love reasons: {get_total_reasons_count()}")
    print("\n--- SAMPLE REASON ---")
    print(get_random_reason("Fatimati"))
    
    print("\n--- SAMPLE MORNING MESSAGE ---")
    print(get_random_morning("Hayati"))

    print("\n--- SAMPLE NIGHT MESSAGE ---")
    print(get_random_night("Habibati"))

    print("\n--- SAMPLE LOVE LETTER ---")
    letter = generate_love_letter("just_because", "Fatima", "Fatimati")
    print(letter[:200] + "...")

    print("\n--- SAMPLE DATE IDEA ---")
    date_idea = get_random_date_idea()
    print(date_idea["title"])
    print(date_idea["desc"])

    print("\n--- TESTING DATABASE ---")
    database.init_db()
    database.add_love_note("Hakim", "Fatima", "You make every day feel like spring, Fatimati!")
    note = database.get_random_love_note()
    assert note is not None
    print(f"Drawn note: '{note['message']}' (from {note['sender']})")

    hug_stat = database.increment_hug("Hakim")
    print(f"Hugs recorded: {hug_stat['hugs']}")

    kiss_stat = database.increment_kiss("Fatima")
    print(f"Kisses recorded: {kiss_stat['kisses']}")

    print("\n✅ ALL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_all()
