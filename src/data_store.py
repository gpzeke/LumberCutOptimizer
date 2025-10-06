import sqlite3


class DataStore:

    connection = None

    def __init__(self):
        if DataStore.connection is None:
            try:
                DataStore.connection = sqlite3.connect('data_store.db')
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
            else:
                print("Connection Established.")

        self.con = DataStore.connection
        self.cur = self.con.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS parts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                length REAL NOT NULL,
                width REAL NOT NULL,
                project_id INTEGER,
                FOREIGN KEY (project_id) REFERENCES projects(id)
            )
        ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        self.con.commit()

    def add_dimension_store(self, length, width, quantity, project_id='NULL'):
        for i in range(quantity):
            self.cur.execute('INSERT INTO parts (length, width, project_id) VALUES (?, ?, ?)', (float(length), float(width), project_id))
        self.con.commit()

    def remove_dimension_store(self, length, width, quantity, project_id='NULL'):
        self.cur.execute('''
            DELETE FROM parts 
            WHERE id IN (
                SELECT id from parts
                WHERE length = ? AND width = ? AND project_id = ?
                LIMIT ?
            )
            ''', 
            (float(length), float(width), project_id, quantity)
        )
        self.con.commit()

    def add_project(self, name):
        try:
            self.cur.execute('INSERT INTO projects (name) VALUES (?)', (name,))
        except sqlite3.IntegrityError as e:
            print(f"Duplicate project name: {e}")
        else:
            self.con.commit()

    def remove_project(self, name):
        self.cur.execute('DELETE FROM projects WHERE name = ?', (name,))
        self.con.commit()
