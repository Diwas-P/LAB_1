list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6]
result = []

for item in list1:
    if item not in list2:
        result.append(item)
        
print("New list:", result)