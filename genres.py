class Genres():
    def __init__(self,id,name, movies = []):
        self.__id= id
        self.__movies= movies if movies else []
        self.__name= name


    def getId(self):
        return self.__id
    
    def getMovies(self):
        return self.__movies
    
    

    def getName(self):
        return self.__name
    

        
    def setName(self,name):
        self.__name= name



    def addMovie(self, movie_id):
        if movie_id not in self.__movies:
            self.__movies.append(movie_id)
            return True
        return False
    
    def removeMovie(self, movie_id):
        if movie_id in self.__movies:
            self.__movies.remove(movie_id)
            return True
        return False
    
    def hasMovie(self, movie_id):
        return movie_id in self.__movies
    
    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "movies": self.__movies,

        }
    
    def from_dict(data):
      return Genres(data['id'], data['name'], data['movies'])
   


        