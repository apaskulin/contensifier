# contensifier
auto-TOC for markdown docs

### instructions
1. Download contensifier
2. Save your markdown file
3. Open a terminal and contensify!
  - `$ python [filepath/contensifier.py] [filepath/yourdocument.md]`
  - ex: `$ python Repositories/contensifier/contensifier.py Desktop/README.md`

### bonus points
Create a symbolic link in your PATH and contensify anywhere, anytime.

1. Create the link
  - `$ ln -s [filepath/contensifier.py] /usr/local/bin/contensify`
  - ex: `$ ln -s ~/Repositories/contensifier/contensifier.py /usr/local/bin/contensify`
2. Restart your terminal
3. `$ contensify [filepath/yourdocument.md]`
