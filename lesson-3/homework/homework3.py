1
fruit_list = ['apple', 'orange', 'banana', 'peach', 'grape']
print(fruit_list[2])

2
first_list = [10,15,18]
second_list = [12,14,19]
combined = first_list+second_list
sorted_list=sorted(combined)
print(sorted_list)

3
list_numbers = [7, 8, 14, 21, 48, 16]
first = list_numbers[0]
middle = list_numbers[len(list_numbers)//2]
last = list_numbers[-1]
result=[first,middle,last]
print(result)

4
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Parasite"]
my_tuple = tuple(favorite_movies)
print(my_tuple)

5
list_cities = ['London', 'New-York', 'Tokyo', 'Madrid', 'Paris']
if 'Paris' in list_cities:
    print('Paris is in the list')
else:
    print('Paris is not in the list')

6
list_of_numbers = [8, 18, 4, 12, 16]
duplicate = list_of_numbers*2
print(duplicate)

7
list_num = [1,2,3,4,5]
list_num[0], list_num[-1] = list_num[-1], list_num[0]
print(list_num)

8
tuple_numbers = (1,2,3,4,5,6,7,8,9,10)
sliced_tuple = tuple_numbers[3:7]
print(sliced_tuple)

9
list_colors = ['red', 'blue', 'black', 'white', 'yellow', 'green', 'blue', 'orange', 'blue']
print(list_colors.count('blue'))

10
tuple_animals = ('lion', 'wolf', 'giraffe', 'monkey', 'elephant')
lion_index = tuple_animals.index('lion')
print(lion_index)

11
first_tuple = (15, 34, 80, 401, 48)
second_tuple = (20, 16, 32, 28, 14)
single_tuple = first_tuple+second_tuple
print("Merged tuple:", single_tuple)

12
List_1 = ['London', 'New-York', 'Tokyo', 'Madrid', 'Paris']
Tuple_1 = ('lion', 'wolf', 'giraffe', 'monkey')
list_length = len(List_1)
tuple_length = len(Tuple_1)
print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)

13
Tuple_of_numbers = (1,7,8,9,2,3,4,5)
list_converted = list(Tuple_of_numbers)
print("Converted list:", list_converted)

14
T_of_numbers = (1,7,8,9,2,3,4,5)
max_value = max(T_of_numbers)
min_value = min(T_of_numbers)
print("Max value:",max_value)
print("Min valie:",min_value)

15
tuple_of_words = ('lion', 'wolf', 'giraffe', 'monkey', 'elephant')
reversed_tuple = tuple_of_words[::-1]
print("Original tuple:", tuple_of_words)
print("Reversed tuple:", reversed_tuple)
