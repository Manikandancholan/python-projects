# #1. FizzBuzz

# for i in range(1, 100):
#     output = ""
#     if i % 3 == 0:
#         output += "Fizz"
#     if i % 5 == 0:
#         output += "Buzz"
#     print(output or i)


# #2. Factorial Calculation

# def factorial_recursive(n):
#     if n < 0:
#         return "Undefined for negative numbers"
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_recursive(n - 1)
# number = int(input("enter an integer value: "))
# print("Factorial:", factorial_recursive(number))


# #3. Prime number checker

# num = int(input("Enter an integer: "))
# if num > 1:
#     for i in range(2, (num//2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


# #4. Sample API call

# import requests as req

# city = input("Enter a city name: ")

# apiKey = "b03a640e5ef6980o4da35b006t5f2942"
# url = "https://api.shecodes.io/weather/v1/forecast?query="+city+"&key="+apiKey

# response = req.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Failed to retrieve data: {response.status_code}")


import psycopg2 as psqlEngine

conn = psqlEngine.connect("dbname=testDB user=postgres password=postgres")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
conn.close()
