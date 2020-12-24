#
# SQLite3アクセサ
#
from .AccInterface import _DBAccessorInterface

import sqlite3

class Accessor(_DBAccessorInterface):

    def __init__(self, dbPath):
        super().__init__()
        self.connection = sqlite3.connect(dbPath)
        self.cursor = self.connection.cursor()
        self.isConnected = True

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

    # 閉じる
    def close(self):
        self.connection.close()
    