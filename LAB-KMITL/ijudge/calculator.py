def main():
    num = int(input())
    count = 0
    if num == 1:
        print(1)
        return
    #process
    for i in range(1,num+1):
        count += len(str(i))
    #result
    print(count+1+num-1)
main()
