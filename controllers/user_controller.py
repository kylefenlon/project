from flask import Flask, render_template, request, redirect, Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.day_repository as day_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def user():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)

@users_blueprint.route("/users/<id>")
def show_user(id):
    user = user_repository.select(id)
    days = user_repository.days(user)
    return render_template("users/show.html", user=user, days=days)


