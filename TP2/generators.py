import random
import data

def generate_board_letters():
    size = data.BOARD_SIZE
    board_letters = []
    for y in range(1, size + 1):
        tmp = []
        for x in range(1, size + 1):
            letter = random.choice(data.OPTIONS_LETTERS)
            field = {
                "letter": letter,
                "formated_letter": letter,
                "coords": {"x": x, "y": y}
            }
            tmp.append(field)
        board_letters.append(tmp)
    return board_letters

def create_objetives(quantity=3):
    objetives = []
    for _ in range(0,quantity):
        select_NO_repeated(objetives)
    return objetives

def select_NO_repeated(arr):
        selected = random.choice(list(data.CODON_TABLE.keys()))
        if selected in arr:
            select_NO_repeated(arr)
        else:
            arr.append(selected)
