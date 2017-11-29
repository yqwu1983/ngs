#!/usr/bin/python

from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('B5ZC00') #you can give several IDs separated by commas
record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins

print dir(record)