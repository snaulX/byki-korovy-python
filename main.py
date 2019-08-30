from random import randint

count = 4 #количество цифр в загадываемом слове
ai = True #если True то число генерируется самостоятельно, иначе вводится человеком
repetition = False #указывает может ли повторятся цифра в загадываемом числе

def viewsettings():
    print("Количество цифр в загадываемом числе: ", count)
    print("Генерация числа компьютером: ", ai)
    print("Могут ли повторятся цифры в загадываемом числе: ", repetetion)
def settings():
    #word = input("""Введите название параметра, который Вы хотите изменить:
#""")
def play():
    pass

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

