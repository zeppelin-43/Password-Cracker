import os
import hashlib
import base64
import re
import argparse
import itertools


def leet(passwords):
    for pw in passwords:
        pw = pw.replace("o","0")
        pw = pw.replace("l","1")
        pw = pw.replace("e","3")
        pw = pw.replace("a","4")
        pw = pw.replace("s","5")
        passwordsAll.append(pw)


def symbol(passwords):
    for pw in passwords:
        for s in symbols:
            passwordsAll.append(pw+s)


def random(passwords):
    lsts = [symbols, symbols, symbols, symbols]
#    lsts.append(symbols)
    new = []
    new = list(map(lambda x: "".join(x), list(itertools.product(*lsts))))
    passwordsAll.extend(new)
    
parser = argparse.ArgumentParser('Crack some passwords')
parser.add_argument('-f', '--password-file', help="A file of hashed passwords", dest="passhashfile")
parser.add_argument('-o', '--output-file', help="The cracked passwords", dest="output")
args = parser.parse_args()

password_file = args.passhashfile
output = args.output

symbols = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1#$%&*?")
passwords = []
with open(password_file, "r") as f_in:
    for pw in f_in:
#        passwordList.append[pw]
        pw = pw.strip(" \r\n")
        passwords.append(pw)

passwordsAll = list(passwords)    

leet(passwords)
symbol(passwords)
random(passwords)
with open(output, "w") as f_out:
    for pw in passwordsAll:
#        passwordList.append[pw]
        f_out.write("%s\n" % pw)
#random(passwords)










       