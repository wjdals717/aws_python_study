from userManagement.util.ResponseUtil import ResponseEntity
from userManagement.repository.UserRepository import UserRepository

class UserController: #데이터를 받아서 repository로 보내서 DB에 넣기 위함

    @staticmethod
    def registerUser(user = None):
        responseBody = bool(UserRepository.saveUser(user))  #매개 변수로 받은 user를 넘겨줌 -> db에 저장하게 됨
        return ResponseEntity(body=responseBody)    #응답은 True이면 200으로 전송됨

    @staticmethod
    def getUserAll():
        responseBody = UserRepository.getUserAll()
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getUser(username=None):
        responseBody = UserRepository.findUserByUsername(username)  # 매개 변수로 받은 user를 넘겨줌 -> db에 저장하게 됨
        return ResponseEntity(body=responseBody)

    @staticmethod
    def updateUser(user=None):
        responseBody = UserRepository.updateUser(user)  # 매개 변수로 받은 user를 넘겨줌 -> db에 저장하게 됨
        return ResponseEntity(body=responseBody)

    @staticmethod
    def deleteUser(userId=None):
        responseBody = UserRepository.deleteUser(userId)  # 매개 변수로 받은 user를 넘겨줌 -> db에 저장하게 됨
        return ResponseEntity(body=responseBody)

