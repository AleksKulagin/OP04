#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа, после return перечислить все значения через запятую): периметр квадрата, площадь квадрата и диагональ квадрата.


def square(arg):
  perimeter = arg * 4
  area = arg **2
  diagonal = arg * 2 ** 0.5
  return perimeter, area, diagonal