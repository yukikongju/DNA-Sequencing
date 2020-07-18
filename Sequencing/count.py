#!usr/bin/python

def countBase(genome):
    counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for base in genome:
        counts[base] += 1
    return counts
