'''5.	Create a class that represents pieces of music. Define a class constructor that allows you to set the initial values of the music piece 
(artist, track title, album, year) when the object is created. Complete the class with the __str__ method returning the song data as a string, 
in the format as below (4 lines).
Performer: Ed Sheeran
Song:      Hearts Don't Break Around Here
Album:     Divide
Year:      2017
Then create three objects that represent three different pieces of music. Display these objects.
'''


class Music():
    
    def __init__(self, artist, title, album, year):
        self.artist = artist 
        self.title = title 
        self.album = album 
        self.year = year 
        
    
    def __str__(self):  
        return "Performer: " + self.artist + "\nSong: " + self.title + "\nAlbum: " + self.album + "\nYear: " + self.year
    
my_song = Music('Ed Sheeran', 'Hearts Dont Break Around Here', 'Divide', '2017')
print(my_song)      
