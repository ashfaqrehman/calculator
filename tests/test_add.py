"""
Test the add() function of the calculator
"""
from calculator import add
def test_two_plus_two():
    """
    If given 2 and 2 as paramters, 4 should be returned
    """
    assert add(2,2) == 4

def test_three_plus_three():
    """
    If given 3 and 2 as paramters, 6 should be returned
    """
    assert add(3,3) == 6   

def test_no_parameters():
    """
    IF no params are provided return 0
    """    
    assert add() == 0

def test_one_two_three():
    """
    Given values 1,2,3 should return 6
    """
    assert add(1,2,3) == 6

def test_negative_values():
    """
    Given values -11,-1,22 should return 6
    """
    assert add(-11,-1,22) == 10