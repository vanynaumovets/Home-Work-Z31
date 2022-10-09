# 1
# file = open('text.csv', 'w')
# file.write('Введите ваше имя:\n')
# file.write('введите ваш возраст:\n')
# file.close()
# print(file)
#1
# file = open('text.xls', 'w')
# file.write('Введите ваше имя:\n')
# file.write('введите ваш возраст:\n')
# file.close()
# print(file)

#2
file = open('data.txt', 'w')
file.write( 'name: Anna\n'
             'firs name: Ivanova\n'
             'age: 24 yaers old\n')
file.write('дезиинформация')

import csv
txtfile = r'data.txt'
csvfile = r'data.csv'
with open (txtfile, 'r') as infile, open(csvfile, 'r'):
    stripped = (line.strip() for line in infile)
    lines = (line.split() for line in stripped if line)
file.close()




