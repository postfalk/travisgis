from unittest import TestCase
from sqlite3 import dbapi2 as db
from travisgis.geometry import Geometry


class TestNothing(TestCase):

    def test_nothing(self):
        silly = 'hello world'
        self.assertEqual(silly, 'hello world')


class TestLibSpatialite(TestCase):

    def setUp(self):
        self.obj = Geometry(None)
        self.obj.create_schema()

    def test_database(self):
        self.obj.save()
