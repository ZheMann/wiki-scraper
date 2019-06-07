# Wiki-scraper
Create a corpus by downloading all wikipedia pages for a given language.

## Instructions
1. For Dutch language: download 'nlwiki-latest-all-titles-in-ns0.gz' from
https://dumps.wikimedia.org/nlwiki/latest/. This file contains roughly 2.6M titles of wikipedia-pages.

2. If necessary, split titles into separate files to distribute processing across multiple devices: 'python split_titles.py titles/nlwiki-latest-all-titles-in-ns0.gz test 500000'

3. 
