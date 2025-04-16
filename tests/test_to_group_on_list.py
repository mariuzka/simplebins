import numbergroup as ng

l = [-10, -7, 0, 1, 90]

def test_list():
    assert ng.to_group(x=l, step=5, output="floor", origin=0) == [-10, -10, 0, 0, 90]
    
def test_empty_list():
    assert ng.to_group(x=[], step=5, output="floor", origin=0) == []