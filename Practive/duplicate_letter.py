def main():
    text = input()
    hashmap = {}
    for i in text:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
    print(hashmap)
main()
