import pymysql

class DataBaseConfig:
    @staticmethod
    def getConnection():
        host = "127.0.0.1"
        port = 3306
        user = "root"
        password = "1q2w3e4r"
        database = "python_study"

        return pymysql.connect(     #connect: DB에 연결시키는 역할
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )