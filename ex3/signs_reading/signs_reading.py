def sign_reading():
    signs = ['', '', '']
    f = open("./signs_input", "r")
    for i in range(3):
        word = f.readline()
        while word != '\n' and word != '':
            signs[i] += word
            word = f.readline()
    f.close()
    return signs


def return_signs(signs, sign):
    if sign == "rock":
        return signs[0]
    if sign == 'paper':
        return signs[1]
    if sign == 'scissors':
        return signs[2]
