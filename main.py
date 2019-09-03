from random import randint

global count, ai, repetition
count = 4 #количество цифр в загадываемом слове
ai = True #если True то число генерируется самостоятельно, иначе вводится человеком
repetition = False #указывает может ли повторятся цифра в загадываемом числе

def viewsettings():
    print("Количество цифр в загадываемом числе: ", count)
    print("Генерация числа компьютером: ", ai)
    print("Могут ли повторятся цифры в загадываемом числе: ", repetition)
def settings():
    word = input("""Введите название параметра, который Вы хотите изменить:
    count - меняет количество цифр в загадываемом слове
    ai - генерирует число компьютер или человек загадывает сам
    repeat - могут ли повторятся цифры в загадываемом числе
    back - если хотите назад
    """)
    if word == "count":
        count = int(input("Введите количетсво цифр в загадываемом слове: "))
    elif word == "ai":
        ai = bool(input("Введите True если число генерируется само или False если нет: "))
    elif word == "repeat":
        repetition = bool(input("Введите True если цифры могут повторятся или False если нет: "))
    elif word == "back":
        pass
    else:
        print("ERROR: parameter by name '%s' not found. Please try again" % word)
        settings()
    print(count)
def play():
    print("Заданные настройки:")
    viewsettings()
    print()
    if ai:
        number = list()
        for i in range(0, count):
            if not repetition:
                while True:
                    e = str(randint(0, 9))
                    if not e in number:
                        break
            else:
                e = str(randint(0, 9))      
            number.append(e)
    else:
        number = list(input("Введите загадываемое число: "))
        if len(number) != count:
            print("Количество цифр в загадываемом числе не соответсвует настройкам!")
            return
        if repetition:
            for i in number:
                if number.count(i) > 1:
                    print("Цифра %s повторяется!" % i)
                    return
    game = True
    while game:
        numb = list(input("Введите число: "))
        if numb == ['e', 'x', 'i', 't']:
            print("Правильным числом было ", number)
            return
        if len(numb) != len(number):
            print("Количество цифр в вводимом числе не равно количетсву цифр в загадываемом числе!")
            continue
        cows = 0
        byki = 0
        for i in numb:
            try:
                if numb.index(i) == number.index(i):
                    byki = byki + 1
                else:
                    cows = cows + 1
            except ValueError:
                pass
        if byki == count:
            print("Вы угадали число!!!")
            return
        else:
            print("Коровы: {0}. Быки: {1}".format(cows, byki))

print("Быки-Коровы, Александр Гунгер 2019")
print("  ------------------------------  ")
print("Для выхода из программы нажмите Ctrl+C")
while True:
    word = input("""      -     Для показа настроек введите viewsettings
      -     Для изменения настроек введите settings
      -     Для начала игры введите play
      -     Для выхода из программы введите exit
""")
    if word == "viewsettings":
        viewsettings()
    elif word == "settings":
        settings()
    elif word == "play":
        play()
    elif word == "exit":
        exit(0)  
    else:
        print("ERROR: command by name '%s' not found. Please try again" % word)

