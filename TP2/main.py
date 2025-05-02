import sys
import generators
import data
import printers
from colorama import Fore, init
init()

#TODO: Agregar un puntaje/vidas
#TODO Agregar un contexto biologico
#TODO que no se pueda seleccionar un nucleotido ya seleccionado

#TODO agregar comentarios a las variables y metodos
hp = 3
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

        print("vida restante", hp)
        if(hp <= 0):
            print("Game over")
            sys.exit(1)
        if(len(codons_finded) >= 4):
            print("Ganaste!!")
            sys.exit(1)

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
        printers.print_help()
    elif (option.isdigit() and int(option) > 0 and int(option) <= data.BOARD_SIZE):
        selected_coords[cord] = int(option)
        if(selected_coords.get("X") and selected_coords.get("Y")):
            process_coord()
    else:
        print(Fore.RED + "No es una coordenada valida" + Fore.RESET + "\n")

def process_coord():
    x = int(selected_coords["X"]) - 1
    y = int(selected_coords["Y"]) - 1

    selected_letter = board_letters[x][y]
    codons_selections.append(selected_letter)
    board_letters[x][y]["formated_letter"] = f"{Fore.YELLOW}{selected_letter["letter"]}{Fore.RESET}"

    printers.clean_view()
    printers.print_mision(objetives)
    printers.print_board(board_letters)
    print(Fore.GREEN + "Como se juega? presiona '??'" + Fore.RESET + "\n")


    if(len(codons_selections) >= 3):
        is_correct_codon()
        codons_selections.clear()
    selected_coords.clear()

def is_correct_codon():
    global hp, objetives
    is_correct = False
    selection = ""
    for a in codons_selections:
        selection += "".join(a["letter"]).replace(" ", "")

    for obj in objetives:
        codon_list: list[str] = data.CODON_TABLE[obj].get("codons", [])
        for codon in codon_list:
            if(codon == selection):
                is_correct = True
                print(Fore.CYAN + "LO ENCONTRASTE!!" + Fore.RESET + "\n")
                codons_finded.append(selection)
                objetives = []
                objetives = generators.create_objetives(1)
                printers.change_color(board_letters, codons_selections, "GREEN")
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
        printers.change_color(board_letters, codons_selections, "RED")
        printers.print_continue_view(objetives, board_letters)



printers.clean_view()
print(Fore.GREEN + "Como se juega? presiona '??'" + Fore.RESET + "\n")
objetives = generators.create_objetives(1)
board_letters = generators.generate_board_letters()
printers.print_mision(objetives)
printers.print_board(board_letters)

main()
