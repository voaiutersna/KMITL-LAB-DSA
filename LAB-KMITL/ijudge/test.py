# print("1".isnumeric())
# inp = input().split()
# print(inp[0])
def main():
    loop = int(input())
    for i in range(loop):
        inp = input()
        student = inp[:8]
        data = inp[12:]
        print(student,loop)
main()