#!/usr/bin/python

__author__ = 'lebrunt'

import subprocess

IFile = open('/Users/lebrunt/Downloads/xferlog', "r")
OFile = open('/tmp/zanonymous.out', "w")

for Line in IFile:
    SLine = Line.split(' ')
    if SLine[13] == "a":
        OFile.write(Line)

OFile.flush()         # Not needed if file closed before sending email

OFile.close()
IFile.close()

# Send Email
subprocess.call(["mail -s 'Anonymous logins' tommy.lebrun@sealedair.com < /tmp/zanonymous.out"], shell=True)

