#Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно.

def sum_range(start, end):
  summa = 0
  for i in range(start, end +1):
    summa +=i
    print(summa)

  return summa

summa=sum_range(0,10)
print(summa)