def pow(x,n):
    #base case
    if n == 0:
        return 1
    if n > 0:
        #recur
        return x * pow(x,n-1)
    else:
        return 1/x * pow(x,n+1)
def main():
    x = float(input())
    n = int(input())
    print(pow(x,n))
main()


# 2^4 = 2 * 2^3 = 2 * (2 * 2^2) = 2 * 2 * (2 * 2^1)