from random import randint

def viewsettings():
    pass
def settings():
    pass
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

