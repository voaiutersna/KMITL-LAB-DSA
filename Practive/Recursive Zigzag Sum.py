def RecursiveZigzagSum(n):
    #base case
    if not n:
        return 0
    if n > 0:
        if n % 2:
            return RecursiveZigzagSum(n-1) + n
        else:
            return RecursiveZigzagSum(n-1) - n
    else:
        if abs(n) % 2:
            return RecursiveZigzagSum(n+1) - n
        else:
            return RecursiveZigzagSum(n+1) + n

def main():
    inp = int(input())
    print(RecursiveZigzagSum(inp))
main()

