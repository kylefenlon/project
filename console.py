from models.day import Day
from models.exercise import Exercise
from models.user import User

from repositories import user_repository
from repositories import day_repository
from repositories import exercise_repository

user_repository.delete_all()
day_repository.delete_all()
exercise_repository.delete_all()

user1 = User("Kyle", 22, "6ft 2in", "82kg")
user_repository.save(user1)

user_repository.select_all()

day1 = Day("Day 1", user1)
day_repository.save(day1)

day2 = Day("Day 2", user1)
day_repository.save(day2)

day3 = Day("Day 3", user1)
day_repository.save(day3)


exercise1 = Exercise("Bench Press", "80kg", 4, 8, "2mins", False, day1)
exercise_repository.save(exercise1)

exercise2 = Exercise("Cable Row", "55kg", 4, 12, "2mins", False, day1)
exercise_repository.save(exercise2)

exercise3 = Exercise("Lat Pulldowns", "70kg", 3, 9, "2mins", False, day1)
exercise_repository.save(exercise3)

exercise4 = Exercise("Incline Bench Press", "80kg", 4, 6, "2mins 30secs", False, day1)
exercise_repository.save(exercise4)

exercise5 = Exercise("Tricep Rope Pulls", "25kg", 3, 12, "2mins", False, day2)
exercise_repository.save(exercise5)

exercise6 = Exercise("Bicep Curls", "14kg", 4, 8, "2mins 30secs", False, day2)
exercise_repository.save(exercise6)

exercise7 = Exercise("Skull Crushers", "16kg", 3, 10, "2mins", False, day2)
exercise_repository.save(exercise7)

exercise8 = Exercise("Hammer Curls", "12kg", 3, 12, "2mins", False, day2)
exercise_repository.save(exercise8)

exercise9 = Exercise("BSS", "40kg", 3, 12, "3mins", False, day3)
exercise_repository.save(exercise9)

exercise10 = Exercise("Leg Extensions", "78kgkg", 3, 8, "2mins 30secs", False, day3)
exercise_repository.save(exercise10)

exercise11 = Exercise("RDL", "100kg", 3, 7, "3mins", False, day3)
exercise_repository.save(exercise11)

exercise12 = Exercise("Calve Raises", "40kgkg", 3, 20, "90secs", False, day3)
exercise_repository.save(exercise12)
