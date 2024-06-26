import mysql.connector as mydb


class DataBaseHandler:
    def __init__(self, host: str, user: str, port: str, password: str, database: str):
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.database = database
        self.conn = self._connect()

    def _connect(self):

        conn = mydb.connect(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            database=self.database,
        )
        return conn

    def ping(self):
        self.conn.ping(reconnect=True)
        print(self.conn.is_connected())
        return self.conn.is_connected()

    def close(self):
        self.conn.close()
        print(self.conn.is_connected())
        return self.conn.is_connected()

    def write(self, query: str):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def select(self, select_query: str):
        cursor = self.conn.cursor()
        cursor.execute(select_query)
        result = cursor.fetchall()
        cursor.close()
        return result
