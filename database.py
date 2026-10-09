import sqlite3
from datetime import datetime, date
from pathlib import Path
from typing import Optional, List, Dict, Any

DB_FILE = Path(__file__).resolve().parent / "love_bot.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Love notes jar
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS love_jar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT NOT NULL,
        recipient TEXT NOT NULL,
        message TEXT NOT NULL,
        category TEXT DEFAULT 'sweet',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_read INTEGER DEFAULT 0,
        read_at TIMESTAMP
    );
    """)

    # Couple bucket list / Date wishlist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bucket_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT DEFAULT 'date',
        added_by TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP
    );
    """)

    # Hugs & Kisses counter
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS counters (
        id INTEGER PRIMARY KEY,
        hugs INTEGER DEFAULT 0,
        kisses INTEGER DEFAULT 0,
        last_sender TEXT,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Initialize counter row if not present
    cursor.execute("SELECT id FROM counters WHERE id = 1;")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO counters (id, hugs, kisses, last_sender) VALUES (1, 0, 0, 'none');")

    # Quiz history
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        user_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        total INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Daily Fortune Cookie tracker
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_fortune (
        user_id INTEGER NOT NULL,
        cookie_date TEXT NOT NULL,
        fortune TEXT NOT NULL,
        PRIMARY KEY (user_id, cookie_date)
    );
    """)

    # Dynamic settings (key/value)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS app_settings (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    );
    """)

    conn.commit()
    conn.close()

# ----------------- Love Jar Functions -----------------

def add_love_note(sender: str, recipient: str, message: str, category: str = "sweet") -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO love_jar (sender, recipient, message, category, created_at) VALUES (?, ?, ?, ?, ?)",
        (sender, recipient, message, category, datetime.now().isoformat())
    )
    note_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return note_id

def get_random_love_note(recipient: Optional[str] = None) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    if recipient:
        cursor.execute(
            "SELECT * FROM love_jar WHERE recipient = ? ORDER BY RANDOM() LIMIT 1",
            (recipient,)
        )
    else:
        cursor.execute("SELECT * FROM love_jar ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_all_notes_count() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM love_jar")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_recent_notes(limit: int = 5) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM love_jar ORDER BY created_at DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

# ----------------- Bucket List Functions -----------------

def add_bucket_item(title: str, category: str, added_by: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bucket_list (title, category, added_by, created_at) VALUES (?, ?, ?, ?)",
        (title, category, added_by, datetime.now().isoformat())
    )
    item_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return item_id

def get_bucket_items(status: str = "pending") -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bucket_list WHERE status = ? ORDER BY id DESC", (status,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def complete_bucket_item(item_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE bucket_list SET status = 'completed', completed_at = ? WHERE id = ?",
        (datetime.now().isoformat(), item_id)
    )
    conn.commit()
    conn.close()

# ----------------- Hugs & Kisses Counter -----------------

def increment_hug(sender: str) -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE counters 
        SET hugs = hugs + 1, last_sender = ?, last_updated = ? 
        WHERE id = 1
    """, (sender, datetime.now().isoformat()))
    conn.commit()
    cursor.execute("SELECT hugs, kisses FROM counters WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return {"hugs": row["hugs"], "kisses": row["kisses"]}

def increment_kiss(sender: str) -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE counters 
        SET kisses = kisses + 1, last_sender = ?, last_updated = ? 
        WHERE id = 1
    """, (sender, datetime.now().isoformat()))
    conn.commit()
    cursor.execute("SELECT hugs, kisses FROM counters WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return {"hugs": row["hugs"], "kisses": row["kisses"]}

def get_counters() -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT hugs, kisses, last_sender, last_updated FROM counters WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"hugs": 0, "kisses": 0, "last_sender": "none"}

# ----------------- Quiz History -----------------

def record_quiz_score(user_id: int, user_name: str, score: int, total: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO quiz_history (user_id, user_name, score, total, played_at) VALUES (?, ?, ?, ?, ?)",
        (user_id, user_name, score, total, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

# ----------------- Daily Fortune Cookie -----------------

def get_today_fortune(user_id: int, today_str: str) -> Optional[str]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT fortune FROM daily_fortune WHERE user_id = ? AND cookie_date = ?", (user_id, today_str))
    row = cursor.fetchone()
    conn.close()
    return row["fortune"] if row else None

def save_today_fortune(user_id: int, today_str: str, fortune: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO daily_fortune (user_id, cookie_date, fortune) VALUES (?, ?, ?)",
        (user_id, today_str, fortune)
    )
    conn.commit()
    conn.close()

# Initialize upon module load
init_db()
