import json
list01 = json.loads(input())
list02 = json.loads(input())
list03 = json.loads(input())
result1, result2, result3 = set(list01), set(list02), set(list03)
print(bool(result1 & result2 & result3))