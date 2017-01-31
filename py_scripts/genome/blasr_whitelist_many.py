import sys

# NOTE: this script assumes a single movie in the blasr alignment

blacklist_alignment = sys.argv[1]
num_holes = int(sys.argv[2])

blacklist = set()
movie_prefix = None
for line in open(blacklist_alignment):
    if line.startswith('qname'):
        continue

    cols = line.split()

    alignment_id_parts = cols[0].split('/')
    if movie_prefix is None:
        movie_prefix = alignment_id_parts[0]

    hole_num = alignment_id_parts[1]

    blacklist.add(hole_num)

for i in range(num_holes):
    i = str(i)
    if i not in blacklist:
        print '/'.join([movie_prefix, i])
