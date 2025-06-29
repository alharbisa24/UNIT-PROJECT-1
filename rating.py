

class Rating():
   
    def __init__(self, id,movieId,user_id,description,score:float):
        self.__id =id
        self.__movie_id= movieId
        self.__user_id= user_id
        self.__description = description
        self.__score = score


    def getId(self):
        return self.__id
    
    def getMovieId(self):
        return self.__movie_id
    
    def setMovieId(self,movieId):
        self.__movie_id= movieId


    def getUserId(self):
        return self.__user_id
    
    def setUserId(self,userId):
        self.__user_id= userId

    
    def getDescription(self):
        return self.__description
    
    def setDescription(self,description):
        self.__description = description

    def getScore(self):
        return self.__score
    
    def setScore(self,score):
        self.__score = score

    def to_dict(self):
        return {
            "id": self.__id,
            "movie_id": self.__movie_id,
            "user_id": self.__user_id,
            "description": self.__description,
            "score": self.__score,
            
        }
    
    def from_dict(data):
      return Rating(data['id'], data['movie_id'], data['user_id'], data['description'], data['score'])
   


        