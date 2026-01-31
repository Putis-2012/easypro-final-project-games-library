class Game:
    def __init__(self,title,developer,year,genre):
        self.title = title
        self.developer = developer
        self.year  = year
        self.genre = genre

    def show(self,index):
        print(f"{index}) {self.title} | {self.developer} | {self.year} | {self.genre}")