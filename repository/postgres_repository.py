from database import get_connection


class PostgresTaskRepository:

    def get_all(self):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM tasks ORDER BY id")
                return cursor.fetchall()
        finally:
            conn.close()

    def get_by_id(self, task_id):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM tasks WHERE id = %s",
                    (task_id,)
                )
                return cursor.fetchone()
        finally:
            conn.close()

    def create(self, title, done):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO tasks (title, done)
                    VALUES (%s, %s)
                    RETURNING id, title, done
                    """,
                    (title, done)
                )
                task = cursor.fetchone()
                conn.commit()
                return task
        finally:
            conn.close()

    def update(self, task_id, title, done):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE tasks
                    SET title = %s, done = %s
                    WHERE id = %s
                    RETURNING id, title, done
                    """,
                    (title, done, task_id)
                )
                task = cursor.fetchone()
                conn.commit()
                return task
        finally:
            conn.close()

    def delete(self, task_id):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM tasks WHERE id = %s",
                    (task_id,)
                )
                deleted = cursor.rowcount > 0
                conn.commit()
                return deleted
        finally:
            conn.close()
