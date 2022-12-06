from flask import Flask, render_template, request, redirect, Blueprint
from models.day import Day
import repositories.day_repository as day_repository
import repositories.user_repository as user_repository

days_blueprint = Blueprint("/days", __name__)

@days_blueprint.route("/days")
def days():
    days = day_repository.select_all()
    return render_template("/days/index.html", days=days)

@days_blueprint.route("/days/<id>")
def show_day(id):
    day = day_repository.select(id)
    user = user_repository.select(day)
    return render_template("/days/show.html", day=day, user=user)

#new (form)
@days_blueprint.route('/days/new')
def new_day():
    users = user_repository.select_all()
    return render_template('days/new.html', users=users)

#Creates a new exercise
@days_blueprint.route('/days', methods=['POST'])
def create_day():
    name = request.form['name']
    user_id = request.form['user_id']

    user = user_repository.select(user_id)
    day = Day(name, user)
    day_repository.save(day)
    return redirect('/days')

#deletes a day
@days_blueprint.route('/days/<day_id>/delete', methods=['POST'])
def delete_exercise(day_id):
    day_repository.delete(day_id)
    return redirect('/days')