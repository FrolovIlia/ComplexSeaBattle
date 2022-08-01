import pytest

from Ships import *


shot = [0, 1]
pos = [[0, 0], [0, 1], [0, 2], [0, 3]]
name = 'Carrier'

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_num1(self=None):
    assert Ship.shot_at_ship(self, shot) == True
