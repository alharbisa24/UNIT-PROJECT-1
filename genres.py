class Genres():
    def __init__(self,id,movieId,name):
        self.__id= id
        self.__movie_id= movieId
        self.__name= name


    def getId(self):
        return self.__id
    
    def getMovieId(self):
        return self.__movie_id

    def getName(self):
        return self.__name
    
    def setMovieId(self,movieid):
        self.__movie_id= movieid
        
    def setName(self,name):
        self.__name= name

   
    def to_dict(self):
        return {
            "id": self.__id,
            "movie_id": self.__movie_id,
            "name": self.__name,
            
        }
    
    def from_dict(data):
      return Genres(data['id'], data['title'], data['description'], data['release_year'])
   


        