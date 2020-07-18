#!/usr/bin/python

import random

def generate_sequence(length):
    seq = ''
    for _ in range(length):
        seq += random.choice('ACGT')
    return seq



