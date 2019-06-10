# Wiki-scraper
Create a corpus by downloading all wikipedia pages for a given language. The python library 'Wikipedia API' is used to extract the information for each wiki-page by usage of function `wikipediaapi.Wikipedia(language).page(title).text`.

## Requirements
1. [Wikipedia API](https://github.com/martin-majlis/Wikipedia-API)

## Instructions
1. For Dutch corpus: download `nlwiki-latest-all-titles-in-ns0.gz` from https://dumps.wikimedia.org/nlwiki/latest/ (replace 'nlwiki' according to preferred language).
2. Run `build_wiki_corpus_by_all_titles.py --titles <file> --output_dir <directory>`

Optional arguments:
* `--language` to initialize the Wikipedia API with (default='nl'). Make sure this is the same language as from where the file is downloaded in step 1. 
* `--eop_token` token appended at the end of each page (default='<|endofpage|>').
* `--sleep` amount of time in seconds to sleep between each request to Wikipedia API (default=0.05).
* `--include_page_title` to indicate whether the page title should be included (default=True).

This script produces another file named 'counter.txt' in which it keeps track of the pages it processed. 

## Split titles into separate files
To distribute the download process of wiki-pages across multiple devices, you can use `split_titles.py`. For example, if you want each file to hold 500000 titles, run the script as follows: 

`split_titles.py <*.gz-file> <outputdir> 500000`
