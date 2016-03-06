#!/usr/bin/python
import re
import argparse

punctuation_regex = r'[^\w\- ]' # https://github.com/jch/html-pipeline/blob/master/lib/html/pipeline/toc_filter.rb#L26

# setup arguments
parser = argparse.ArgumentParser(description='Auto-generate a linked TOC for a markdown doc')
parser.add_argument('filename', type=str, help='markdown file')
args = parser.parse_args()

# open the file
doc = file(args.filename,'rw')

# get lines with headings
taglist = []
for line in doc:
    if '#' in line:
        taglist.append(line)

# remove new lines, tags, and whitespaces
for tag in taglist:
    clean_tag = tag.replace('\n','').replace('#','').strip()
    level = tag.count('#') - 1

# omit h1 tags
    if level is 0:
        continue

# remove capitals and hypenate spaces
    link = clean_tag.lower().replace(' ', '-')

# remove punctuation
    link = re.sub(punctuation_regex, '', link)

    print '\t'*(level - 1) + '- [' + clean_tag + '](#'+ link + ')'
