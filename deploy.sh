#!/usr/bin/git-shell
GIT_WORK_TREE=$HOME/discordion
GIT_DIR=$HOME/discordion/discordion.git
git checkout -f
source $HOME/discordion/venv/bin/activate
cd $HOME/discordion
nohup python $HOME/discordion/bot.py &