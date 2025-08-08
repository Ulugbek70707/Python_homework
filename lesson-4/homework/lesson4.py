# 1
my_dict = {"apple":6, "banana":3, "orange":5, "peach":4, "lemon":2}
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Original dictionary:", my_dict)
print("Sorted by value (ascending):", ascending)
print("Sorted by value (descending):", descending)

# 2
sample_dict = {0:10, 1:20}
sample_dict[2]=30 
print(sample_dict)

# 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = dic1|dic2|dic3
print(merged_dict)

# 4
dic_1 = {}
for i in range(1,6):
    dic_1[i] = i*i
print(dic_1)

# 5
dic_2 = {}
for i in range(1,16):
     dic_2[i] = i*i
print(dic_2)

# 6
set_1 = {1, "Lola", True, "apple" }
print(set_1)

# 7
set_2 = {'apple', 'banana', 'cherry'}
for item in set_2:
     print(item)

# 8
set_3 = {'apple', 'banana', 'cherry'}
set_3.update(['orange', 'lemon', 'grapefruit'])
print(set_3)

# 9
set_4 = {'apple', 'banana', 'cherry'}
set_4.remove('apple')
print(set_4)

# 10
fruits = {"apple", "banana", "cherry"}
item = "banana"
if item in fruits:
    fruits.remove(item)
    print(f"{item} has been removed from the set.")
else:
    print(f"{item} is not in the set.")
print("Updated set:", fruits)
