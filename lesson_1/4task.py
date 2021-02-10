a = int (input ('Введите положительное число: '))
b = 0
while a <= 0:
    print ('Ваше число отрицательное!')
    break
while a > 0:
     c = a % 10
     if c >= b : b = c
     a//= 10

print (b)
