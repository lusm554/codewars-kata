import psycopg2

class PoException(Exception):
    def __init__(self, text):
        self.txt = text

class Postgres:
    def init(self):
        self.connectline = "dbname=test user=postgres"

    def connect(self):
        self.conn = psycopg2.connect(self.host)
        self.cur = self.conn.cursor()

    def select(self, table, *args):
        if table is None:
            raise PoException("not table defined")
        self.cur.execute(f"select {','.join(args)} from {table}")
        return self.cur.fetchone()

    def commit(self):
        self.conn.commit()


if __name__ == "__main__":
    p = Postgres() 

