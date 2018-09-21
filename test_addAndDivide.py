def test_add_three():
    from addAndDivide import add_three
    s = add_three(1,2,3)
    assert s == 6

def test_divide_three():
    from addAndDivide import divide_three
    d = divide_three(6)
    assert d == 2
