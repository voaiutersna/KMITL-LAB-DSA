import json


def main():
    amount = int(input())
    coins_raw = input()
    coins = {int(k): v for k, v in json.loads(coins_raw).items()}

    print(f"Amount: {amount}")

    denominations = sorted(coins.keys(), reverse=True)
    n = len(denominations)

    # dp[i][j] = min coins to make amount j using first i denominations
    # used[i][j] = how many coins of denomination i were used
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
    used = [[0] * (amount + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        d = denominations[i - 1]
        c = coins[d]
        for j in range(amount + 1):
            dp[i][j] = dp[i - 1][j]  # use 0 of this denomination
            used[i][j] = 0
            for k in range(1, min(c, j // d) + 1):
                if dp[i - 1][j - k * d] != float('inf'):
                    val = dp[i - 1][j - k * d] + k
                    if val < dp[i][j]:
                        dp[i][j] = val
                        used[i][j] = k

    if dp[n][amount] == float('inf'):
        print("Can not exchange.")
        return

    # Traceback
    result = {}
    j = amount
    for i in range(n, 0, -1):
        d = denominations[i - 1]
        result[d] = used[i][j]
        j -= used[i][j] * d

    print("Coin exchange result:")
    total = 0
    for d in denominations:
        print(f"  {d} baht = {result[d]} coins")
        total += result[d]
    print(f"Number of coins: {total}")


main()
