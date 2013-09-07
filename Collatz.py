#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

memorized_cycles = [0]*1000000

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    r is a  reader
    returns an generator that iterates over a sequence of lists of ints of length 2
    for s in r :
        l = s.split()
        b = int(l[0])
        e = int(l[1])
        yield [b, e]
    """
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval ((i, j)) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
	assert i > 0
    assert j > 0
    minRange = min(i, j)
    maxRange = max(i, j)
    v = 1
    for n in range(minRange, maxRange+1):
        v = max(v, collatz_solver(n))
	assert v > 0
    return v

def collatz_solver(n):
    if n == 1:
        return 1
    elif n < 1000000:
        if memorized_cycles[n]:
            return memorized_cycles[n]
        elif (n % 2): #odd
            memorized_cycles[n] = collatz_solver(3 * n + 1) + 1
            return memorized_cycles[n]
        else:   #even
            memorized_cycles[n] = collatz_solver(n >> 1) + 1
            return memorized_cycles[n]
    else :
        if n % 2:
            return collatz_solver(3 * n + 1) + 1
        else:
            return collatz_solver(n >> 1) + 1
	
# -------------
# collatz_print
# -------------

def collatz_print (w, (i, j), v) :
    """
    prints the values of i, j, and v
    w is a writer
    v is the max cycle length
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    for t in collatz_read(r) :
        v = collatz_eval(t)
        collatz_print(w, t, v)