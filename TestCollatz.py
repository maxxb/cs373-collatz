#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 10)
        
    def test_read_2 (self) :
        r = StringIO.StringIO("1 999999\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  1)
        self.assert_(j == 999999)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("50 51\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  50)
        self.assert_(j == 51)
        
    def test_read_4 (self) :
        r = StringIO.StringIO("123456 987654\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i ==  123456)
        self.assert_(j == 987654)
        

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval((1, 10))
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval((100, 200))
        self.assert_(v == 125)
 
    def test_eval_3 (self) :
        v = collatz_eval((201, 210))
        self.assert_(v == 89)
 
    def test_eval_4 (self) :
        v = collatz_eval((900, 1000))
        self.assert_(v == 174)
        
    #mine
    def test_eval_5 (self) :
        v = collatz_eval((111111, 999999))
        self.assert_(v == 525)
        
    def test_eval_6 (self) :
        v = collatz_eval((10100, 200201))
        self.assert_(v == 383)
        
    def test_eval_7 (self) :
        v = collatz_eval((1, 999999))
        self.assert_(v == 525)
        
        
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (100, 200), 125)
        self.assert_(w.getvalue() == "100 200 125\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (111111, 999999), 525)
        self.assert_(w.getvalue() == "111111 999999 525\n")
        
    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, (10100, 200201), 383)
        self.assert_(w.getvalue() == "10100 200201 383\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("794830 945413\n877637 958120\n425505 783680\n281057 940251\n126406 352861\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "794830 945413 525\n877637 958120 507\n425505 783680 509\n281057 940251 525\n126406 352861 443\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("24137 212741\n622811 705104\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "24137 212741 383\n622811 705104 509\n")
        
    def test_solve_4 (self) :
        r = StringIO.StringIO("616050 743680\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "616050 743680 509\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."