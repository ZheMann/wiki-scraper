"""
Creates a corpus by downloading all wikipedia pages for a given language.

For Dutch language: download 'nlwiki-latest-all-titles-in-ns0.gz' from
https://dumps.wikimedia.org/nlwiki/latest/

This file contains roughly 2.6M titles of wikipedia-pages.

If one prefers to split this file into separate files,
use split_all_titles_to_separate_files(). This could be helpful to distribute
downloading pages across several machines.
"""


import sys
import gzip
import wikipediaapi
import time
import os
import argparse

COUNTER_FILE = "counter.txt"

parser = argparse.ArgumentParser(
    description='Download wikipedia corpus',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--titles', type=str, required=True, help='Input file that contains wiki-titles')
parser.add_argument('--output_dir', type=str, required=True, help='Output directory')
parser.add_argument('--language', type=str, default="nl", help='Language Wikipedia')
parser.add_argument('--eop_token', type=str, default="<|endofpage|>", help='End of page token is appended to end of each page')
parser.add_argument('--sleep', type=float, default=0.05, help='Amount of time (in seconds) to wait between each request')
parser.add_argument('--include_page_title', type=bool, default=True, help='If set to True, also page title is written to file')


def get_next_start_index():
    idx = 0
    with open(COUNTER_FILE, "rt", encoding="utf-8") as f_in:
        for line in f_in:
            idx = line.split(' ')[0]

    # Return next index
    if idx == 0:
        return int(idx)
    else:
        return int(idx) + 1


def make_corpus():
    in_f = args.titles
    out_dir = args.output_dir
    language = args.language
    eop_token = args.eop_token
    sleep = args.sleep
    include_title = args.include_page_title

    try:
        os.mkdir(out_dir)
    except FileExistsError:
        pass

    if not out_dir.endswith('/'):
        out_dir = "{0}/".format(out_dir)

    # Init language specific wikipedia-api
    wiki = wikipediaapi.Wikipedia(language)

    # Number of retries in case of an exception
    # Todo: add to arguments
    max_retries = 3

    exists = os.path.isfile(COUNTER_FILE)
    start_idx = 0 if not exists else get_next_start_index()

    print("Starting from index: {0}".format(start_idx))

    count = 0
    out_file = "{0}wiki_pages.txt".format(out_dir)

    start_time = time.time()

    with gzip.open(in_f, "rt", encoding="utf-8") as f_in\
            , open(out_file, "a", encoding="utf-8") as f_out\
            , open(COUNTER_FILE, "a+", encoding="utf-8") as counter_out:
        for line in f_in:
            if start_idx > 0 and count < start_idx:
                count += 1
                continue

            attempts = 0
            wiki_title = ""
            wiki_text = ""
            while attempts < max_retries:
                attempts += 1

                try:
                    # Strip end-of-line token if present
                    if "\n" in line:
                        line = line.split("\n")[0]

                    page = wiki.page(line)
                    if page is not None and page.exists():
                        wiki_title = page.title
                        wiki_text = page.text

                    # Break out of while-loop
                    break
                except:
                    print("Oops! {0} occured for page {1}. Trying again in 5 seconds. Number of attempts: "
                          "{2}/{3}".format(sys.exc_info()[0], line, attempts, max_retries))
                    time.sleep(5)

            # If either is empty, something went wrong
            if not wiki_title or not wiki_text:
                print("Page with title {0} not found. Continuing with next page.".format(line))
                continue

            if include_title:
                f_out.write("{0}\n".format(wiki_title))
            f_out.write(wiki_text)
            f_out.write("\n{0}\n".format(eop_token))

            # Write page titles to separate file to keep track of processed pages
            counter_out.write("{0} {1}\n".format(count, wiki_title))

            # Write changes immediately to disk
            f_out.flush()
            counter_out.flush()

            # Print statement after processing 100 pages
            if (count - start_idx) % 100 == 0:
                time_elapsed = (time.time() - start_time) / 60
                print("Added {0} pages so far in {1:.2f} minutes".format(count - start_idx, time_elapsed))

            count += 1

            # Take a break of {value} seconds after 5000 pages.
            # Todo: add as argument
            if (count - start_idx) % 5000 == 0:
                sec = 10
                print("Processed 5000 pages, going to sleep now for {0} seconds.".format(sec))
                time.sleep(sec)
            else:
                # Sleep between requests to wikipedia's api
                time.sleep(sleep)


if __name__ == '__main__':
    args = parser.parse_args()
    make_corpus()
