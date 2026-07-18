#!/usr/bin/env bash

if [ -z "$TMUX" ]; then
    exec tmux new-session -A -s scratch "$0"
fi

sesh connect $(sesh list -tzi | fzf-tmux \
        --ansi --no-bold -e -p 55%,60% \
        --color='fg:white,pointer:yellow,hl+:yellow,bg+:black,hl:yellow,fg+:bright-white,border:white' \
        --no-sort --border-label '   ' --prompt '  ' \
        --bind 'tab:down,btab:up')
