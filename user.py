class User():
    def __init__(self,email:str,movies:list):
        self.__email=email
        self.__movies =movies

    
    def getEmail(self):
        return self.__email
    
    def setEmail(self,email):
        self.__email = email

    def getMovies(self):
        return self.__movies

    def setMovies(self,movies):
        self.__movies= movies