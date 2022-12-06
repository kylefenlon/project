from db.run_sql import run_sql
from models.exercise import Exercise
import repositories.day_repository as day_repository
import pdb

def save(exercise):
    sql = "INSERT INTO exercises (name, weight, sets, reps, rest, completed, day_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [exercise.name, exercise.weight, exercise.sets, exercise.reps, exercise.rest, exercise.completed, exercise.day.id]
    results = run_sql(sql, values)
    exercise.id = results[0]['id']


def select_all():
    exercises = []
    sql = "SELECT * FROM exercises"
    results = run_sql(sql)

    for row in results:
        day = day_repository.select(row['day_id'])
        exercise = Exercise(row['name'], row['weight'], row['sets'], row['reps'], row['rest'], row['completed'], day, row['id'])
        exercises.append(exercise)
    return exercises

def select(id):
    exercise = None
    sql = "SELECT * FROM exercises WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        day = day_repository.select(result['day_id'])
        exercise = Exercise(result['name'], result['weight'], result['sets'], result['reps'], result['rest'], result['completed'], day, result['id'])
    return exercise

def delete_all():
    sql = "DELETE FROM exercises"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM exercises WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update_exercise(exercise):
    sql = "UPDATE exercises SET (name, weight, sets, reps, rest, completed, day_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [exercise.name, exercise.weight, exercise.sets, exercise.reps, exercise.rest, exercise.completed, exercise.day.id, exercise.id]
    run_sql(sql, values)