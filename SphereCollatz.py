#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

# -------
# imports
# -------

import sys

def makeCache(i, j):
    if i > j:
        i,j = j,i
    masterList = []

    x = i

    while x <= j:
        span = []
        span.append(x)
        x += 1000
        if x > j:
            x = j
        span.append(x)
    masterList.append(span)
    return (masterList)






def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_compute(n):
    assert isinstance(n, int)
    assert n > 0
    cycle = 1
    while n > 1:
        if (n%2) == 0:
            n = (n / 2)
        else:
            n = (3 * n) + 1
        cycle += 1
    assert n == 1
    assert cycle > 0
    return cycle


def collatz_eval(twodlist):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>

    # for p in range(i, j):
    #     if


    # assert j > i
    # if i > j:
    #     i,j = j,i

    for slist in twodlist:
        i = slist[0]
        j = slist[1]
        max_cycles = 0
        for a in range(i, j + 1):
            current = collatz_compute(a)
            if current > max_cycles:
                max_cycles = current
        return max_cycles

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)



# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)

""" #pragma: no cover
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""
