import simplebins

def test_list():
    l = [-10,  -7, 0, 1, 90]
    e = [-10, -10, 0, 0, 90]
    assert simplebins.cut(x=l, binwidth=5, output="floor", origin=0) == e

def test_list_with_None():
    l = [1, 90, None]
    e = [0, 90, None]
    assert simplebins.cut(x=l, binwidth=5, output="floor", origin=5) == e
    
def test_empty_list():
    l = []
    e = []
    assert simplebins.cut(x=l, binwidth=5, output="floor", origin=0) == e