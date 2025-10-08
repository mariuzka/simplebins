import simplebins
import pandas as pd
import numpy as np


def test_series():
    s = pd.Series([3, 13, 89])
    e = pd.Series([0, 10, 80])
    s = simplebins.cut(x=s, binwidth=10, output="floor", origin=0)
    assert s.to_list() == e.to_list()

def test_series_with_None():
    s = pd.Series([3, 13, None])
    e = pd.Series([0, 10, None])
    s = simplebins.cut(x=s, binwidth=10, output="floor", origin=0)
    
    for i, val in enumerate(s.to_list()):
        val is e.to_list()[i]

def test_series_with_NA():
    s = pd.Series([3, 13, np.nan])
    e = pd.Series([0, 10, np.nan])
    s = simplebins.cut(x=s, binwidth=10, output="floor", origin=0)
    
    for i, val in enumerate(s.to_list()):
        val is e.to_list()[i]