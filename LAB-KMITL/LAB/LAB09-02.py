import json


def knapsackV2(amount, itemList):
    n = len(itemList)

    # dp[i][w] = max value using first i items with weight limit w
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, price, weight = itemList[i - 1]
        for w in range(amount + 1):
            dp[i][w] = dp[i - 1][w]  # don't take item i
            if weight <= w:
                take = dp[i - 1][w - weight] + price
                if take > dp[i][w]:
                    dp[i][w] = take

    # Traceback
    chosen = []
    w = amount
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(itemList[i - 1])
            w -= itemList[i - 1][2]

    chosen.sort(key=lambda x: x[0])

    print(f"Total: {dp[n][amount]}")
    for name, price, weight in chosen:
        print(f"{name} -> {weight} kg -> {price} THB")


itemList = json.loads(input())
amount = int(input())
knapsackV2(amount, itemList)
