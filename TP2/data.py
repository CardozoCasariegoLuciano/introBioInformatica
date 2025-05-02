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
