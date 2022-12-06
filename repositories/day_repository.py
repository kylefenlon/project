from db.run_sql import run_sql
from models.day import Day
from models.exercise import Exercise
import repositories.user_repository as user_repository


def save(day):
    sql = "INSERT INTO days (name, user_id) VALUES (%s, %s) RETURNING *"
    values = [day.name, day.user.id]
    results = run_sql(sql ,values)
    day.id = results[0]['id']
    return day

def select_all():
    days = []
    sql = "SELECT * FROM days"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        day = Day(row['name'], user, row['id'])
        days.append(day)
    return days

def select(id):
    day = None
    sql = "SELECT * FROM days WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        day = Day(result['name'], user, result['id'])
    return day

def delete_all():
    sql = "DELETE FROM days"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM days WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def exercises(day):
    exercises = []
    sql = "SELECT * FROM exercises WHERE day_id = %s"
    values = [day.id]
    results = run_sql(sql, values)
    for row in results:
        exercise = Exercise(row['name'], row['weight'], row['sets'], row['reps'], row['rest'], row['completed'], day, row['id'])
        exercises.append(exercise)
    return exercises

