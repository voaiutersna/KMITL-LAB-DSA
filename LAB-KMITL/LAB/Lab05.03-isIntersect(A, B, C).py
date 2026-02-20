import json
list1 = json.loads(input())
list2 = json.loads(input())
list3 = json.loads(input())
print(bool(set(list1) & set(list2) & set(list3)))
# print(set(list1) & set(list2))