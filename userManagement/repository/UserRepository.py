from userManagement.config.DataBaseConfig import DataBaseConfig, pymysql
import pandas as pd

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        try:
            connection = DataBaseConfig.getConnection(); #DB와 연결된 객체를 의미
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = f"""
            insert into user_tb
            values(0, %s, %s, %s, %s)
            """
            insertCount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
            connection.commit() #트랜젝션 마무리, insert가 실행됨!
            return insertCount
        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def getUserAll():
        try:
            connection = DataBaseConfig.getConnection(); #실행할 때마다 DB에 연결해야 함!!
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            select
                user_id as userId,
                username,
                password,
                name,
                email
            from
                user_tb
            """
            cursor.execute(sql)
            rs = cursor.fetchall()      #하나만 리턴하고 싶은 경우, 리스트에 담느냐/안 담느냐의 차이, fetchone은 리스트의 첫번째를 가져옴
            return rs
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def findUserByUsername(username=None):
        try:
            connection = DataBaseConfig.getConnection();  # 실행할 때마다 DB에 연결해야 함!!
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = f"""
                select
                    user_id as userId,
                    username,
                    password,
                    name,
                    email
                from
                    user_tb
                where
                    username = %s
                """
            cursor.execute(sql, username)
            rs = cursor.fetchone()  # 하나만 리턴하고 싶은 경우, 리스트에 담느냐/안 담느냐의 차이, fetchone은 리스트의 첫번째를 가져옴
            return rs

        except Exception as e:
            print(e)
            return None

    @staticmethod
    def updateUser(user=None):
        try:
            connection = DataBaseConfig.getConnection();  # DB와 연결된 객체를 의미
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = f"""
                update user_tb
                set
                    password = %s,
                    name = %s,
                    email = %s
                where
                    user_id = %s
                """
            insertCount = cursor.execute(sql,
                                         (user.get("password"), user.get("name"), user.get("email"), user.get("userId")))
            connection.commit()  # 트랜젝션 마무리, insert가 실행됨!
            return insertCount
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def deleteUser(userId):
        try:
            connection = DataBaseConfig.getConnection();  # 실행할 때마다 DB에 연결해야 함!!
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = f"""
                   delete from user_tb
                   where
                        user_id = %s
                   """
            cursor.execute(sql, userId)
            rs = cursor.fetchone()  # 하나만 리턴하고 싶은 경우, 리스트에 담느냐/안 담느냐의 차이, fetchone은 리스트의 첫번째를 가져옴
            return rs

        except Exception as e:
            print(e)
            return None

if __name__ == '__main__':
    userList = UserRepository.getUserAll()
    # print(userList)

    data = {
        "userId": [1, 2, 3],
        "username": ["aaa", "bbb", "ccc"],
        "password": ["1234", "1111", "222"],
        "name": ["aaa", "bbb", "ccc"],
        "email": ["aaa@gmail.com", "bbb@gmail.com", "ccc@gmail.com"]
    }

    # print(pd.Series(userList)) #한 개의 딕셔너리만 가능

    df = pd.DataFrame(userList) #리스트만 가능함
    print(df)
    # print(df.get("username"))






