import random


class Cell:
    """Класс для представления клетки игрового поля"""

    def __init__(self, around_mines=0, mine=False):
        self.around_mines = 0
        self.mine = False
        self.fl_open = False  # закрыта/открыта клетка


class GamePole:
    """Класс для управления игровым полем, размером N x N клеток """

    def __init__(self, size_of_pole: int, mins_quantity: int) -> None:
        self.size_of_pole = size_of_pole
        self.mins_quantity = mins_quantity
        self.pole = None
        self.init()

    @staticmethod
    def set_mine(cell: Cell) -> None:
        cell.mine = True

    def init(self):
        """Инициализация поля с новой расстановкой мин."""
        mins_quantity = self.mins_quantity
        self.pole = []
        # Сначала создаем пустое поле
        for i in range(self.size_of_pole):
            row = []
            for j in range(self.size_of_pole):
                row.append(Cell())
            self.pole.append(row)
        # установка бомб
        mines = self.mins_quantity
        while mines:
            position = random.randrange(0, self.size_of_pole ** 2)

            column = 0

            while position >= self.size_of_pole:
                column += 1
                position -= self.size_of_pole
            if self.pole[column][position].mine:
                continue
            else:
                self.pole[column][position].mine = True
                mines -= 1

            # расстановка цифр вокруг бомбы

            if column == 0:
                if position == 0:
                    self.pole[column][1].around_mines += 1
                    self.pole[column + 1][1].around_mines += 1
                    self.pole[column + 1][0].around_mines += 1
                elif position == self.size_of_pole - 1:
                    self.pole[column][position - 1].around_mines += 1
                    self.pole[column + 1][position].around_mines += 1
                    self.pole[column + 1][position - 1].around_mines += 1
                else:
                    self.pole[column][position + 1].around_mines += 1
                    self.pole[column][position - 1].around_mines += 1
                    self.pole[column + 1][position].around_mines += 1
                    self.pole[column + 1][position + 1].around_mines += 1
                    self.pole[column + 1][position - 1].around_mines += 1

            elif column == self.size_of_pole - 1:
                if position == 0:
                    self.pole[column][1].around_mines += 1
                    self.pole[column - 1][1].around_mines += 1
                    self.pole[column - 1][0].around_mines += 1
                elif position == self.size_of_pole - 1:
                    self.pole[column][position - 1].around_mines += 1
                    self.pole[column - 1][position].around_mines += 1
                    self.pole[column - 1][position - 1].around_mines += 1
                else:
                    self.pole[column][position + 1].around_mines += 1
                    self.pole[column][position - 1].around_mines += 1
                    self.pole[column - 1][position].around_mines += 1
                    self.pole[column - 1][position + 1].around_mines += 1
                    self.pole[column - 1][position - 1].around_mines += 1
            else:
                if position == 0:
                    self.pole[column][1].around_mines += 1
                    self.pole[column + 1][1].around_mines += 1
                    self.pole[column - 1][1].around_mines += 1
                    self.pole[column - 1][0].around_mines += 1
                    self.pole[column + 1][0].around_mines += 1
                elif position == self.size_of_pole - 1:
                    self.pole[column][position - 1].around_mines += 1
                    self.pole[column - 1][position].around_mines += 1
                    self.pole[column - 1][position - 1].around_mines += 1
                    self.pole[column + 1][position].around_mines += 1
                    self.pole[column + 1][position - 1].around_mines += 1

                else:
                    self.pole[column][position + 1].around_mines += 1
                    self.pole[column][position - 1].around_mines += 1
                    self.pole[column - 1][position].around_mines += 1
                    self.pole[column - 1][position + 1].around_mines += 1
                    self.pole[column - 1][position - 1].around_mines += 1
                    self.pole[column + 1][position + 1].around_mines += 1
                    self.pole[column + 1][position - 1].around_mines += 1
                    self.pole[column + 1][position].around_mines += 1

    def show(self) -> None:
        """Отображение поля в консоли. Если клетка не открыта, то отображается символ #;
        Мина отображается символом *;
        Между клетками - пробел."""
        for i in self.pole:
            for j in i:
                if j.fl_open == False:
                    print('#', end=' ')
                elif j.mine:
                    print('*', end=' ')
                else:
                    print(j.around_mines, end=' ')
            # смена строки
            print()

    def open_cell(self, row: int, column: int) -> bool:
        """Открытие клетки и проверка на бомбу"""
        self.pole[row - 1][column - 1].fl_open = True
        if self.pole[row - 1][column - 1].mine:
            return False
        else:
            return True

    def open_mine(self, row: int, column: int) -> bool:
        """Открытие клетки, где предроложительно расположена бомба"""
        self.pole[row - 1][column - 1].fl_open = True
        if self.pole[row - 1][column - 1].mine:
            return True
        else:
            return False

    def play(self):
        """Метод, который запускает игру и перчатает все необходимое для нее.
        Также обрабатывает ошибки ввода."""
        print()
        self.show()
        print()
        print("Вы хотите попробовать открыть клеточку(введите 1)?\n"
              "Хотите обнаружить бомбу(введите 2)?")
        # Обработка некоректного ввода
        try:
            num = int(input())
        except:
            print()
            print('Вы ввели некоректное значение, попробуем еще раз')
            self.play()
        # Сценарий открытия клеточки без бомбы
        if num == 1:
            print('Введите число строчки и столбика через пробел', end=' ')
            # Проверка на коректность ввода
            try:
                row, column = [int(i) for i in input().split()]
                # дополнительная проверка на диапазон чисел, доступных в игре
                if row > self.size_of_pole or column > self.size_of_pole:
                    raise ValueError
            except:
                print('Вы ввели некоркетное значение, попробуем еще раз')
                self.play()
            result = self.open_cell(row, column)
            if result:
                print()
                self.play()
            else:
                print('Вы проирали')
        # Сценарий открытия клеточки с бомбой
        elif num == 2:
            print()
            print('Введите число строчки и столбика через пробел', end=' ')
            try:
                row, column = [int(i) for i in input().split()]
                # дополнительная проверка на диапазон чисел, доступных в игре
                if row > self.size_of_pole or column > self.size_of_pole:
                    raise ValueError
            except:
                print('Вы ввели некоркетное значение, попробуем еще раз')
                self.play()
            result = self.open_mine(row, column)
            if result:
                print()
                self.play()
            else:
                print('Вы проирали')
        else:
            print('Вы ввели некоректное значение')
            self.play()


n = 10  # размер поля
m = 12  # количество мин
pole_game = GamePole(n, m)
pole_game.play()
