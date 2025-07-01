class Admin():
    def __init__(self,id, username, password):
        self.__id = id
        self.__username = username
        self.__password= password


    def getId(self):
        return self.__id
    
    def getUsername(self):
        return self.__username
    
    def setUsername(self,username):
        self.__username = username

    def getPassword(self):
        return self.__password
    
    def setPassword(self,password):
        self.__password = password
    

    def to_dict(self):
        return {
            "id": self.__id,
            "username": self.__username,
            "password": self.__password
                        }
    
    def from_dict(data):
      return Admin(data['id'], data['username'], data['password'])