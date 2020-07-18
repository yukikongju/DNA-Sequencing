#!/usr/bin/python

def reverse_complement(s):
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



