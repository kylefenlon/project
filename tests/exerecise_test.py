import unittest

from models.exercise import Exercise
from models.day import Day
from models.user import User

class TestExercise(unittest.TestCase):

    def setUp(self):
        self.user = User("Kyle", 22, "6ft 2in", "81kg")
        self.day = Day("Monday", self.user)
        self.exercise = Exercise("Bench Press", "80kg", 4, 9, "2mins 30secs", False, self.day)
        

    def test_exercise_has_name(self):
        self.assertEqual("Bench Press", self.exercise.name)

    def test_exercise_has_weight(self):
        self.assertEqual("80kg", self.exercise.weight)

    def test_day_has_name(self):
        self.assertEqual("Monday", self.day.name)

    def test_user_has_name(self):
        self.assertEqual("Kyle", self.user.name)

    