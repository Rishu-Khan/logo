#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import time
import sys

os.system('apt update')
os.system('apt upgrade -y')
os.system('pkg install figlet -y')
os.system('pkg install ncurses-utils -y') 
os.system('pkg install ruby -y')
os.system('gem install lolcat')

import os,sys,time,random
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.06)
'''.format(name)
h1 = open(output+'wlc.py', 'w')
h1.write(wlc)
h1.close()
clear
echo "
   < ━━━━━━━━━ [★] T E R M U X [★] ━━━━━━━━━━━━ >  "
echo
    echo "  █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█"
    echo "  █  \033[1;92m########..####..######..##.....##.##.....##  \033[1;91m█"
    echo "  █  \033[1;92m##.....##..##..##....##.##.....##.##.....##  \033[1;91m█"
    echo "  █  \033[1;92m##.....##..##..##.......##.....##.##.....##  \033[1;91m█"
    echo "  █  \033[1;92m########...##...######..#########.##.....##  \033[1;91m█"
    echo "  █  \033[1;92m##...##....##........##.##.....##.##.....##  \033[1;91m█"
    echo "  █  \033[1;92m##....##...##..##....##.##.....##.##.....##  \033[1;91m█"
    echo "  █  \033[1;92m##.....##.####..######..##.....##..#######.  \033[1;91m█"
    echo "  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█"
echo "
   < ━━━━━━━━━━━ [★]RISHU×KHAN[★] ━━━━━━━━━━━━ > "
'''
bashrc2 = '''
python /data/data/com.termux/files/usr/etc/wlc.py
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
#PS1="\\033[1;31mTHBD~#"
PS1="\[\e[1;31m┌──\\a─TIME─\\a──┐\\033[1;31m\\a┌──\\a─DATE─\\a───>\\033[1;31m
\\a┌─[\\033[1;92m \@\\033[1;32m ]──[\\033[1;92m \d\\033[1;32m ]\\033[1;32m
\\a├─[\\033[1;32m\w\\033[1;32m]\\033[1;32m
'''

h2 = open(output+'bash.bashrc', 'w')
h2.write(bashrc1)
h2.write("\nfiglet    '    "+name+"' |lolcat\n")
h2.write(bashrc2)
h2.write('\[\e[32m\]└─>\[\e[36m\]'+name+'\[\e[36m\]RISHU─>\[\e[1;32m\] "\n')
h2.write('echo -e "\e[6 q"')
h2.close()
print('DONE')
