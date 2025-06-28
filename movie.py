import genre

class Movie():
    def __init__(self, title:str,description:str,price:int, release_year:str,row,seat,genres:list, date,time, ratings: list):
        self.__title= title
        self.__description=description
        self.__price= price
        self.__release_year = release_year
        self.__row= row
        self.__seat= seat
        self.__genres = []
        self.__ratings = []
        self.__date = date
        self.__time= time

    
    def getTitle(self) -> str:
        return self.__title
    
    def setTitle(self, title: str):
        self.__title = title
    
    def getDescription(self) -> str:
        return self.__description
    
    def setDescription(self, description: str):
        self.__description = description
    
    def getPrice(self) -> int:
        return self.__price
    
    def setPrice(self, price: int) :
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("price cannot be negative")
    

    def getReleaseYear(self):
        return self.__release_year
    
    def setReleaseYear(self, release_year):
        self.__release_year = release_year
    
    def getRow(self):
        return self.__row
    
    def setRow(self, row):
        self.__row = row

    def getSeat(self):
        return self.__seat
    
    def setSeat(self, seat):
        self.__seat = seat

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
    
    def getDate(self):
        return self.__date
    
    def setDate(self, date):
        self.__date = date


    def getTime(self):
        return self.__time
    
    def setTime(self, time):
        self.__time = time
    