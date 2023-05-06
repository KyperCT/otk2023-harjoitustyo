import unittest
import os
import sqlite3
from database import db_interact


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_location = os.path.join(os.path.dirname(__file__), "test.db")
        db_interact.database_startup(location=self.db_location)
    
    def test_database_is_created_on_setup(self):
        self.assertTrue(os.path.isfile(self.db_location))

    def test_database_highscore_table_correct(self):
        con = sqlite3.connect(self.db_location)
        with con as cur:
            data = cur.execute("PRAGMA table_info(Highscores);")
            data = data.fetchall()
        con.close()
        correct_info = [(0, 'id', 'INTEGER', 0, None, 1),
                        (1, 'nickname', 'TEXT', 0, None, 0),
                        (2, 'score', 'INTEGER', 0, None, 0)]
        self.assertListEqual(correct_info, data)
    
    def test_database_insert_adds_data(self):
        db_interact.database_enter_new_score("test", 1800, location=self.db_location)

        con = sqlite3.connect(self.db_location)
        with con as cur:
            data = cur.execute("SELECT * FROM Highscores;")
            data = data.fetchall()
        
        self.assertListEqual(data, [(1, "test", 1800)])
    
    def test_database_get_gets_correct_list(self):
        db_interact.database_enter_new_score("test1", 1800, location=self.db_location)
        db_interact.database_enter_new_score("test2", 3600, location=self.db_location)
        db_interact.database_enter_new_score("test3", 0, location=self.db_location)
        db_interact.database_enter_new_score("test4", 400, location=self.db_location)

        scores = db_interact.database_get_top_scores(location=self.db_location)
        self.assertListEqual(scores, [("test2", 3600), ("test1", 1800), ("test4", 400), ("test3", 0)])

    def tearDown(self):
        os.remove(self.db_location)
