import json

def bubble(num,lastindex):
    count = 0
    for i in range(lastindex+1): #i is sorted index
        swapped= False
        for j in range(lastindex-1,i-1,-1): #im start at before_lastindex and -- until first unsorted index
            count += 1
            if ((num[j][0],int(num[j][1:])) > (num[j+1][0],int(num[j+1][1:]))):
                swapped = True
                num[j] , num[j+1] = num[j+1], num[j]
        print(num)
        if not swapped:
            break
    print(f"Comparison times: {count}")
bubble(json.loads(input()),int(input()))