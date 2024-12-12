# ~/.bashrc: executed by bash(1) for non-login shells.


### --- Tom's setup --- ###

# To enable GIT information on command prompt:
source /etc/bash_completion.d/git-prompt
# And also define PROMPT setup:
if [ "$USER" = "jg2641@belgrid.net" ]; then
    PS1='\[\e[1m\][\[\e[1;32m\]tom@\h\[\e[0m\]|\[\e[1;34m\]\w\[\e[0m\]\[\e[1m\]\[\033[00m\]\[\e[0;33m\]$(__git_ps1 " (git)-%s")\[\e[0m\]\[\e[1m\]] \[\e[0m\]'
else
    PS1='\[\e[1m\][\[\e[1;32m\]\u@\h\[\e[0m\]|\[\e[1;34m\]\w\[\e[0m\]\[\e[1m\]\[\033[00m\]\[\e[0;33m\]$(__git_ps1 " (git)-%s")\[\e[0m\]\[\e[1m\]] \[\e[0m\]'
fi
export PS1

# My 'ls' settings using coreutils-gls:
LS_COLORS=$LS_COLORS:'di=1;34:' ; export LS_COLORS
alias ls='ls -h --color=auto --group-directories-first'
export QUOTING_STYLE=literal

# To make path output more readable:
function path(){
    old=$IFS
    IFS=:
    printf ${PATH//:/$'\n'}
    IFS=$old
}

# Copy pwd to the clipboard:
alias cpwd='printf "%q\n" "$(pwd)" | pbcopy && echo "Current directory copied to clipboard:" $(pbpaste)'

# Quick aliases for git commands:
alias gs='git status'
alias gf='git fetch'
alias gfs='git fetch && git status'
alias gba='git branch -a'
