import psycopg2


class connection_postgresql:
    def connect_db(self):

        conn = psycopg2.connect(database="demo_database1", user="demo_user", password="demo@1234", host="localhost", port="5432")
        cursor = conn.cursor()
        return cursor
if __name__ == "__main__":
  obj=connection_postgresql()
  cursor = obj.connect_db()