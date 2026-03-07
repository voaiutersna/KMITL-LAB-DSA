class Item:
  def __init__(self, name, price, weight):
    self.__name = name
    self.__price = price
    self.__weight = weight

  def get_name(self):
    return self.__name

  def get_price(self):
    return self.__price

  def get_weight(self):
    return self.__weight

  def get_cost(self):
    return self.__price / self.__weight


def knapsack(items, amount):
  sorted_items = sorted(items, key=lambda item: item.get_cost(), reverse=True)
  remaining = amount
  picked = []
  total = 0

  for item in sorted_items:
    if item.get_weight() <= remaining:
      picked.append(item)
      remaining -= item.get_weight()
      total += item.get_price()

  print(f"Knapsack Size: {amount} kg")
  print("===============================")
  for item in picked:
    print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
  print(f"Total: {total} THB")


def main():
  import json
  items = []
  num_items = int(input())
  while num_items != 0:
    item_in = json.loads(input())
    items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
    num_items = num_items - 1
  knapsack_capacity = float(input())
  knapsack(items, knapsack_capacity)

main()
