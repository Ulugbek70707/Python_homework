# 1
def is_leap(year):
     if not isinstance(year, int):
          raise ValueError("Year must be an integer.")
     return (year%4 == 0 and year%100 != 0) or (year % 400 == 0)
try:
    year = int(input("Yilni kiriting: "))
    if is_leap(year):
        print(f"{year} kabisa yili.")
    else:
         print(f"{year} kabisa yili emas.")
except ValueError:
     print("Iltimos butun son kiritishingiz kerak.")

# 2
n = int(input("n sonini kiriting: "))

if n % 2 == 1:  # Agar toq bo'lsa
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

# 3
# 1st solution
a = int(input('a = '))
b = int(input('b = '))

def even_numbers_if(a, b):
    if a>b:
        return[]
    if a%2 == 0:
        return[a]+even_numbers_if(a+1,b)
    else:
        return even_numbers_if(a+1,b)
result = even_numbers_if(a,b)
print("Juft sonlar: ", result)

# 2nd solution
a = int(input('a = '))
b = int(input('b = '))
def even_numbers_no_if(a, b):
    start = a + (a % 2)
    return list(range(start, b+1, 2))
print("Juft sonlar: ", even_numbers_no_if(a,b))
