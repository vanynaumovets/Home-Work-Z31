
print("Добро пожаловать в программу  Калькулятор:")

a = float(input("Введите число №1:"))

print(a)

b = float(input("Введите число №2:"))

print((b))

action = input("действие:")

if action == "+":
 result = a+b

elif action == "-":
 result = a-b

elif action == "/":
 result = a / b

elif action == "*":
 result = a*b

elif action == "**":
  result = a**b
print(round(result, 2))



