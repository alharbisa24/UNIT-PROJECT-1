class User():
    def __init__(self,id, email):
        self.__id = id
        self.__email = email


    def getId(self):
        return self.__id
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self,email):
        self.__email = email

    def to_dict(self):
        return {
            "id": self.__id,
            "email": self.__email,
        }
    
    def from_dict(data):
      return User(data['id'], data['email'])