import re
import argparse

# arguments setup
parser = argparse.ArgumentParser(description='Auto-generate a linked TOC for a markdown doc')
parser.add_argument('filename', type=str, help='markdown file')
args = parser.parse_args()

# open the file
doc = file(args.filename,'rw')

# get tags
taglist = []
for line in doc:
    if '#' in line:
        taglist.append(line)

# format the tags
for tag in taglist:
    clean_tag = tag.replace('\n','').replace('#','').strip()
    level = tag.count('#') - 1

    if level is 0:
        continue

    if clean_tag.lower() in 'terminology':
        level = 0

    # remove capitals and hypenate spaces
    link = clean_tag.lower().replace(' ', '-')
    # remove periods, colons, parentheses, and apostrophes
    link = link.replace('.', '')
    link = link.replace(':', '')
    link = link.replace('(', '')
    link = link.replace(')', '')
    link = link.replace("'", '')

    print '\t'*(level - 1) + '- [' + clean_tag + '](#'+ link + ')'

# update Table Of Contents
