#!/bin/bash

# .bashrc


# Source global definitions

if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi


# User specific aliases and functions

if [ -f $HOME/.aliases ]; then
	. $HOME/.aliases
fi

if [ -f $HOME/git-completion.bash ]; then
    . $HOME/git-completion.bash
fi

# Enable pattern recognition bash history search
# Allows the user to use the up arrow keys to auto-complete
# commands that match the pattern thus far.                                                    
#if [ $TERM!=screen ]; then
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'
#fi

export CLICOLOR=1
export LS_COLORS="di=1;34:ln=4;32:so=1;31:pi=1;33:ex=1;95:bd=34;46:cd=34;43:su=30;41:sg=30;46:tw=30;42:ow=30;43:*.pdf=00;33:*.gz=00;31:*.root=00;35"


export GREP_COLORS="ms=01;35:mc=01;35:sl=:cx=:fn=01;34:ln=33:bn=32:se=36"
alias grep="`which grep` --color=auto -n"

export PS1="\[\e[30m\][\[\e[m\]\[\[\e[32m\]\h:\[\e[m\]\[\e[35m\]\W\[\e[m\]\[\e[30m\]]\[\e[m\]\[\e[30m\]\\$\[\e[m\] "

export PATH=~/.local/bin/:$PATH


