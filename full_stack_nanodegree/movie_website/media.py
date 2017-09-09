import webbrowser

class Video():
    def __init__(self, title, duration, box_art):
        self.title = title
        self.duration = duration
        self.poster_image_url = box_art
        
        
class Movie(Video):
    def __init__(self, title, duration, storyline, box_art, youtube_trailer):
        Video.__init__(self, title, duration, box_art)
        self.storyline = storyline
        self.trailer_youtube_url = youtube_trailer
        
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)