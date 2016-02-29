from unittest import TestCase


class TestNothing(TestCase):

    def test_nothing(self):
        silly = 'hello world'
        self.assertEqual(silly, 'hello world')
