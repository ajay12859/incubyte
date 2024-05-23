def add(s):
    if s=="":
        return 0
    delim = ","
    if s.startswith("//"):
        delim = s[2]
        s = s[3:]

    nums = [ int(x.strip()) for x in s.split(delim)]
    sum = 0
    negatives = []
    hasNegative = False
    for n in nums:
        if n<0:
            negatives.append(str(n))
            if not hasNegative:
                hasNegative = True

        if not hasNegative:
            sum += n
    
    if hasNegative:
        raise Exception(f"negative numbers not allowed {','.join(negatives)}")
    return sum


if __name__ == '__main__':
    print(add("//;\n1;-2;-3"))