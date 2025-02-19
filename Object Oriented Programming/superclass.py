#Created by Ali Adnan
#CMP621A
#February 12th 2025
#This program showcases a superclass with three subclasses that use a __str__ method and shows a fstring


#Classes and variables------------------------------------

class Music:
    def __init__(self, Name, Genre, ReleaseYear, Rating):
        self.Name=Name
        self.Genre=Genre
        self.ReleaseYear=ReleaseYear
        self.Rating=Rating
    def tellall(self):
        print ("Name:", self.Name,)
        print ("Genre:", self.Genre)
        print ("Release Year:", self.ReleaseYear)
        print ("Rating:", self.Rating)

class Song(Music):
    def __init__(self, Name, Artist, Genre, ReleaseYear, Rating):
        Music.__init__(self, Name, Genre, ReleaseYear, Rating )
        self.Artist=Artist
    
    def tell(self):
        print (self.Artist, "Is the artist behind the song", self.Name)
        

class Album(Music):
    def __init__(self, Name, Producers, Genre, ReleaseYear, Rating):
        Music.__init__(self, Name, Genre, ReleaseYear, Rating)
        self.Producers=Producers

    def tell(self):
        print (self.Producers, "Are the Producers behind the Album", self.Name)

class Playlist(Music):
    def __init__(self, Name, Creator, Genre, ReleaseYear, Rating):
        Music.__init__(self, Name, Genre, ReleaseYear, Rating)
        self.Creator=Creator

    def tell(self):
        print (self.Creator, "Is the Creator behind the Playlist", self.Name)

    
albumlist=[
    Album("Hurry Up Tomorrow", "Abel Tesfaye & Leland Wayne","R&B","2025","10 Stars"),
    Album("Dawn FM", "Abel Tesfaye & Max Martin", "2022","Pop","8 Stars"),
    Album("After Hours", "Abel Tesfaye & Illangelo","2020", "Pop", "10 Stars")
]

songlist=[
    Song("Melt Session #1", "Denzel Curry", "Hip Hop", "2022","10 Stars"),
    Song("Walkin'", "Denzel Curry", "Hip Hop", "2022", "10 Stars"),
    Song("Mental", "Denzel Curry", "Hip Hop", "2022", "9 Stars")
]

playlistlist=[
    Playlist("January 2025","Ali Adnan","Pop","2025","7 Stars"),
    Playlist("February 2022","Noah Rashed","Rap","2022","9 Stars"),
    Playlist("Hip Hop Jams","Jayson Blaisdell","Hip Hop","2024","10 Stars")
]


#Main-----------------------------

for album in albumlist:
    album.tellall()
    album.tell()
    print()

for song in songlist:
    song.tellall()
    song.tell()
    print()

for playlist in playlistlist:
    playlist.tellall()
    playlist.tell()
    print()