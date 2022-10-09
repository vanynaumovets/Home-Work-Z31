import math
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operation = input("Введите действие: (+,-,*,/)=")
if operation == "+":
 res = int(num1+num2)
 print("результат вычислений", res)
if operation == "-":
 res = int(num1-num2)
 print("результат вычислений", res)
if operation == "*":
 res = int(num1*num2)
 print("результат вычислений", res)
if operation == "/":
 res = int(num1/num2)
 print("результат вычислений", res)
