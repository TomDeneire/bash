#!/bin/bash
sesh connect "$(
    sesh list -tzi | fzf \
        --ansi --no-sort -e \
        --color='fg:white,pointer:yellow,hl+:yellow,bg+:black,hl:yellow,fg+:bright-white,border:black'
)"
