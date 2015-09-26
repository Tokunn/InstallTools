#####################################################################
#
#  Sample .zshrc file
#  initial setup file for only interactive zsh
#  This file is read after .zshenv file is read.
#
#####################################################################

###
# Set Shell variable
# WORDCHARS=$WORDCHARS:s,/,,
HISTSIZE=10000 HISTFILE=~/.zsh_history SAVEHIST=10000
setopt hist_ignore_dups
#PROMPT='%m{%n}%% '
PROMPT='%F{green}%n%f@%F{cyan}%m%f %F{blue}%*%f %F{yellow}[%~]%f $ '
#RPROMPT='%F{yellow}[%~]%f'

# Set shell options
setopt hist_verify
setopt auto_cd auto_remove_slash auto_name_dirs 
setopt extended_history hist_ignore_dups hist_ignore_space prompt_subst
setopt extended_glob list_types no_beep always_last_prompt
setopt cdable_vars sh_word_split auto_param_keys pushd_ignore_dups
#setopt auto_menu  correct rm_star_silent sun_keyboard_hack
setopt auto_menu
#setopt CORRECTALL
setopt share_history inc_append_history
setopt correct

# Alias and functions
alias copy='cp -ip' del='rm -i' move='mv -i'
alias fullreset='echo "\ec\ec"'
h () 		{history $* | less}
alias ja='LANG=ja_JP.eucJP XMODIFIERS=@im=kinput2'
alias ls='ls -F --color' la='ls -a' ll='ls -la'
mdcd ()		{mkdir -p "$@" && cd "$*[-1]"}
mdpu ()		{mkdir -p "$@" && pushd "$*[-1]"}
alias pu=pushd po=popd dirs='dirs -v'
alias grep="grep --color=auto"

# Suffix aliases
alias -s pdf=acroread dvi=xdvi 
alias -s {odt,ods,odp,doc,xls,ppt}=soffice
alias -s {tgz,lzh,zip,arc}=file-roller


# binding keys
bindkey -e
#bindkey '^p'	history-beginning-search-backward
#bindkey '^n'	history-beginning-search-forward

zstyle ':completion:*' format '%BCompleting %d%b'
zstyle ':completion:*' group-name ''
zstyle ':completion:*:cd:*' tag-order local-directories path-directories
autoload -U compinit && compinit

#indigo()
#{
    #cd /opt/ros/indigo/
    source /opt/ros/indigo/setup.zsh
    export PYTHONPATH=/opt/ros/indigo/lib/python2.7/site-packages:/usr/lib/python3.4/site-packages/
    export PKG_CONFIG_PATH="/opt/ros/indigo/lib/pkgconfig"
    export PYTHONPATH=/opt/ros/indigo/lib/python2.7/site-packages
    source /home/tokunn/catkin_ws/devel/setup.zsh
    #cd ~/
#}

#androidconf()
#{
    export PATH="$PATH:/home/tokunn/Program/android-studio/bin"
#}

multiple()
{
    export ROS_MASTER_URI=http://172.16.14.224:11311
    export ROS_IP=172.16.14.114
}
