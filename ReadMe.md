# Shell-cat

That simple utility creates two commands in your zsh or bash config :
- One that displays a random cat
- An other that git add ., git commit, and git push, with of course a random cat

## Installation

```sh
# In a folder where you have full writes
git clone https://github.com/t0mm4rx/shell-cat && cd shell-cat && python install.py && cd ../ && rm -rf shell-cat
```

Don't forget to source the shell you use, or open a new terminal:
```sh
source ~/.zshrc
```

## Problem ?

Something went wrong ? Just delete your .bashrc and .zshrc and rename .bashrc_backup to .bashrc and .zshrc_backup to .zshrc.
