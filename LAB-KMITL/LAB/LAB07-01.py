import json

def insertion(num,last_index):
    count = 0
    # print(num)
    # print(last_index)
    for i in range(last_index+1):
        if not i:
            continue
        for j in range(i,0,-1):
            count += 1
            if num[j-1] > num[j]:
                num[j-1] , num[j] = num[j] , num[j-1]
            else:
                break
        print(num)
    print(f"Comparison times: {count}")

    # print("-----")
    # for i in range(0,-1,-1):
    #     print(i)
insertion(json.loads(input()),int(input()))
