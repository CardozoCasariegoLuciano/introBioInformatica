import sys
import generators
import data
import printers
from colorama import Fore, init
init()

hp = 3
aa_finded = [] # Lista de Aminoacidos correctamente traducidos
all_codons_selected = [] # Lista de todos los codones seleccionados (para no repetirlos)
board_letters = [] # Lista de listas con todas las letras del tablero
nucleotid_selections = [] # Lista de  nucleotios seleccionados, al llegar a 3 se evalua si estan bien
objetives: list[str] = [] # Lista con los objetivos
selected_coords = { # Objeto con las ultimas coordenadas ingresadas por el usuario
    "x" : 0,
    "y" : 0,
}

def main():
    while True:

        print("vidas restante", hp)
        print("Aminoacidos pendientes: ", str(2 - len(aa_finded)), "\n")
        if(hp <= 0):
            print("Game over")
            sys.exit(1)
        if(len(aa_finded) >= 2):
            print("Ganaste!!")
            sys.exit(1)

        if selected_coords.get("x"):
            porcess_input("y")
        else:
            porcess_input("x")
        print("\n")

def porcess_input(cord):
    option = input("Selecciona una coordenada " + cord +  ":\n")

    if (option == "??"):
        printers.print_help(board_letters, objetives)
    elif (option.isdigit() and int(option) > 0 and int(option) <= data.BOARD_SIZE):
        selected_coords[cord] = int(option)
        if(selected_coords.get("x") and selected_coords.get("y")):
            process_coord()
    else:
        print(Fore.RED + "No es una coordenada valida" + Fore.RESET + "\n")

def process_coord():
    x = int(selected_coords["x"]) - 1
    y = int(selected_coords["y"]) - 1

    if(is_alredy_use()):
        print(Fore.RED + "YA seleccionaste ese nucleotido!" + Fore.RESET + "\n")
        printers.print_continue_view(objetives, board_letters)
        selected_coords.clear()
        return

    selected_letter = board_letters[y][x]
    all_codons_selected.append(selected_letter)
    nucleotid_selections.append(selected_letter)
    board_letters[y][x]["formated_letter"] = f"{Fore.YELLOW}{selected_letter["letter"]}{Fore.RESET}"

    printers.clean_view()
    printers.print_mision(objetives)
    printers.print_board(board_letters)
    print(Fore.GREEN + "Como se juega? presiona '??'" + Fore.RESET + "\n")

    if(len(nucleotid_selections) >= 3):
        process_codon()
        nucleotid_selections.clear()
    selected_coords.clear()

def is_alredy_use():
    for codon in all_codons_selected:
        if codon["coords"] == selected_coords:
            return True
    return False

def process_codon():
    global hp, objetives
    is_correct = False
    selection = ""
    for a in nucleotid_selections:
        selection += "".join(a["letter"]).replace(" ", "")


    for obj in objetives:
        codon_list: list[str] = data.CODON_TABLE[obj].get("codons", [])
        for codon in codon_list:
            if(codon == selection):
                is_correct = True
                print(Fore.CYAN + "LO ENCONTRASTE!!" + Fore.RESET + "\n")
                aa_finded.append(selection)
                objetives = []
                objetives = generators.create_objetives(1)
                printers.change_color(board_letters, nucleotid_selections, "GREEN")
                printers.print_continue_view(objetives, board_letters)

    if not is_correct:
        print(Fore.RED + "Perdiste una vida!! No estamos buscando eso" + Fore.RESET + "\n")
        print("Estamos buscando alguna de estas:" +Fore.CYAN )
        for obj in objetives:
            for key in data.CODON_TABLE[obj].keys():
                print("\t\t" + key + ": "+  str(data.CODON_TABLE[obj].get(key)))
        print(Fore.RESET)
        hp = hp-1
        objetives = []
        objetives = generators.create_objetives(1)
        printers.change_color(board_letters, nucleotid_selections, "RED")
        printers.print_continue_view(objetives, board_letters)


try:
    printers.clean_view()
    printers.intro()
    print(Fore.GREEN + "Como se juega? presiona '??'" + Fore.RESET + "\n")
    objetives = generators.create_objetives(1)
    board_letters = generators.generate_board_letters()
    printers.print_mision(objetives)
    printers.print_board(board_letters)

    main()
except:
    sys.exit(1)
