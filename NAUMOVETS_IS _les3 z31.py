# задание №1

# word1 = "Петр"
# word2 = "Идет"
# print(word1,    word2, sep=" ! ")


# задание №2
user_data1 = input("введите ваше имя: ")
user_data2 = int(input("введите ваш возраст: "))
# вариант 1
# while user_data2 <= 0:
#    if user_data2 <=0:
#       print("Ошибка, повторите ввод")
# while user_data2 > 0 or user_data2 < 10:
#    print("Привет, шкет", user_data1)
# while user_data2 >= 10 or user_data2 < 18:
#    print ("как жизнь", user_data1)
# while user_data2 >= 18 or user_data2 < 100:
#    print("что желаете", user_data1)
# while user_data2 > 100:
#    print(user_data1, "вы лжете в наше время столько не живут")
# вариант 2
if user_data2 <=0:
    print("Ошибка, повторите ввод")
for user_data2 in range (1, 9):
    print("Привет, шкет", user_data1)
    if user_data2 == 10: break
for user_data2 in range (10, 18):
    print("как жизнь", user_data1)
    if user_data2 == 19: break
for user_data2 in range (19, 99):
    print("что желаете", user_data1)
    if user_data2 == 100: break
for user_data2 in range (100, 1000):
    print(user_data1, "вы лжете в наше время столько не живут")
    if user_data2 == 1000: break



