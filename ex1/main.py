from console_ui.ui import user_input, user_input1


def menu():
    return """
        1 - Draw Letters
        2 - Draw with commands
        3 - Stop
     """


def main():
    while True:
        print(menu())
        opt = int(input('opt= '))
        if opt == 1:
            user_input()
        if opt == 2:
            user_input1()
        if opt == 3:
            break


main()
