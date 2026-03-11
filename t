#!/bin/bash
sesh connect "$(
    sesh list -tziH | fzf \
        --ansi --no-sort -e \
        --color='fg:white,pointer:yellow,hl+:yellow,bg+:black,hl:yellow,fg+:bright-white,border:black' \
)"
