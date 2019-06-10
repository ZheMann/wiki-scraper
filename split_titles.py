import sys
import gzip
import numpy as np
import os

def split_all_titles_to_separate_files(in_f, out_dir, titles_per_file):
    if out_dir.endswith('/'):
        out_dir = out_dir.split('/')[0]

    try:
        os.mkdir(out_dir)
    except FileExistsError:
        pass

    out_dir = "{0}/".format(out_dir)

    count = 0
    with gzip.open(in_f, 'rt', encoding='utf-8') as fin:
        for line in fin:
            count += 1

    print("Nb of lines in file: {0}".format(count))
    nb_files = int(np.ceil(count / titles_per_file))
    print("Nb of files to generate: {0}".format(nb_files))

    idx = 0
    lines = gzip.open(in_f, 'rt', encoding='utf-8').readlines()
    for i in range(0, nb_files):
        end_idx = idx + titles_per_file if idx + titles_per_file < count else count
        file_name = "{0}all_titles_{1}_{2}.gz".format(out_dir, idx, end_idx)

        with gzip.open(file_name, 'wt', encoding='utf-8') as fout:
            for j in range(idx, end_idx):
                fout.write(lines[j])
                idx += 1

            #Write to drive immediately
            fout.flush()

        print("Created file {0}".format(file_name))


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python split_titles.py <input file> <output directory> <nb titles per file>')
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    nb_titles = int(sys.argv[3])

    split_all_titles_to_separate_files(input_file, output_dir, nb_titles)
