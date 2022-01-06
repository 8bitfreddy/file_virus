# -*- coding: utf-8 -*-
import os
import shutil
import hashlib


def clone():
    print('input count')
    f = open('k.txt')
    tmp_l = f.readline()
    if tmp_l.isdigit():
        tmp_l = int(tmp_l)
    else:
        exit(0)
    print(tmp_l)
    for i in range(tmp_l):
        shutil.copy2('C:/Users/Илья/PycharmProjects/virus/file.txt',
                     'C:/Users/Илья/PycharmProjects/virus/file{0}.txt'.format(i))


def cipher_file():
    file = open('file.txt', 'rb+')

a = int("1")
b = int("2")
print(bin(a))
print(bin(b))
print(bin(a ^ b))

# file = open('file.txt', 'w+')
# file.write('you have been hacked')
#
#
# file.close()
clone()
# cipher_file()











'''

file = open('file.txt')
for line in file:
    print(line)
'''




#print(os.path.dirname(__file__))

