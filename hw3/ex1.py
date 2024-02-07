'''def user_backpack(items, max_weight):
    collected_items = {}
    count = 0
    for item, weight in items.items():
        if weight <= max_weight:
            collected_items[str(item)] = weight
            max_weight -= weight
    return collected_items

items = {'tent': 6, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
max_weight = 12
# print(user_backpack(items, max_weight))

backpack = user_backpack(items, max_weight)
print(backpack)'''
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

sorted_items = dict(sorted(items.items(), key = lambda item: item[1]))
weight = 0
backpack = {}
for k, v in sorted_items.items():
    if weight + v > max_weight:
        break
    else:
        weight += v
        backpack[k] = v
print(backpack)