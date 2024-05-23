import pytest

def add(s):
    nums = [ int(x) for x in s.split(',')]
    sum = 0
    for n in nums:
        sum += n
    return sum


# def test():
#     s1 = ""
#     s2 = "1"
#     # s3 =
#     assert add(s1) == 0

# test()



