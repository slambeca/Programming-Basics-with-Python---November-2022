word = ""

c_iteration = 0
o_iteration = 0
n_iteration = 0

c_has_occurred = False
n_has_occurred = False
o_has_occurred = False

input_line = input()

while input_line != "End":
    letter = input_line
    if letter == "a":
        word += letter
    elif letter == "b":
        word += letter
    elif letter == "c":
        c_iteration += 1
        if c_iteration != 1:
            c_has_occurred = True
    elif letter == "d":
        word += letter
    elif letter == "e":
        word += letter
    elif letter == "f":
        word += letter
    elif letter == "g":
        word += letter
    elif letter == "h":
        word += letter
    elif letter == "i":
        word += letter
    elif letter == "j":
        word += letter
    elif letter == "k":
        word += letter
    elif letter == "l":
        word += letter
    elif letter == "m":
        word += letter
    elif letter == "n":
        n_iteration += 1
        if n_iteration != 1:
            n_has_occurred = True
    elif letter == "o":
        o_iteration += 1
        if o_iteration != 1:
            if o_iteration == 2:
                word += letter
            o_has_occurred = True
    elif letter == "p":
        word += letter
    elif letter == "q":
        word += letter
    elif letter == "r":
        word += letter
    elif letter == "s":
        word += letter
    elif letter == "t":
        word += letter
    elif letter == "u":
        word += letter
    elif letter == "v":
        word += letter
    elif letter == "w":
        word += letter
    elif letter == "x":
        word += letter
    elif letter == "y":
        word += letter
    elif letter == "z":
        word += letter
    elif letter == "A":
        word += letter
    elif letter == "B":
        word += letter
    elif letter == "C":
        word += letter
    elif letter == "D":
        word += letter
    elif letter == "E":
        word += letter
    elif letter == "F":
        word += letter
    elif letter == "G":
        word += letter
    elif letter == "H":
        word += letter
    elif letter == "I":
        word += letter
    elif letter == "J":
        word += letter
    elif letter == "K":
        word += letter
    elif letter == "L":
        word += letter
    elif letter == "M":
        word += letter
    elif letter == "N":
        word += letter
    elif letter == "O":
        word += letter
    elif letter == "P":
        word += letter
    elif letter == "Q":
        word += letter
    elif letter == "R":
        word += letter
    elif letter == "S":
        word += letter
    elif letter == "T":
        word += letter
    elif letter == "U":
        word += letter
    elif letter == "V":
        word += letter
    elif letter == "W":
        word += letter
    elif letter == "X":
        word += letter
    elif letter == "Y":
        word += letter
    elif letter == "Z":
        word += letter

    if c_has_occurred and o_has_occurred and n_has_occurred:
        print(word)
        break

    input_line = input()