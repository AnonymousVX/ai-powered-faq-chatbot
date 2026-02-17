import sqlite3
from config import DATABASE_NAME
from datetime import datetime

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def save_chat(user_message, bot_response):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO chat_history (user_message, bot_response, timestamp)
        VALUES (?, ?, ?)
    """, (user_message, bot_response, datetime.now().isoformat()))
    
    conn.commit()
    conn.close()

def get_chat_history():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT user_message, bot_response, timestamp FROM chat_history ORDER BY id ASC")
    rows = cursor.fetchall()
    
    conn.close()
    return rows
