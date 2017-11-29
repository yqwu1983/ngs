#!/usr/bin/python

import re
import sys
from ntpath import split

def file_from_path(path, folder=False):
    head, tail = split(path)
    if folder: return head
    else: return tail

f_name = sys.argv[1]
f = open(f_name, 'r')

f_out_name = f_name[0:-8] + '_filtered.vcf'

out = []
for line in f.readlines():
	if line[0] == '#':
		out.append(line)
	else:
		s_line = line.split('\t')
		alt = s_line[4].split(',')
		qual = s_line[5]
		info = s_line[7]
		match = re.match('.*DP4=((\d+),(\d+),(\d+),(\d+)).*', info)
		if match:
			a = float(match.group(2))
			b = float(match.group(3))
			c = float(match.group(4))
			d = float(match.group(5))
			if len(alt)<3 and (b + d) > 0 and (a + c) > 0 and float(qual) >= 10.0:
				fw_rv_ratio = (a + c)/(b + d)
				if fw_rv_ratio < 5 and fw_rv_ratio > 0.2:
					out.append(line)
f.close()

f_out = open(f_out_name, 'w')
for out_line in out:
	f_out.write(out_line)
f_out.close()