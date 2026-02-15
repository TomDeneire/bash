# New machine (Ubuntu-like, e.g. Mint)

## Install Linux

- see https://www.dell.com/support/kbdoc/nl-be/000131253/how-to-install-ubuntu-and-windows-8-or-10-as-a-dual-boot-on-your-dell-pc

## Install Dropbox

- https://www.dropbox.com/install-linux
- sync to /home/tdeneire/Dropbox

## Install terminal

- Install wezterm

```bash
curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg
echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
sudo apt update
sudo apt install wezterm
```

- ln -s /home/tdeneire/Dropbox/dotfiles/wezterm/.wezterm.lua /home/tdeneire/.wezterm.lua

## Set up directory structure

- mkdir /home/tdeneire/projects && cd /home/tdeneire/projects
- ln -s /home/tdeneire/Dropbox/code .
- ln -s /home/tdeneire/Dropbox/websites .

- cd /home/tdeneire
- ln -s /home/tdeneire/Dropbox/Documents
- ln -s /home/tdeneire/projects/code/go

## Git

- sudo apt install git
- ln -s /home/tdeneire/Dropbox/dotfiles/git/.gitconfig /home/tdeneire/.gitconfig

## Install terminal environment

- ln -s /home/tdeneire/Dropbox/dotfiles/bash/.bashrc /home/tdeneire/.bashrc
- ln -s /home/tdeneire/Dropbox/dotfiles/bash/.bash-preexec.sh /home/tdeneire/.bash-preexec.sh
- sudo apt install lsd
- ln -s /home/tdeneire/Dropbox/dotfiles/lsd /home/tdeneneire/.config/lsd
- sudo apt install tmux
- ln -s /home/tdeneire/Dropbox/dotfiles/tmux/.tmux.conf /home/tdeneneire/.tmux.conf
- ln -s /home/tdeneire/Dropbox/code/go/sesh/sesh /home/tdeneire/bin/sesh
- ln -s /home/tdeneire/Dropbox/code/go/fzf/fzf /home/tdeneire/bin/fzf
- ln -s /home/tdeneire/Dropbox/code/bash/t /home/tdeneire/bin/t

- sudo apt install batcat
- sudo apt install meld
- sudo apt install fzf-tmux
- sudo apt install zoxide
- sudo apt install fd-find
- sudo apt install ripgrep
- sudo apt install xsel
- sudo apt install jq
- sudo apt install gcc
- sudo apt install tree
- sudo apt install build-essential -y

## Install neovim

- node/npm/npx (for LSPs) -> get prebuilt binaries and put on $PATH (ln -s xxx ~/bin/npm)
- npm install -g tree-sitter-cli
- nvim-update
- python3 -m pip install --upgrade neovim
- python3 -m pip3 install --upgrade pynvim
- ln -s /home/tdeneire/Dropbox/dotfiles/nvim /home/tdeneire/.config/nvim

## Install programming languages

- Python 3, including pip and virtualenv
- golang-update
- Rust

## Install tools

- lazygit-update
- ln -s /home/tdeneire/Dropbox/dotfiles/lazygit /home/tdeneire/.config/lazygit
- atuin-update
- ln -s /home/tdeneire/Dropbox/dotfiles/atuin /home/tdeneire/.config/atuin
- docker (check installation instructions)

## Install applications

- Google Chrome

## Sync from Dropbox (not in Git because passwords)

- ~/.gitcredentials
- ~/.ssh/

## Add startup script to startup via menu

## Add batman script to startup via menu
