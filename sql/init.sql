CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO tasks (title, done)
SELECT 'Learn FastAPI', FALSE
WHERE NOT EXISTS (
    SELECT 1 FROM tasks WHERE title = 'Learn FastAPI'
);

INSERT INTO tasks (title, done)
SELECT 'Build CRUD API', FALSE
WHERE NOT EXISTS (
    SELECT 1 FROM tasks WHERE title = 'Build CRUD API'
);

INSERT INTO tasks (title, done)
SELECT 'Push to GitHub', FALSE
WHERE NOT EXISTS (
    SELECT 1 FROM tasks WHERE title = 'Push to GitHub'
);
