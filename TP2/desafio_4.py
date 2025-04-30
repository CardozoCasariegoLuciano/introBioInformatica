from colorama import Fore, init
import sys
import random
init()

OPTIONS_LETTERS = [" U ", " C ", " A ", " G "]
BOARD_SIZE = 10
OBJETIVES_QUANT = 1
CODON_TABLE = {
    'A': {
        'name': 'Alanine',
        'abbrev': 'Ala',
        'codons': ['GCU', 'GCC', 'GCA', 'GCG']
    },
    'C': {
        'name': 'Cysteine',
        'abbrev': 'Cys',
        'codons': ['UGU', 'UGC']
    },
    'D': {
        'name': 'Aspartic acid',
        'abbrev': 'Asp',
        'codons': ['GAU', 'GAC']
    },
    'E': {
        'name': 'Glutamic acid',
        'abbrev': 'Glu',
        'codons': ['GAA', 'GAG']
    },
    'F': {
        'name': 'Phenylalanine',
        'abbrev': 'Phe',
        'codons': ['UUU', 'UUC']
    },
    'G': {
        'name': 'Glycine',
        'abbrev': 'Gly',
        'codons': ['GGU', 'GGC', 'GGA', 'GGG']
    },
    'H': {
        'name': 'Histidine',
        'abbrev': 'His',
        'codons': ['CAU', 'CAC']
    },
    'I': {
        'name': 'Isoleucine',
        'abbrev': 'Ile',
        'codons': ['AUU', 'AUC', 'AUA']
    },
    'K': {
        'name': 'Lysine',
        'abbrev': 'Lys',
        'codons': ['AAA', 'AAG']
    },
    'L': {
        'name': 'Leucine',
        'abbrev': 'Leu',
        'codons': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']
    },
    'M': {
        'name': 'Methionine',
        'abbrev': 'Met',
        'codons': ['AUG'],
    },
    'N': {
        'name': 'Asparagine',
        'abbrev': 'Asn',
        'codons': ['AAU', 'AAC']
    },
    'P': {
        'name': 'Proline',
        'abbrev': 'Pro',
        'codons': ['CCU', 'CCC', 'CCA', 'CCG']
    },
    'Q': {
        'name': 'Glutamine',
        'abbrev': 'Gln',
        'codons': ['CAA', 'CAG']
    },
    'R': {
        'name': 'Arginine',
        'abbrev': 'Arg',
        'codons': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
    },
    'S': {
        'name': 'Serine',
        'abbrev': 'Ser',
        'codons': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']
    },
    'T': {
        'name': 'Threonine',
        'abbrev': 'Thr',
        'codons': ['ACU', 'ACC', 'ACA', 'ACG']
    },
    'V': {
        'name': 'Valine',
        'abbrev': 'Val',
        'codons': ['GUU', 'GUC', 'GUA', 'GUG']
    },
    'W': {
        'name': 'Tryptophan',
        'abbrev': 'Trp',
        'codons': ['UGG']
    },
    'Y': {
        'name': 'Tyrosine',
        'abbrev': 'Tyr',
        'codons': ['UAU', 'UAC']
    },
    'STOP': {
        'name': 'Stop',
        'abbrev': 'Stop',
        'codons': ['UAA', 'UAG', 'UGA'],
    }
}

codons_finded = []
board_letters = []
codons_selections = []
objetives: list[str] = []
selected_coords = {
    "X" : 0,
    "Y" : 0,
}

def main():
    while True:
        try:
            if selected_coords.get("X"):
                porcess_input("Y")
            else:
                porcess_input("X")
            print("\n")
        except:
            sys.exit(1)

def porcess_input(cord):
    option = input("Selecciona una coordenada " + cord +  ":\n")

    if (option == "??"):
        print_help()
    elif (option.isdigit() and int(option) > 0 and int(option) <= BOARD_SIZE):
        selected_coords[cord] = int(option)
        if(selected_coords.get("X") and selected_coords.get("Y")):
            process_coord()
    else:
        print(Fore.RED + "No es una coordenada valida" + Fore.RESET + "\n")

def print_help():
    clean_view()
    print("Primero seleccioná una coordenada X de la tabla")
    print("Luego seleccioná una coordenada Y de la tabla")
    print("\nTenes que encontrar los nucleotidos para formar el aminoacido objetivo")

    input("\n" + "Toca una tecla para continuar" + "\n")


def process_coord():
    print("Coords", selected_coords)
    x = int(selected_coords["X"]) - 1
    y = int(selected_coords["Y"]) - 1

    selected_letter = board_letters[x][y]

    codons_selections.append(selected_letter)
    board_letters[x][y] = Fore.YELLOW + selected_letter + Fore.RESET


    clean_view()
    print_mision()
    create_board(BOARD_SIZE)
    print(Fore.GREEN + "Como se juega? presiona '??'" + Fore.RESET + "\n")


    if(len(codons_selections) >= 3):
        is_correct_codon()
    selected_coords.clear()


def is_correct_codon():
    selection = "".join(codons_selections).replace(" ", "")
    is_correct = False

    for a in objetives:
        lista: list[str] = CODON_TABLE[a].get("codons", []) if CODON_TABLE[a].get("codons") is not None else []
        for b in lista:
            if(b == selection):
                is_correct = True
                print(Fore.CYAN + "LO ENCONTRASTE!!" + Fore.RESET + "\n")

    if not is_correct:
        print(Fore.RED + "Perdiste!! No estamos buscando eso :C" + Fore.RESET + "\n")
        print("Estamos buscando alguna de estas:" +Fore.CYAN )
        for a in objetives:
            for key in CODON_TABLE[a].keys():
                print("\t\t" + key + ": "+  str(CODON_TABLE[a].get(key)))

        print(Fore.RESET)
        sys.exit(1)


def create_board(size):
    print("   " + " ".join(f"{i:2}" for i in range(1, size + 1)))
    print("  +" + "---" * size + "+")

    for y in range(1, size + 1):
        print(f"{y:2}|", end="")
        for x in range(1, size + 1):
            print(board_letters[x-1][y-1], end="")
        print(" |")
    print("  +" + "---" * size + "+")

def generate_board_letters(size):
    for _ in range(1, size + 1):
        tmp = []
        for _ in range(1, size + 1):
            tmp.append(random.choice(OPTIONS_LETTERS))
        board_letters.append(tmp)


def clean_view():
    for _ in range(0, 40):
        print("\n\n")


def print_mision():
    print(Fore.GREEN + "Objetivo: formar el siguientes aminoacido" + Fore.RESET)
    for op in objetives:
        print("\t\t\t\t\t" + Fore.YELLOW + str(CODON_TABLE[op].get("name"))+ Fore.RESET)

def create_objetives(quantity=3):
    for _ in range(0,quantity):
        select_NO_repeated(objetives)

def select_NO_repeated(arr):
        selected = random.choice(list(CODON_TABLE.keys()))
        if selected in arr:
            select_NO_repeated(arr)
        else:
            arr.append(selected)

clean_view()
print(Fore.GREEN + "Como se juega? presiona '??'" + Fore.RESET + "\n")
create_objetives(OBJETIVES_QUANT)
generate_board_letters(BOARD_SIZE)
print_mision()
create_board(BOARD_SIZE)

main()
