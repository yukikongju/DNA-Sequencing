#!/usr/bin/python

aa_letter_to_code = {
        'A': 'ala',
        'R': 'arg',
        'N': 'asn',
        'D': 'asp',
        'B': 'asx',
        'C': 'cys',
        'E': 'glu',
        'Q': 'gln',
        'Z': 'glx',
        'G': 'gly',
        'H': 'his',
        'I': 'ile',
        'L': 'leu',
        'K': 'lys',
        'M': 'met',
        'F': 'phe',
        'P': 'pro',
        'S': 'ser',
        'T': 'thr',
        'W': 'trp',
        'Y': 'tyr',
        'V': 'val'
        }

def getReverseComplement(s):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse = ''
    for base in s:
        reverse += complement[base]
    return reverse

def match(s1, s2):
    if not len(s1) == len(s2):
        return False
    for i in range(s1):
        if not s1[i] == s2[i]:
            return False
    return True

def getCodeTranslation(genome):
    code_seq = []
    for i in translation:
        code = aa_letter_to_code.get(i)
        code_seq.append(code)
    return '-'.join(code_seq)



