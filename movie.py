import rating

class Movie():
    def __init__(self,id:int, title:str,description:str, release_year:str):
        self.__id = id
        self.__title= title
        self.__description=description
        self.__release_year = release_year

    def getId(self):
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
    
    def setTitle(self, title: str):
        self.__title = title
    
    def getDescription(self) -> str:
        return self.__description
    
    def setDescription(self, description: str):
        self.__description = description
    

    def getReleaseYear(self):
        return self.__release_year
    
    def setReleaseYear(self, release_year):
        self.__release_year = release_year
    


    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.__title,
            "description": self.__description,
            "release_year": self.__release_year,
            
        }
    
    def from_dict(data):
      return Movie(data['id'], data['title'], data['description'], data['release_year'])
   

