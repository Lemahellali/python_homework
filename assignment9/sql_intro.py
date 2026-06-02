import sqlite3

conn = None
def add_publisher(cursor, name):
    cursor.execute(
        "SELECT * FROM publishers WHERE name = ?",
        (name,)
    )

    result = cursor.fetchall()

    if len(result) > 0:
        print(f"Publisher '{name}' already exists.")
        return

    cursor.execute(
        "INSERT INTO publishers (name) VALUES (?)",
        (name,)
    )
def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute(
            "SELECT * FROM magazines WHERE name = ?",
            (name,)
        )

        result = cursor.fetchall()

        if len(result) > 0:
            print(f"Magazine '{name}' already exists.")
            return

        cursor.execute(
            "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
            (name, publisher_id)
        )

    except sqlite3.Error as error:
        print("Database error:", error)

def add_subscriber(cursor, name, address):
    cursor.execute(
        "SELECT * FROM subscribers WHERE name = ? AND address = ?",
        (name, address)
    )
    result = cursor.fetchall()

    if len(result) > 0:
        print(f"Subscriber '{name}' already exists.")
        return

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):

    cursor.execute(
        "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
        (subscriber_id, magazine_id)
    )

    result = cursor.fetchall()

    if len(result) > 0:
        print("This subscription already exists.")
        return

    cursor.execute(
        """
        INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
        VALUES (?, ?, ?)
        """,
        (subscriber_id, magazine_id, expiration_date)
    )
  
  

try:
    
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
    )
    """)
    add_publisher(cursor, "National Geographic")
    add_publisher(cursor, "Vogue")
    add_publisher(cursor, "Forbes")

    add_magazine(cursor, "Time", 1)
    add_magazine(cursor, "Fashion Weekly", 2)
    add_magazine(cursor, "Business Today", 3)

    add_subscriber(cursor, "Lema Hellali", "8340 Greensboro Dr")
    add_subscriber(cursor, "Sara Khan", "120 Main Street")
    add_subscriber(cursor, "Ali Ahmad", "45 Green Road")

    add_subscription(cursor, 1, 1, "2026-12-31")
    add_subscription(cursor, 2, 2, "2026-11-30")
    add_subscription(cursor, 3, 3, "2026-10-31")

    conn.commit()

    print("\nAll Subscribers:")

    cursor.execute("SELECT * FROM subscribers")
    results = cursor.fetchall()

    for row in results:
        print(row)


    print("\nMagazines Sorted by Name:")

    cursor.execute("SELECT * FROM magazines ORDER BY name")
    results = cursor.fetchall()

    for row in results:
        print(row)    

    print("\nMagazines from National Geographic:")

    cursor.execute("""
        SELECT magazines.name, publishers.name
        FROM magazines
        JOIN publishers
        ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = 'National Geographic'
    """)

    results = cursor.fetchall()

    for row in results:
        print(row)    

finally:
    if conn:
        conn.close()
        print("Database connection closed.")


     