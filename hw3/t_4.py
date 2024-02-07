lst = [1, 1, 2, 2, 3, 3, 4]


print(list(set([i for i in lst if lst.count(i) > 1])))


# duplicates = set()
#
# for item in lst:
#     if lst.count(item) >= 2:
#         duplicates.add(item)
#
# result = list(duplicates)
# print(result)
