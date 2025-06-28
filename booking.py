import movie
import user

class Booking():
    def __init__(self, movie:movie,user:user, row,seat):
        self.__movie=movie
        self.__user=user
        self.__row=row
        self.__seat = seat

    

    def getMovie(self):
        return self.__movie
    
    def setMovie(self,movie:movie):
        self.__movie = movie


    def getUser(self):
        return self.__user
    
    def setUser(self,user:user):
        self.__user = user

    def getRow(self):
        return self.__row
    
    def setRow(self,row):
        self.__row = row

    def getSeat(self):
        return self.__seat
    
    def setSeat(self,seat):
        self.__seat = seat
        