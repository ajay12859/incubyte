import pytest
from main import add

assert add("") == 0
assert add("1") == 1
assert add("1,5") == 6
assert add("1,2,3,4,5") == 15
assert add("1\n,2,3") == 6
assert add("//;\n1;2;3") == 6

with pytest.raises(Exception) as e_info:
    add("1,-2,3")
    assert str(e_info.value) == 'negative numbers not allowed -2'