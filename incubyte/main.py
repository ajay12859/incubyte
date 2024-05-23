def add(s):
    if s=="":
        return 0
    nums = [ int(x) for x in s.split(',')]
    sum = 0
    for n in nums:
        sum += n
    return sum


if __name__ == '__main__':
    add("")