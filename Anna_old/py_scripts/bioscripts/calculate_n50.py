#!/usr/bin/python
import sys
import os

sequence, lengths = [], []
with open(sys.argv[1]) as handle:
  for line in handle:
    if line.startswith('>'):
      lengths.append(len(''.join(sequence)))
      sequence = []
    else:
      sequence += line.strip()


n50 = sorted(lengths)[len(lengths)/2] # approximately?
