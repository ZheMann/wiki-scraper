import sys


def remove_short_sentences(f_in, min_nb_words):
    with open(f_in, "r") as f:
        lines = f.readlines()

    with open(f_in, "w") as f:
        for line in lines:
            if len(line.split()) >= min_nb_words:
                f.write(line)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python remove_short_sentences.py <input_file> <minimal number of words per sentence>')
        sys.exit(1)

    f_in = sys.argv[1]
    min_nb_words = int(sys.argv[2])

    remove_short_sentences(f_in, min_nb_words)
    print("Sentences containing less than {0} words removed.".format(str(min_nb_words)))
