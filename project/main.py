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

    def generate_initial_games(self):
        count = self._read_int("Сколько игр добавить в библиотеку при запуске? ")

        max_count = len(self.titles)
        if count > max_count:
            print("Столько игр нет в подготовленных массивах. Добавлю " + str(max_count) + ".")
            count = max_count

        for i in range(count):
            game = Game(self.titles[i], self.developers[i], self.years[i], self.genres[i])
            self.library.add_game(game)

    def add_game_manual(self):
        title = input("Название: ")
        developer = input("Разработчик")
        year = self._read_int("Год выпуска: ")
        genre = input("Жанр: ")

        self.library.add_game(Game(title,developer,year,genre))
        print("Игра добавлена")

    def search_menu(self):
        print("\nПоиск:")
        print("1) по названию")
        print("2) по разработчику")
        print("3) по году")
        print("4) по жанру")

        choice = input("Выбор: ")

        if choice == "1":
            title = input("Введите название: ")
            found = self.library.search_by_title(title)
            self.library.show_found(found)

        elif choice == "2":
            dev = input("Введите разработчика: ")
            found = self.library.search_by_developer(dev)
            self.library.show_found(found)

        elif choice == "3":
            year = self._read_int("Введите год: ")
            found = self.library.search_by_year(year)
            self.library.show_found(found)

        elif choice == "4":
            genre = input("Введите жанр: ")
            found = self.library.search_by_genre(genre)
            self.library.show_found(found)

        else:
            print("Неверный пункт поиска.")

    def run(self):
        self.generate_initial_games()

        while True:
            print("\n=== Библиотека видеоигр ===")
            print("1) Показать все игры")
            print("2) Добавить игру вручную")
            print("3) Удалить игру по названию")
            print("4) Поиск игр")
            print("0) Выход")

            cmd = input("Выбор: ")

            if cmd == "1":
                self.library.show_all()

            elif cmd == "2":
                self.add_game_manual()

            elif cmd == "3":
                title = input("Введите название для удаления: ")
                removed = self.library.remove_by_title(title)
                if removed == 0:
                    print("Игры с таким названием не найдены.")
                else:
                    print("Удалено игр: " + str(removed))

            elif cmd == "4":
                self.search_menu()

            elif cmd == "0":
                print("Выход.")
                break

            else:
                print("Неверная команда.")


Main().run()