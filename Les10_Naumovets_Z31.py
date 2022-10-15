
# задание №1
try:
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

except ValueError:
 '''
 данное исключение, вызывается 
 при возникновении ошибки 
 с неверным форматом введенных данных 
 '''
 print("Ошибка ввода, не верный формат!!!")

except ZeroDivisionError:
 print("На 0 делить нельзя, введите коректные данные")
# данное исключение вызывается при нарушении арифметических правил о запрете деления на 0

