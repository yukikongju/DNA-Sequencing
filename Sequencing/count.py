#!usr/bin/python

from collections import Counter

def countBase(genome):
    counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for base in genome:
        counts[base] += 1
    return counts

def getCodeCount(translation):
    code_seq = []
    for i in translation:
        code = aa_letter_to_code.get(i)
        code_seq.append(code)
    return Counter(code_seq)

def getHammingDistance(seq_1, seq_2):
    count = abs(len(seq_1) - len(seq_2))
    length = 0
    if (len(seq_1) < len(seq_2)):
        length = len(seq_1)
    else:
        length = len(seq_2)
    for i in range(length):
        if (seq_1[i] != seq_2[i]):
            count+=1
    return count
