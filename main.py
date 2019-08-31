from random import randint

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
def play():
    print("Заданные настройки:")
    viewsettings()
    print()
    if ai:
        number = list(str(randint(0, 10)))
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
        pass
        # numb = list(input("Введите число: "))        

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

