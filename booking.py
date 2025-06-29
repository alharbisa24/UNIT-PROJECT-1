import movie

class Booking():
    
    def __init__(self, id,movie_id:str,user_id:str, row,seat):
        self.__id=id
        self.__movie_id=movie_id
        self.__user_id=user_id
        self.__row=row
        self.__seat = seat

    
    def getId(self):
        return self.__id

    def getMovieId(self):
        return self.__movie_id
    
    def setMovieId(self,movieid:str):
        self.__movie_id = movieid

    def getUserId(self):
        return self.__user_id
    
    def setUserId(self,userid:str):
        self.__user_id = userid

   

    def getRow(self):
        return self.__row
    
    def setRow(self,row):
        self.__row = row

    def getSeat(self):
        return self.__seat
    
    def setSeat(self,seat):
        self.__seat = seat
        

    def to_dict(self):
        return {
            "id": self.__id,
            "movie_id": self.__movie_id,
            "user_id": self.__user_id,
            "row": self.__row,
            "seat": self.__seat,
            
        }
    
    def from_dict(data):
      return Booking(data['id'], data['movie_id'], data['user_id'], data['row'], data['seat'])
   

