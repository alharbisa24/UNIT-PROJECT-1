import genre
import rating

class Movie():
    def __init__(self, title:str,description:str, release_year:str,genres:list, ratings: list):
        self.__title= title
        self.__description=description
        self.__release_year = release_year
        self.__genres = []
        self.__ratings = []

    
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
    
    def average_rating(self):
        if not self.__:
            return 0
        return sum(r.score for r in self.ratings) / len(self.ratings)
    
    def getGenres(self) -> list:
        return self.__genres.copy() 
    
    def setGenres(self, genres: list):
        self.__genres.clear()
        if genres:
            self.__genres.extend(genres)
    
    def addGenre(self, genre: genre):
        if genre not in self.__genres:
            self.__genres.append(genre)
    
    def removeGenre(self, genre: genre):
        if genre in self.__genres:
            self.__genres.remove(genre)
    
    def getRating(self) -> list:
        return self.__ratings.copy() 
    
    def setRatings(self, ratings: list):
        self.__ratings.clear()
        if ratings:
            self.__ratings.extend(ratings)
    
    def addRating(self, rating: rating):
        if rating not in self.__ratings:
            self.__ratings.append(rating)
    
    def removeRating(self, rating: rating):
        if rating in self.__ratings:
            self.__ratings.remove(rating)
    