from db.run_sql import run_sql
from models.user import User
from models.day import Day

def save(user):
    sql = "INSERT INTO users (name, age, height, weight) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [user.name, user.age, user.height, user.weight]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['age'], row['height'], row['weight'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        user = User(result['name'], result['age'], result['height'], result['weight'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def days(user):
    days = []
    sql = "SELECT * FROM days WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)
    for row in results:
        day = Day(row['name'], user, row['id'])
        days.append(day)
    return days

def update(user):
    sql = "UPDATE users SET (name, age, height, weight) = (%s, %s) WHERE id = %s"
    values = [user.name, user.age, user.height, user.weight, user.id]
    run_sql(sql, values)

 