#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os

def play(data):
    if len(data[5:]) == 0:
        print(Fore.BLUE + "Song name doesn't exist. (music '"'song name'"') " + Fore.RESET)

    else:
        wanted = data[6:]
        find = os.popen("ls | grep -i " +'"'+ wanted +'"')
        music = str(find.readline())

        if not music:
            os.system("instantmusic -s " + wanted)
            find = os.popen("ls -tc --hide='__*' --hide='*.py'")
            music = str(find.readline()).replace("\n", "")
            os.system("XDG_CURRENT_DESKTOP= DESKTOP_SESSION= xdg-open " + music.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)"))

        else:
            os.system("XDG_CURRENT_DESKTOP= DESKTOP_SESSION= xdg-open " + music.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)"))

play('aurora')
