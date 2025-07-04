class User():
    def __init__(self,id, email, password):
        self.__id = id
        self.__email = email
        self.__password= password


    def getId(self):
        return self.__id
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self,email):
        self.__email = email

    def getPassword(self):
        return self.__password
    
    def setPassword(self,password):
        self.__password = password
    

    def to_dict(self):
        return {
            "id": self.__id,
            "email": self.__email,
            "password": self.__password
                            }
    
    def from_dict(data):
      return User(data['id'], data['email'], data['password'])