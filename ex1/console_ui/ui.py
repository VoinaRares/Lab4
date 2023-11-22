import turtle
from ex1.logic.signs import (draw_a, draw_b, draw_c, draw_d, draw_e, draw_f, draw_g, draw_h, draw_i, draw_j, draw_k,
                             draw_l, draw_m, draw_n, draw_o, draw_p, draw_q, draw_r, draw_s, draw_t, draw_u, draw_v,
                             draw_w, draw_x, draw_y, draw_z, draw_dot, draw_exclam, draw_question)

from ex1.logic.commands import w, s, d, a, f, g


def find_word_pos(sentence, word):
    for i in range(len(sentence)):
        if word == sentence[i]:
            return i + 1


def user_input():
    wn = turtle.Screen()
    wn.clear()
    function_dic = {"a": draw_a, "b": draw_b, "c": draw_c, "d": draw_d, "e": draw_e, "f": draw_f, "g": draw_g,
                    "h": draw_h, "i": draw_i, "j": draw_j, "k": draw_k, "l": draw_l, "m": draw_m, "n": draw_n,
                    "o": draw_o, "p": draw_p, "q": draw_q, "r": draw_r, "s": draw_s, "t": draw_t, "u": draw_u,
                    "v": draw_v, "w": draw_w, "x": draw_x, "y": draw_y, "z": draw_z, ".": draw_dot, "!": draw_exclam,
                    "?": draw_question}

    command_dict = {"w": w, "s": s, "d": d, "a": a, "f": f, "g": g}
    p = turtle.Turtle()
    text = input('Your input is:')
    shift = 0
    ok = True
    for character in text:
        if character not in 'abcdefghijklmnopqrtsuvwxyz?!.':
            ok = False
    if ok is True:
        for i in range(len(text)):
            if text[i] == ' ':
                shift += 100
            else:
                function_dic[text[i]](shift)
                shift += 80
    else:
        read_file = open('input.txt', 'r')
        input_list = []
        are_commands = True
        for word in read_file:
            input_list.append(word.strip())
        for character in text:
            if character not in input_list:
                are_commands = False
        read_file.close()
        if are_commands is True:
            for character in text:
                command = input_list[find_word_pos(input_list, character)]
                for elem in command:
                    command_dict[elem](p)


def user_input1():
    wn = turtle.Screen()
    wn.clear()
    inputs = []
    command_dict = {"w": w, "s": s, "d": d, "a": a, "f": f, "g": g}

    input_string = input('your input is:')

    read_file = open('input.txt', 'r')
    for command in read_file:
        inputs.append(command)

    if (input_string + '\n') in inputs:
        print("This command already exists")
    else:
        command_input = input('What sign do you wanna assign it to: ')
        while (command_input + '\n' in inputs) or (command_input in 'abcdefghijklmnopqrtsuvwxyz?!.'):
            command_input = input("Please enter a sign that doesnt already have commands attached to it: ")

        fi = open('input.txt', 'w')
        inputs.append(command_input)
        inputs.append('\n')
        inputs.append(input_string)
        fi.writelines(inputs)
        fi.write('\n')
        fi.close()

        p = turtle.Turtle()

        for i in range(len(input_string)):
            command_dict[input_string[i]](p)
    read_file.close()
