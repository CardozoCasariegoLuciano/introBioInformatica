#DESAFÍO V: Escribí un scrip en Python que prediga la estructura secundaria que adoptará cada residuo (aminoácido) de la secuencia proteica 
# dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).


from colorama import Fore, Style, init
init()

def predict_secondary_structure(sequence):
    aa_propensities = {
        'A': {'H': 1.45, 'B': 0.97}, 'C': {'H': 0.77, 'B': 1.30},
        'D': {'H': 0.98, 'B': 0.80}, 'E': {'H': 1.53, 'B': 0.26},
        'F': {'H': 1.12, 'B': 1.28}, 'G': {'H': 0.53, 'B': 0.81},
        'H': {'H': 1.24, 'B': 0.71}, 'I': {'H': 1.00, 'B': 1.60},
        'K': {'H': 1.07, 'B': 0.74}, 'L': {'H': 1.34, 'B': 1.22},
        'M': {'H': 1.20, 'B': 1.67}, 'N': {'H': 0.73, 'B': 0.65},
        'P': {'H': 0.59, 'B': 0.62}, 'Q': {'H': 1.17, 'B': 1.23},
        'R': {'H': 0.79, 'B': 0.90}, 'S': {'H': 0.79, 'B': 0.72},
        'T': {'H': 0.82, 'B': 1.20}, 'V': {'H': 1.14, 'B': 1.65},
        'W': {'H': 1.14, 'B': 1.19}, 'Y': {'H': 0.61, 'B': 1.29}
    }
    
    structure = []
    sequence_formated = sequence.upper()
    for aa in sequence_formated:
        if aa not in aa_propensities:
            structure.append('L')
            continue
        
        h_score = aa_propensities[aa]['H']
        b_score = aa_propensities[aa]['B']
        
        if h_score > 1.0 and h_score > b_score:
            structure.append('H')
        elif b_score > 1.0 and b_score > h_score:
            structure.append('B')
        else:
            structure.append('L')
    
    return ''.join(structure)


nombre = input("ingrese la cadena de aminoácidos: ")
print("Prediccion: ")
print(Fore.BLUE + predict_secondary_structure(nombre) + Style.RESET_ALL)