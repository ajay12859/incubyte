def add(s):
    if s=="":
        return 0
    delim = ","
    if s.startswith("//"):
        delim = s[2]
        s = s[3:]

    nums = [ int(x.strip()) for x in s.split(delim)]
    sum = 0
    
    for n in nums:
        if n<0:
            raise Exception(f"negative numbers not allowed {str(n)}")
        sum += n
    return sum


if __name__ == '__main__':
    print(add("//;\n1;2;-3"))