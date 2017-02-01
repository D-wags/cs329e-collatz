#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# check_cache
# ------------


def check_cache(nbr, the_cache):
    """
    reads in cycle cache and current number (the_cache, nbr)
    and checks for number in cache, if present gets cycle 
    length for number 
    else runs collatz_compute and adds to cache
    return cycle length

    """
    if nbr not in the_cache:
        cycle = collatz_compute(nbr, the_cache)
        the_cache[nbr] = cycle
        return cycle
    else:
        cycle = the_cache[nbr]
        return cycle

# ---------------
# collatz_compute
# ---------------


def collatz_compute(n, the_cache):
    """
    reads in number n and dictionary the_cache
    if nbr is even divide by 2
    if odd multiply by 3 and add 1
    repeat until 1 and record number of iterations (cycles)
    use cache to store cycles
    return cycle length

    """
    assert n > 0
    cycle = 1
    while n > 1:
        if n in the_cache:
            cycle += the_cache[n] - 1
            return cycle
        elif (n % 2) == 0:
            n = (n // 2)
            cycle += 1
        else:
            n = ((3 * n) + 1) // 2
            cycle += 2
    assert n == 1
    assert cycle > 0
    return cycle

# ---------------
# collatz_eval
# ---------------


def collatz_eval(i, j, the_cache):
    """
    i the beginning of the range, inclusive
    j the end of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    if i > j:
        i, j = j, i

    max_cycles = 0
    for a in range(i, j + 1):
        current = check_cache(a, the_cache)
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
    the_cache = {}

    for s in r:

        i, j = collatz_read(s)
        v = collatz_eval(i, j, the_cache)
        collatz_print(w, i, j, v)
