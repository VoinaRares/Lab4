from ex3.signs_reading.signs_reading import return_signs, sign_reading


def show_signs(p, c):
    signs = sign_reading()
    print(f"{return_signs(signs, p.choice)} \n VS \n {return_signs(signs, c.choice)}")