import random
import pytest

def test_random_list():
    l = sorted([random.randint(a=1, b=100) for i in range(10)])
    assert len(l) == 10




