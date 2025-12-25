def AlternatingPowerSum(n):
    #base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    #recur
    if n%2:
        return n**2 + AlternatingPowerSum(n-1)
    else:
        return -(n**2) +  AlternatingPowerSum(n-1)
    

def main():
    n = int(input())
    result = AlternatingPowerSum(n)
    print(result)
main()
