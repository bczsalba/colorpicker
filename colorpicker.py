#!/usr/bin/env python3
import random
import getkey
import sys
import os
import re

os.system('clear')

tWidth,tHeight = os.get_terminal_size()

def printRGB(rgb):
    r,g,b = rgb
    for x in range(tWidth//2-25,tWidth//2+25):
        for y in range(tHeight//2-12,tHeight//2+12):
           sys.stdout.write(f'\033[{y-10};{x}H\033[38;2;{r};{g};{b}m█')

    sys.stdout.flush()
    print('\033[0m')

def center(string):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    _len = len(ansi_escape.sub('', string))
    return ((tWidth-_len)//2)*' '+string

def getMaxPad(array,offset=0):
    maxLen = None
    for a in array:
        if not maxLen or len(a) > maxLen:
            maxLen = len(a)
    return (tWidth-(maxLen+offset))//2*' '

rgb = [random.randint(1,255) for _ in range(3)]
rows = ['red','green','blue']
selection = 0
keys = getkey.keys

while 1:
    printRGB(rgb)
    print('\n')
    
    # print rows
    padding = getMaxPad(rows,2)
    midPad = max(len(l) for l in rows)*' '
    for i,row in enumerate(rows):
        colVal = rgb[i]

        # for rgb ansi escape codes
        col = '\033[38;2'
        for index in range(3):
            if i == index:
                col += f';{colVal}'
            else:
                col += ';0'
        col += f'm{colVal}'
            
        hi = ('\033[30;47m' if selection == i else '')
        print('\033[K'+padding+hi+row+': '+midPad[len(row)-2:]+col+'\033[0m')

    # print hex
    hexVal = "".join([format(val, '02X') for val in rgb])
    color = ''.join([';'+str(v) for v in rgb])+'m'
    print(padding+'hex: #'+'\033[38;2'+color+hexVal)
    print('\033[0m')
    
    # get, handle input
    key = getkey.getkey()

    # down
    if key in ['j',keys.DOWN]:
        selection = min(selection+1,len(rows)-1)

    # up
    elif key in ['k',keys.UP]:
        selection = max(selection-1,0)

    # right
    elif key in ['l',keys.RIGHT]:
        rgb[selection] = min(255,rgb[selection]+1)

    # left
    elif key in ['h',keys.LEFT]:
        rgb[selection] = max(0,rgb[selection]-1)
