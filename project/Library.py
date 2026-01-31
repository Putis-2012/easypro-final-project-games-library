class Library:
    def __init__(self):
        self.games = []

    def add_game(self,game):
        self.games.append(game)

    def show_all(self):
        if len(self.games) == 0:
            print("Library is empty")
            return

        for i in range(len(self.games)):
            self.games[i].show(i + 1)

    def remove_by_title(self,title):
        title_low = title.lower()

        for i in range(len(self.games)):
            if self.games[i].title.lower() == title_low:
                self.games.pop(i)

    def search_by_title(self,title):
        found = []
        title_low = title.lower()

        for i in range(len(self.games)):
            if self.games[i].title.lower() == title_low:
                found.append(games[i])

        return found

    def search_by_developer(self,developer):
        found = []
        developer_low = developer.lower()

        for i in range(len(self.games)):
            if self.games[i].developer.lower() == developer_low:
                found.append(games[i])

        return found

    def search_by_year(self,year):
        found = []

        for i in range(len(self.games)):
            if self.games[i].year == year:
                found.append(games[i])

        return found

    def search_by_genre(self,genre):
        found = []
        genre_low = genre.lower()

        for i in range(len(self.games)):
            if self.games[i].genre.lower() == genre_low:
                found.append(games[i])

        return found

    def show_found(self,found):
        if len(found) == 0:
            print("Ничего не найдено")

        for i in range(len(found)):
            found[i].show(i + 1)