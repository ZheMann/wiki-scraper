import sys


def remove_empty_lines(file_in):
    with open(file_in, "r") as f:
        lines = f.readlines()

    with open(f_in, "w") as f:
        for line in lines:
            if not line.isspace():
                f.write(line)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python remove_empty_lines.py <input file>')
        sys.exit(1)

    f_in = sys.argv[1]

    remove_empty_lines(f_in)
    print("Removing empty lines is done")
