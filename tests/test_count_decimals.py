import simplebins

def test_count_decimals():
    assert simplebins._count_decimals(number=1) == 0
    assert simplebins._count_decimals(number=1.0) == 0
    assert simplebins._count_decimals(number=3.2) == 1
    assert simplebins._count_decimals(number=0.05) == 2
    assert simplebins._count_decimals(number=-1.02359) == 5