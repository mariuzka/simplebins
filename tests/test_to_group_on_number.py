import numbergroup as ng

def test_x():
    assert ng.to_group(x=0, step=5, output="floor", origin=0) == 0
    assert ng.to_group(x=1, step=5, output="floor", origin=0) == 0
    assert ng.to_group(x=5, step=5, output="floor", origin=0) == 5
    assert ng.to_group(x=-7, step=5, output="floor", origin=0) == -10
    assert ng.to_group(x=10, step=5, output="floor", origin=0) == 10

l = [-6, 3, 10]

def test_step():
    assert [ng.to_group(x=number, step=1, output="floor", origin=0) for number in l] == [-6, 3, 10]
    assert [ng.to_group(x=number, step=3, output="floor", origin=0) for number in l] == [-6, 3, 9]
    assert [ng.to_group(x=number, step=5, output="floor", origin=0) for number in l] == [-10, 0, 10]

def test_output():
    assert [ng.to_group(x=number, step=5, output="floor", origin=0) for number in l] == [-10, 0, 10]
    assert [ng.to_group(x=number, step=5, output="ceiling", origin=0) for number in l] == [-5, 5, 15]
    assert [ng.to_group(x=number, step=5, output="index", origin=0) for number in l] == [-2, 0, 2]
    assert [ng.to_group(x=number, step=10, output="mid", origin=0) for number in l] == [-5, 5, 15]
    assert ng.to_group(x=7, step=5, output="label", origin=0) == "5 <= x < 10"
    assert ng.to_group(x=-3, step=5, output="label", origin=0) == "-5 <= x < 0"

def test_origin():
    assert ng.to_group(x=10, step=5, output="floor", origin=0) == 10
    assert ng.to_group(x=10, step=5, output="floor", origin=1) == 5
    assert ng.to_group(x=10, step=5, output="floor", origin=5) == 5
    assert ng.to_group(x=10, step=5, output="index", origin=0) == 2
    assert ng.to_group(x=10, step=5, output="index", origin=1) == 1
    assert ng.to_group(x=10, step=5, output="index", origin=5) == 1
    