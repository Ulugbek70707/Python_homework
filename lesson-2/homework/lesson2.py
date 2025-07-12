# 1
name = input("Enter your name: ") 
Year_of_birth = int(input("Enter year of birth: "))
current_year = 2025 

Age = current_year-Year_of_birth
print(f"Hello, {name}! You are {Age} years old.")

# 2
txt = 'LMaasleitbtui'
car_name = txt[0]+txt[2]+txt[4]+txt[6]+txt[8]+txt[10]+txt[12]
print("Car name:", car_name)

# 3
txt = 'MsaatmiazD'
car_name_1 = txt[0]+txt[2]+txt[4]+txt[6]+txt[8]
car_name_2 = txt[9]+txt[2]+txt[5]+txt[3]+txt[1]
print("Car name:", car_name_1)
print("Car name:", car_name_2)

# 4
txt = "I'am John. I am from London"
area = txt.split("from ")[1]
print("Residence area:", area)

# 5
word = input("Enter any word: ")
reversed_word = word[::-1]
print("Reversed word:",reversed_word)


# 6
text = input("Enter any word: ")
vowels = 'aeiouAEIOU'
count = 0
for char in text:
     if char in vowels:
          count += 1
print("Number of vowels:", count)

# 7
List = {4,5,6,7,10,21,58,12}
maximum = max(List)
print("Maximum value is:", maximum)

# 8
Something = input('Enter a word: ')
if Something == Something[::-1]:
     print("It's a palindrome")
else:
     print("It's not a palindrome.")      
     
# 9
email = input("Enter email address: ")
domain = email.split('@')[1]
print("email domain is:",domain)

# 10
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(12))
print("Generated password:", password)
