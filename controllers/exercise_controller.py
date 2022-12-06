from flask import Flask, render_template, request, redirect, Blueprint
from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository
import repositories.day_repository as day_repository
import pdb

exercises_blueprint = Blueprint('exercises', __name__)

#This gets all exercises
@exercises_blueprint.route('/exercises')
def exercises():
    exercises = exercise_repository.select_all()
    return render_template('exercises/index.html', exercises=exercises)

#This shows one specific exercise
@exercises_blueprint.route('/exercises/<exercise_id>')
def show_exercise(exercise_id):
    exercise = exercise_repository.select(int(exercise_id))
    return render_template("exercises/show.html", exercise=exercise)

#new (form)
@exercises_blueprint.route('/exercises/new')
def new_exercise():
    days = day_repository.select_all()
    return render_template('exercises/new.html', days=days)



#Creates a new exercise
@exercises_blueprint.route('/exercises', methods=['POST'])
def create_exercise():
    name = request.form['name']
    weight = request.form['weight']
    sets = request.form['sets']
    reps = request.form['reps']
    rest = request.form['rest']
    completed = request.form['completed']
    day_id = request.form['day_id']

    day = day_repository.select(day_id)
    exercise = Exercise(name, weight, sets, reps, rest, completed, day)
    exercise_repository.save(exercise)
    return redirect('/exercises')

#edits an exercise
@exercises_blueprint.route('/exercises/<exercise_id>/edit')
def edit_exercise(exercise_id):
    exercise = exercise_repository.select(exercise_id)
    days = day_repository.select_all()
    return render_template('exercises/edit.html', days=days, exercise=exercise)

#DELETES an exercise
@exercises_blueprint.route('/exercises/<exercise_id>/delete', methods=['POST'])
def delete_exercise(exercise_id):
    exercise_repository.delete(exercise_id)
    return redirect('/exercises')

@exercises_blueprint.route('/exercises/<exercise_id>', methods=['POST'])
def update_exercise(exercise_id):
    name = request.form['name']
    weight = request.form['weight']
    sets = request.form['sets']
    reps = request.form['reps']
    rest = request.form['rest']
    completed = request.form['completed']
    day_id = request.form['day_id']

    day = day_repository.select(day_id)
    exercise = Exercise(name, weight, sets, reps, rest, completed, day, exercise_id)
    exercise_repository.update_exercise(exercise)
    return redirect('/days/' + day_id)

@exercises_blueprint.route('/exercises/<exercise_id>/complete')
def toggle_complete(exercise_id):
    exercise = exercise_repository.select(exercise_id)
    exercise.completed = not exercise.completed
    exercise_repository.update_exercise(exercise)
    return redirect(request.referrer)


