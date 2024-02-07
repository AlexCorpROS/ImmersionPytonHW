'''items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1
backpacks = []
sorted_result = []
for i in range(2**len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks.append(backpack)

full_result = [backpack for backpack in backpacks if backpack]
result = []
for item in full_result:
    if item not in result:
        result.append(item)

print(result)'''

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1

'''backpacks = []
sorted_result = []
for i in range(2**len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks.append(backpack)

full_result = [backpack for backpack in backpacks if backpack]
result = []
for item in full_result:
    if item not in result:
        result.append(item)

print(result)'''

'''def fill_backpack(item, max_weight, current_weigth, current_items, result):
    for item, weight in items.item():
        if current_weigth + weight <= max_weight:
            current_items[item] = weight
            current_weigth += weight
        if current_weigth == max_weight:
            result.append(dict(current_items))
        else:
            fill_backpack(item, max_weight, current_weigth, current_items, result)
        del current_items(item)
        current_weigth -= weight'''

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1
backpacks = []
sorted_result = []
for i in range(2**len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks.append(backpack)

full_result = [backpack for backpack in backpacks if backpack]
result = []
for item in full_result:
    if item not in result:
        result.append(item)

print(result)