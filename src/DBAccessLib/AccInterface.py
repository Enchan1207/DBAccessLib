#
# DBアクセサ基底インタフェース
#

class _DBAccessorInterface():
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.isConnected = False
        
    # SQL実行
    def exec(self) -> bool:
        if not self.isConnected:
            return False

        return True

    # 接続切断
    def disConnection(self):
        self.cursor.close()
        self.connection.close()
        self.isConnected = False

    # Prepared-Statementでパラメータの置換に使う文字列を返す
    def getReplacer(self) -> str:
        return "?"

    # フェッチ
    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    # iterable?
    def fetchmany(self, size=1):
        return self.cursor.fetchmany(size)