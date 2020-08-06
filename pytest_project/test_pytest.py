import pytest
# w cmd robimy pip install pytest-xdist co pozwo;i nam uruchaiac kilka testow na raz
#@pytest.mark.skip -- pomijany jest dany test
#@pytest.mark.xfail -- informacja, ze pewne testy powinny failowac ze wzgledu na bledy
@pytest.mark.skip
def test_method():
    x = 5
    y = 2
    assert x+y==7, "Assertion failed, Excepted 7"
    assert x+y==2, "Assertion failed, Expected 2"

def test_method2():
    x = 5
    y = 2
    assert x+y==7, "Assertion failed, Excepted 7"
    assert x+y==2, "Assertion failed, Expected 2"

def random_name():
    x = 5
    y = 2
    assert x+y==7, "Assertion failed, Excepted 7"
    assert x+y==2, "Assertion failed, Expected 2"

def random_name_test():
    x = 5
    y = 2
    assert x+y==7, "Assertion failed, Excepted 7"
    assert x+y==2, "Assertion failed, Expected 2"
