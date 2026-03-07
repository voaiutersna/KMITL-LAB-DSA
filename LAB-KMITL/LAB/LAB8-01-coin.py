def convert_key(data):
  """JSON"""
  return {int(k): v for k, v in data.items()}

def coinExchange(amount, coins):
    result = {}
    remaining = amount
    for coin in sorted(coins.keys(), reverse=True):
        use = min(remaining // coin, coins[coin])
        result[coin] = use
        remaining -= use * coin
    if remaining > 0:
        return None
    return result

def main():
    import json
    amount = int(input())
    data = convert_key(json.loads(input()))

    print(f"Amount: {amount}")
    result = coinExchange(amount, data)
    if result is None:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        total_coins = 0
        for coin in sorted(result.keys(), reverse=True):
            print(f"  {coin} baht = {result[coin]} coins")
            total_coins += result[coin]
        print(f"Number of coins: {total_coins}")

main()