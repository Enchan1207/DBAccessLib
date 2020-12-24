#
# MySQLアクセサ
#
from urllib.parse import urlparse
import mysql.connector as MySQL
class Accessor():
    def __init__(self, databaseURL):
        self.connection = None
        self.cursor = None

        # 接続
        url = urlparse(databaseURL)
        self.connection = MySQL.connect(
            host = url.hostname or 'localhost',
            port = url.port or 3306,
            user = url.username or 'root',
            password = url.password or 'password',
            database = url.path[1:] or 'database',
        )
        self.connection.ping(reconnect = True)
        self.isConnected = self.connection.is_connected()

        # 接続できたらcursorを作成
        if self.isConnected:
            self.cursor = self.connection.cursor(buffered = True)
        else:
            print("\033[31mERROR:\033[0mcouldn't establish connection.")

    # SQL実行
    def exec(self, sql, param = None) -> bool:
        if not self.isConnected:
            return False

        # paramがタプルならexecute、リストならexecutemany
        paramType = type(param)
        if paramType is tuple:
            self.cursor.execute(sql, param)
        elif paramType is list:
            self.cursor.executemany(sql, param)
        else:
            self.cursor.execute(sql)

        self.connection.commit()
        return True

    # 接続切断
    def disConnection(self):
        self.cursor.close()
        self.connection.close()
        self.isConnected = False

    # フェッチ
    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    # iterable?
    def fetchmany(self, size=1):
        return self.cursor.fetchmany(size)