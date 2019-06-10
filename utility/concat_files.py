"""
Use this script to concatenate files, given a directory.
"""

import sys
import glob
import os
import time


def concat(input_dir):
    os.chdir(input_dir)
    filenames = glob.glob("*.txt")

    out_file_path = "concat.txt"
    start_time = time.time()
    with open(out_file_path, 'a', encoding="utf-8") as outfile:
        for fname in filenames:
            file_start_time = time.time()
            print("Start processing {0}".format(fname))
            with open(fname, "r", encoding="utf-8") as infile:
                for line in infile:
                    outfile.write(line)

            file_sec_elapsed = time.time() - file_start_time
            print("Processing {0} done in {1:.2f} seconds".format(fname, file_sec_elapsed))

    sec_elapsed = time.time() - start_time
    print("Done concatenating all files into {0} in {1:.2f} seconds".format(out_file_path, sec_elapsed))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python concat_files.py <input directory>')
        sys.exit(1)

    in_dir = sys.argv[1]

    concat(in_dir)

