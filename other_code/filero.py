#!/usr/bin/env python3
# coding : utf-8

filename = input('Enter the file name: ')

with open(filename) as file:
    count = 0
    for line in file:
        count += 1
        print(line)
    print('Lines: ', count)
