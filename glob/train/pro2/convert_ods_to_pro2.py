import os
import sys

in_dir = sys.argv[1]
out_dir = sys.argv[2]
files = os.listdir(in_dir)

for file_name in files:
    if file_name.endswith('.txt'):
        with open(os.path.join(in_dir, file_name), 'r') as f1:
            with open(os.path.join(out_dir, file_name), 'w+') as f2:
                for line in f1.readlines():
                    toks = line.split()
                    toks = [toks[0]] + ['12', '13', '14', '15', '16', '17'] + toks[3:]
                    f2.write(' '.join(toks) + '\n')
        