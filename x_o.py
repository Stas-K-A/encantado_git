def weelcome(): # Правила игры
    print("------------------------------")
    print("     ИГРА КРЕСТИКИ НОЛИКИ     ")
    print("------------------------------")
    print("           ПРАВИЛА            ")
    print('ПЕРВЫЙ ИГРОК - "Х"   "КРЕСТИК"')
    print('ВТОРОЙ ИГРОК - "О"     "НОЛИК"')
    print("------------------------------")
    print("   ИГРОКИ ХОДЯТ ПООЧЕРЕДНО    ")
    print("ЧЕРЕЗ ПРОБЕЛ НЕОБХОДИМО ВВЕСТИ")
    print("          ДВА ЧИСЛА           ")
    print(" НОМЕР СТРОКИ И НОМЕР СТОЛБЦА ")
    print("------------------------------")
    print("            ПОЕХАЛИ!          ")


def show_field(F): # Вывод игрового поля
    print(f"\n\t\t\t  | 0 | 1 | 2 |")
    print(f"\t\t\t---------------")
    for i, row in enumerate(F):
        row_fields = " | ".join(row) # Обращаемся к элементам списка F
                                   # без использования индекса i
        print(f"\t\t\t{i} | {row_fields} |")
        print(f"\t\t\t---------------")

def play_x_o(F): # Ход игрока 
 
    while True:
        digits_2 = input(
            "\n\tВведите два числа через пробел - номер строки и столбца:"
            ).split()
        
        if len(digits_2) != 2: # Проверка количества введенных координат - x и y
            print("\nЧисло может быть либо - 0, либо - 1, либо - 2")
            continue
        x, y = digits_2 # Проверка координат - должны быть числовые значения
        if not(x.isdigit()) or not(y.isdigit()):
            print("\nНекорректное значение!")
            continue

        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2: # Проверка координат - числа 0, 1, 2
            print("\nЧисло вне диапазона 0, 1, 2")
            continue

        if F[x][y] != "-": # Проверка клетки на использование игроком
            print("\nКлетка занята!")
            continue

        return x,y

def win(F): # Проверка выигрышной комбинации
    win_combination = (((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
                       ((0, 2), (1, 2), (2, 2)), ((0, 0), (0, 1), (0, 2)),
                       ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                       ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    
    for combination in win_combination:
        chars = []
        for char in combination:
            chars.append(F[char[0]][char[1]])
        if chars == ["X", "X", "X"]:
            print('\n\t\tПОБЕДА! - "КРЕСТИКИ" - "X"')
            return True
        if chars == ["O", "O", "O"]:
            print('\n\t\tПОБЕДА! - "НОЛИКИ" - "O"')
            return True
    return False


fields =  [['-']*3 for _ in range(3)] # Генератор  двумерного массива 3х3
count_play = 0 # Номер хода   - максимальное число ходов в игре = 9
               # Нечетный ход - "КРЕСТИК" - "X"
               # Четный ход   - "НОЛИК"   - "O"


weelcome()               
while True:
    count_play += 1

    show_field(fields) # Вывод игрового поля

    if count_play%2 == 1: # Нечетный ход - "X"
        print('\nВаш ход - "КРЕСТИК" - "Х"')
        x, y = play_x_o(fields)
        fields[x][y] = "X"
    if count_play%2 == 0: # Четный ход - "O"
        print('\nВаш ход - "НОЛИК" - "О"')
        x, y = play_x_o(fields)
        fields[x][y] = "O"
    if win(fields): # Проверка выигрышных комбинаций
        show_field(fields)
        break
    if count_play == 9:
        show_field(fields)
        print("\n\t\tИГРА ОКОНЧЕНА - НИЧЬЯ!")
        break
    







