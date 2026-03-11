#!/bin/bash
selected="$(sesh list -tziH | fzf \
  --ansi --no-sort -e \
  --color='fg:white,pointer:yellow,hl+:yellow,bg+:black,hl:yellow,fg+:bright-white,border:black'
)"
[ -n "$selected" ] && sesh connect "$selected"
