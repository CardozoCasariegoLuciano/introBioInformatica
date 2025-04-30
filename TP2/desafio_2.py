import sys

# Diccionario del código genético (aminoácido -> codones más comunes)
codon_table = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'C': ['UGU', 'UGC'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'F': ['UUU', 'UUC'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'K': ['AAA', 'AAG'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'M': ['AUG'],
    'N': ['AAU', 'AAC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    '*': ['UAA', 'UAG', 'UGA'],  # Codones de terminación
}

def protein_to_rna(protein_sequence):
    """Convierte una secuencia proteica en ARN codificante"""
    rna_sequence = []
    for aa in protein_sequence:
        aa = aa.upper()
        if aa in codon_table:
            # Tomamos el primer codón de la lista para simplificar
            rna_sequence.append(codon_table[aa][0])
        else:
            raise ValueError(f"Aminoácido no válido: {aa}")
    return ''.join(rna_sequence)

def main():
    if len(sys.argv) != 2:
        print("Uso: python desafio_2.py <secuencia_proteica>")
        print("Ejemplo: python desafio_2.py 'ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'")
        sys.exit(1)

    protein_seq = sys.argv[1]
    try:
        rna_seq = protein_to_rna(protein_seq)
        print(f"ARN codificante: {rna_seq}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
