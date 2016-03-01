from unittest import TestCase
from sqlite3 import dbapi2 as db
from travisgis.geometry import Point


class TestNothing(TestCase):

    def test_nothing(self):
        silly = 'hello world'
        self.assertEqual(silly, 'hello world')


class TestLibSpatialite(TestCase):

    def setUp(self):
        self.obj = Point('10', '20')
        self.obj.create_schema()

    def tearDown(self):
        self.obj

    def test_database(self):
        self.obj.save()
