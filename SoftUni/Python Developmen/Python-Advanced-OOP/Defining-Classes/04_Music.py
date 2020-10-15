class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is {self.title} from {self.artist}'

    def play(self):
        return self.lyrics


song1 = Music("Title", "Artist", "Lyrics")
song2 = Music("Title2", "Artist2", "Lyrics2")

print(song1.print_info())
print(song1.play())

print(song2.print_info())
print(song2.play())