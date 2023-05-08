from PIL import Image, ImageFilter
from pathlib import Path
import csv

def proc1():
    cur_d = ''
    file = Path(cur_d).glob('*')
    Path('new_d').mkdir(parents=True, exist_ok=True)
    for i in file:
        if i.suffix in ['.jpg', '.png']:
            with Image.open(i) as img:
                img.load()
                newimg = img.filter(ImageFilter.CONTOUR)
                newimg.save(Path('new_d', i))

def proc2():

    f = open("list.csv", "r")
    d = list(csv.reader(f, delimiter=";"))
    s = 0
    print("Нужно купить:")
    for i in d:
        print(f'{i[0]} - {i[1]} шт. за {i[2]} руб.')
        s = s + sum([int(i[1]) * int(i[2])])
    print(f'Итоговая сумма: {s} рублей')

proc1(), proc2()