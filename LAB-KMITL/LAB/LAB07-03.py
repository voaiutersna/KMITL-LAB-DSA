import json
def main(num,last_index):
    count = 0 
    for i in range(last_index+1):
        swapped = False
        for j in range(last_index-1, i-1, -1):
            count += 1
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                swapped = True
        print(num)
        if not swapped:
            break
    print(f"Comparison times: {count}")
    # print(last_index)
main(json.loads(input()),int(input()))