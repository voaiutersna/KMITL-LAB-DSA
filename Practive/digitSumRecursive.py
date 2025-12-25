def digitSumRecursive(inp,l,num):
    #base case
    if l == len(inp):
        return num
    #process
    if int(inp[l]) % 2:
        num -= int(inp[l])
    else:
        num += int(inp[l])

    #recur
    return digitSumRecursive(inp,l+1,num)

def digitSumRecursive02(inp,l):
    #base case
    if l == len(inp):
        return 0
    #process
    digit = int(inp[l])
    if digit % 2:
        #recur
        return -digit + digitSumRecursive02(inp,l+1)
    else:
        #recur
        return digit + digitSumRecursive02(inp,l+1)
def main():
    inp = input()
    num = 0
    l= 0
    result = digitSumRecursive(inp,l,num)
    print(result)
    result02 = digitSumRecursive02(inp,l)
    print(result02)
main()
