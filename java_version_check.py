#!/usr/bin/python3

import subprocess

def checkJava():
    cmd = subprocess.run('java -version', stdout=subprocess.PIPE, shell=True)
    print(cmd.stdout.decode())

checkJava()