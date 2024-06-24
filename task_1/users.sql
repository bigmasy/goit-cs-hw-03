--Table: users
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

--Table: status
DROP TABLE IF EXISTS status;
CREATE TABLE status(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);
INSERT INTO status (name) VALUES ('new'), ('in progress'), ('completed');

--Table: tasks
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_status
        FOREIGN KEY(status_id) 
        REFERENCES status(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id) 
        REFERENCES users(id)
        ON DELETE CASCADE


);