from itertools import product


def distinct_middle_clauses():
    alphabet = [0, 1]  # 0 >> Zelle hat keine Bombe | 1 => Zelle hat Bombe
    middle_clauses = []

    print("\nVariationen der Mittelzellen mit 8 moeglichen Nachbarzellen wenn aktuelle Zelle = 0")
    for x in product(alphabet, repeat=8):
        if x.count(1) == 0:
            print('zelle_x_y_0 -->', x)
            middle_clauses.append(x)

    print("\nVariationen der Mittelzellen mit 8 moeglichen Nachbarzellen wenn aktuelle Zelle = 1")
    for x in product(alphabet, repeat=8):
        if x.count(1) == 1:
            print('zelle_x_y_1 -->', x)
            middle_clauses.append(x)

    print("\nVariationen der Mittelzellen mit 8 moeglichen Nachbarzellen wenn aktuelle Zelle = 2")
    for x in product(alphabet, repeat=8):
        if x.count(1) == 2:
            print('zelle_x_y_2 -->', x)
            middle_clauses.append(x)

    print("\nVariationen der Mittelzellen mit 8 moeglichen Nachbarzellen wenn aktuelle Zelle = 3")
    for x in product(alphabet, repeat=8):
        if x.count(1) == 3:
            print('zelle_x_y_3 -->', x)
            middle_clauses.append(x)

    return middle_clauses