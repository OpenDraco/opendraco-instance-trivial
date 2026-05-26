from is_even import is_even


def test_zero_is_even():
    assert is_even(0)


def test_two_is_even():
    assert is_even(2)


def test_three_is_odd():
    assert not is_even(3)


def test_negative_even():
    assert is_even(-4)
