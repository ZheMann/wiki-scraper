# Wiki-scraper
Create a corpus by downloading all wikipedia pages for a given language.

## Requirements
1. [Wikipedia API](https://github.com/martin-majlis/Wikipedia-API)

## Instructions to download (Dutch) wiki corpus
1. Download `nlwiki-latest-all-titles-in-ns0.gz` from https://dumps.wikimedia.org/nlwiki/latest/.
2. Execute `build_wiki_corpus_by_all_titles.py`

## Additional stuff
To distribute the download process of wiki-pages across multiple devices:  split titles into separate files to distribute processing across multiple devices: 'python split_titles.py titles/nlwiki-latest-all-titles-in-ns0.gz test 500000'
