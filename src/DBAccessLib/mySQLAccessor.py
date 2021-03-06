#
# MySQLアクセサ
#
from .AccInterface import _DBAccessorInterface

from urllib.parse import urlparse
import mysql.connector as MySQL

class Accessor(_DBAccessorInterface):
    def __init__(self, databaseURL):
        super().__init__()

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

    # Prepared-Statementでパラメータの置換に使う文字列を返す
    def getReplacer(self) -> str:
        return "%s"

    # フェッチ
    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    # iterable?
    def fetchmany(self, size=1):
        return self.cursor.fetchmany(size)