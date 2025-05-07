from colorama import Fore, init
import data
init()


def intro():
    print("En el núcleo de cada célula, el ADN guarda las instrucciones para construir proteínas, esenciales para la vida. Este proceso ocurre en dos etapas clave: \n")
    print(Fore.GREEN + "Transcripcion" + Fore.RESET)
    print("Una secuencia de ADN (un gen) se copia en ARN mensajero (ARNm).")
    print("El ARNm lleva el 'mensaje genético' desde el núcleo hasta los ribosomas.")
    print("\n"+Fore.GREEN + "Transcripcion" + Fore.RESET)
    print("Los ribosomas 'leen' el ARNm en grupos de tres nucleótidos llamados codones.")
    print("Cada codón codifica un aminoácido específico (o una señal de parada).")
    print("Los aminoácidos se ensamblan en una cadena para formar una proteína funcional.")
    print("\n")
    print("En este juego, eres un ribosoma humano que debe decodificar codones en el tablero y evitar errores, Un fallo \nen la traducción puede producir proteínas defectuosas (¡como en la vida real!).")

    input("\n\nToca ENTER para continuar")
    clean_view()

def print_continue_view(objetives, board_letters):
    input("Toca ENTER para continuar")
    clean_view()
    print_mision(objetives)
    print_board(board_letters)
    print(Fore.GREEN + "Como se juega? presiona '??'" + Fore.RESET + "\n")

def print_board(board_letters):
    size = data.BOARD_SIZE

    print(Fore.CYAN + "  x" + Fore.RESET + " ".join(f"{i:2}" for i in range(1, size + 1)), "")
    print(Fore.CYAN +"y " + Fore.RESET + "+" + "---" * size + "+")

    for y in range(1, size + 1):
        print(f"{y:2}|", end="")
        for x in range(1, size + 1):
            print(board_letters[y-1][x-1].get("formated_letter", ""), end="")
        print(" |")
    print("  +" + "---" * size + "+")

def clean_view():
    for _ in range(0, 12):
        print("\n\n")

def print_mision(objetives):
    print(Fore.GREEN + "Objetivo: traducir el siguientes aminoacido" + Fore.RESET)
    for op in objetives:
        print("\t\t\t\t\t" + Fore.YELLOW + str(data.CODON_TABLE[op].get("name"))+ Fore.RESET)

def change_color(board_letters, list, color):
    if( color == "RED"):
        for item in list:
            x = item["coords"].get("y", "") -1
            y = item["coords"].get("x", "") -1
            board_letters[x][y]["formated_letter"] = f"{Fore.RED}{item["letter"]}{Fore.RESET}"
    else:
        for item in list:
            x = item["coords"].get("y", "") -1
            y = item["coords"].get("x", "") -1
            board_letters[x][y]["formated_letter"] = f"{Fore.GREEN}{item["letter"]}{Fore.RESET}"

def print_help(board_letters, objetives):
    clean_view()
    print("Primero seleccioná una coordenada X de la tabla")
    print("Luego seleccioná una coordenada Y de la tabla")
    print("\nTenes que encontrar los nucleotidos para formar el aminoacido objetivo")

    input("\n" + "Toca una tecla para continuar" + "\n")
    print_mision(objetives)
    print_board(board_letters)
