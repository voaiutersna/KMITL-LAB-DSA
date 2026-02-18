import json
def selection(num,last_index):
    count = 0
    for i in range(last_index):
        smallest = num[i]
        smallest_index = i
        for j in range(i+1,last_index+1):
            count += 1
            if smallest > num[j]:
                smallest = num[j]
                smallest_index = j
        num[i] , num[smallest_index] = num[smallest_index] , num[i]
        print(num)
    print(f"Comparison times: {count}")
selection(json.loads(input()),int(input))
