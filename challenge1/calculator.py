#!/usr/bin/env python3
import sys

gz = int(sys.argv[1])
bx = 0
qz = 3500
sl = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
ssk = [0, 105, 555, 1005, 2755, 5505, 13505]
ynsd = gz - bx - qz
if gz <= 0:
    print('please enter a number greater than 0 ')
elif gz <= 3500:
    print("You dot't have to pay taxes")
else:
    if ynsd <= 1500:
        i = 0
        ns = ynsd * sl[i] - ssk[i]
    elif ynsd <= 4500:
        i = 1
        ns = ynsd * sl[i] - ssk[i]
    elif ynsd <= 9000:
        i = 2
        ns = ynsd * sl[i] - ssk[i]
    elif ynsd <= 35000:
        i = 3
        ns = ynsd * sl[i] - ssk[i]
    elif ynsd <= 55000:
        i = 4
        ns = ynsd * sl[i] - ssk[i]
    elif ynsd <= 80000:
        i = 5
        ns = ynsd * sl[i] - ssk[i]
    else:
        i = 6
        ns = ynsd * sl[i] - ssk[i]
    print("{:.2f}".format(ns))
