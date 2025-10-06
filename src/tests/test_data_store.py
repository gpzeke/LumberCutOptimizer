import unittest

from data_store import DataStore

class TestDataStore(unittest.TestCase):
    def test_database_initialization(self):
        db = DataStore()
        
        self.assertIsNotNone(db.con)

        fetch = db.con.execute('SELECT name FROM sqlite_master ORDER BY name ASC;')
        self.assertEqual(fetch.fetchall(), [('parts',), ('projects',), ('sqlite_autoindex_projects_1',), ('sqlite_sequence',)])

    def test_add_dimension_store(self):
        db = DataStore()
        db.add_dimension_store(10.5, 5.25, 3)

        fetch = db.con.execute('SELECT length, width FROM parts;')
        results = fetch.fetchall()
        
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertEqual(result, (10.5, 5.25))

        # Clean up after test, can transition to mock potentially in the future.
        for result in results:
            db.cur.execute('DELETE FROM parts WHERE length = ? AND width = ?', (result[0], result[1]))
        db.con.commit()

        fetch = db.con.execute('SELECT length, width FROM parts;')
        results = fetch.fetchall()
        self.assertEqual(len(results), 0)

    def test_remove_dimension_store(self):
        db = DataStore()
        db.add_dimension_store(10.5, 5.25, 5)

        db.remove_dimension_store(10.5, 5.25, 2)

        fetch = db.con.execute('SELECT length, width FROM parts;')
        results = fetch.fetchall()
        
        self.assertEqual(len(results), 3)
        for result in results:
            self.assertEqual(result, (10.5, 5.25))

        for result in results:
            db.cur.execute('DELETE FROM parts WHERE length = ? AND width = ?', (result[0], result[1]))
        db.con.commit()

        fetch = db.con.execute('SELECT length, width FROM parts;')
        results = fetch.fetchall()
        self.assertEqual(len(results), 0)

    def test_add_project(self):
        db = DataStore()
        db.add_project("Test Project")

        fetch = db.con.execute('SELECT name FROM projects WHERE name = ?', ("Test Project",))
        results = fetch.fetchall()
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Test Project",))

        db.remove_project("Test Project")
        fetch = db.con.execute('SELECT name FROM projects WHERE name = ?', ("Test Project",))
        results = fetch.fetchall()
        self.assertEqual(len(results), 0)

    def test_duplicate_project(self):
        db = DataStore()
        db.add_project("Unique Project")
        db.add_project("Unique Project")  # Attempt to add duplicate

        fetch = db.con.execute('SELECT name FROM projects WHERE name = ?', ("Unique Project",))
        results = fetch.fetchall()
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], ("Unique Project",))

        db.remove_project("Unique Project")
        fetch = db.con.execute('SELECT name FROM projects WHERE name = ?', ("Unique Project",))
        results = fetch.fetchall()
        self.assertEqual(len(results), 0)