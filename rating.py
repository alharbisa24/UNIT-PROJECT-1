import movie
import user


class Rating():
    def __init__(self, description,score:float):
        self.__description = description
        self.__score = score
        self.__user = user
        self.__movie = movie


    def getDescription(self):
        return self.__description
    
    def setDescription(self,description):
        self.__description = description

    def getScore(self):
        return self.__score
    
    def setScore(self,score):
        self.__score = score

    def getUser(self):
        return self.__user

    def setUser(self,user):
        self.__user = user

    def getMovie(self):
        return self.__movie

    def setUser(self,movie):
        self.__movie = movie

    



        