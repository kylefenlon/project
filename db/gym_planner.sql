DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS days;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    height VARCHAR(255),
    weight VARCHAR(255)
);

CREATE TABLE days (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    user_id INT REFERENCES users(id) on DELETE CASCADE
);

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    weight VARCHAR(255),
    sets INT,
    reps INT,
    rest VARCHAR(255),
    completed BOOLEAN,
    day_id INT REFERENCES days(id) ON DELETE CASCADE
);