from unittest import TestCase
from sqlite3 import dbapi2 as db


class TestNothing(TestCase):

    def test_nothing(self):
        silly = 'hello world'
        self.assertEqual(silly, 'hello world')


class TestLibSpatialite(TestCase):

    def test_database(self):
        conn = db.connect('test.sqlite')
        cur = conn.cursor()
