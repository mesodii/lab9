import csv

f = open("list.csv", "r")
d = list(csv.reader(f, delimiter=";"))
print("Нужно купить:")
s = 0
for i in d:
    print(f'{i[0]} - {i[1]} шт. за {i[2]} руб.')
    s = s + sum([int(i[1])*int(i[2])])
print(f'Итоговая сумма: {s} рублей')