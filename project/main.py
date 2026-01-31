import random
from Game import Game
from Library import Library

class Main:
    def __init__(self):
        self.titles = [
            "Hollow Knight", "Stardew Valley", "Celeste", "Hades", "Terraria",
            "Portal 2", "Dead Cells", "Undertale", "Factorio", "Subnautica"
        ]

        self.developers = [
            "Team Cherry", "ConcernedApe", "Maddy Makes Games", "Supergiant Games", "Re-Logic",
            "Valve", "Motion Twin", "Toby Fox", "Wube Software", "Unknown Worlds"
        ]

        self.years = [2017, 2016, 2018, 2020, 2011, 2011, 2018, 2015, 2020, 2018]

        self.genres = [
            "Metroidvania", "Simulation", "Platformer", "Roguelike", "Sandbox",
            "Puzzle", "Roguelike", "RPG", "Strategy", "Survival"
        ]

        self.library = Library()

    def _read_int(self,prompt):
        s = input(prompt)

        while not s.isdigit():
            print("Enter number: ")
            s = input(prompt)

        return int(s)

    def genarate_initial_games(self):
        count = self._read_int("Сколько игр добавить в библиотеку при запуске?")

        for i in range(count):
            random_index = random.randint(0,len(self.titles))
            game = Game(self.titles[random_index],self.developers[random_index],self.years[random_index],self.genres[random_index])
            self.library.add_game(game)

    def add_game_manual(self):
        title = input("Название: ")
        developer = input("Разработчик")
        year = self._read_int("Год выпуска: ")
        genre = input("Жанр: ")

        self.library.add_game(Game(title,developer,year,genre))
        print("Игра добавлена")