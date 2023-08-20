import sqlite3

class HabitDatabase:
    def __init__(self, db_name='habit_tracker.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT
                )
            ''')

    def add_habit(self, name, description=None):
        with self.conn:
            self.conn.execute('INSERT INTO habits (name, description) VALUES (?, ?)', (name, description))

    def get_habits(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM habits')
            return cursor.fetchall()
        
    def clear_all_habits(self):
        with self.conn:
            self.conn.execute('DELETE FROM habits')

# Instantiate the HabitDatabase class to use it in other parts of your app
db = HabitDatabase()
