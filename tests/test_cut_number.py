import simplebins
import numpy as np
import pandas as pd

def test_x():
    assert simplebins.cut(x=0, binwidth=5, output="floor", origin=0) == 0
    assert simplebins.cut(x=1, binwidth=5, output="floor", origin=0) == 0
    assert simplebins.cut(x=5, binwidth=5, output="floor", origin=0) == 5
    assert simplebins.cut(x=-7, binwidth=5, output="floor", origin=0) == -10
    assert simplebins.cut(x=10, binwidth=5, output="floor", origin=0) == 10
    assert simplebins.cut(x=None, binwidth=5, output="floor", origin=0) is None
    assert pd.isna(simplebins.cut(x=np.nan, binwidth=5, output="floor", origin=0))

l = [-6, 3, 10]

def test_binwidth():
    assert [simplebins.cut(x=number, binwidth=1, output="floor", origin=0) for number in l] == [-6, 3, 10]
    assert [simplebins.cut(x=number, binwidth=3, output="floor", origin=0) for number in l] == [-6, 3, 9]
    assert [simplebins.cut(x=number, binwidth=5, output="floor", origin=0) for number in l] == [-10, 0, 10]

def test_output():
    assert [simplebins.cut(x=number, binwidth=5, output="floor", origin=0) for number in l] == [-10, 0, 10]
    assert [simplebins.cut(x=number, binwidth=5, output="ceiling", origin=0) for number in l] == [-5, 5, 15]
    assert [simplebins.cut(x=number, binwidth=5, output="index", origin=0) for number in l] == [-2, 0, 2]
    assert [simplebins.cut(x=number, binwidth=10, output="center", origin=0) for number in l] == [-5, 5, 15]
    assert simplebins.cut(x=7, binwidth=5, output="label", origin=0) == "5 <= x < 10"
    assert simplebins.cut(x=-3, binwidth=5, output="label", origin=0) == "-5 <= x < 0"

def test_origin():
    assert simplebins.cut(x=10, binwidth=5, output="floor", origin=0) == 10
    assert simplebins.cut(x=10, binwidth=5, output="floor", origin=1) == 6
    assert simplebins.cut(x=10, binwidth=5, output="floor", origin=5) == 10
    assert simplebins.cut(x=10, binwidth=5, output="index", origin=0) == 2
    assert simplebins.cut(x=10, binwidth=5, output="index", origin=1) == 1
    assert simplebins.cut(x=10, binwidth=5, output="index", origin=5) == 1

def test_ignore():
    assert simplebins.cut(x=3, binwidth=5, ignore=None) == 0
    assert simplebins.cut(x=3, binwidth=5, ignore=[]) == 0
    assert simplebins.cut(x=3, binwidth=5, ignore=[4]) == 0
    assert simplebins.cut(x=3, binwidth=5, ignore=[3]) == 3
    assert simplebins.cut(x=None, binwidth=5, ignore=[None]) is None