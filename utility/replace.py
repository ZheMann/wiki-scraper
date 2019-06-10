import sys


def replace(f_in, f_out, original_char, new_char):
    r = open(f_in, "r", encoding="utf-8").read()
    r = r.replace(original_char, new_char)

    with open(f_out, "w", encoding="utf-8") as w:
        w.write(r)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Replace char with new char.\nUsage: python replace.py <input file> <output file> <character to replace '
              '(for new line use \'newline\')> <new character (for new line use \'newline\')>')
        sys.exit(1)

    f_in = sys.argv[1]
    f_out = sys.argv[2]
    replace_char = sys.argv[3]
    replace_with = sys.argv[4]

    if replace_char == "newline":
        replace_char = "\n"

    # f_in = "all_columns_endoftext.txt"
    # f_out = "hah.txt"
    # replace_char = "\n"
    # replace_with = "<|n|>"
    replace(f_in, f_out, replace_char, replace_with)
    print("Replacing {0} with {1} is done.".format(replace_char, replace_with))
