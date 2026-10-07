from math import*
print('Введите A:')
a=int(input())
print('Введите B:')
b=int(input())
print('Введите C:')
c=int(input())
if not(-10000<=a<=10000) or not(-10000<=b<=10000) or not(-10000<=c<=10000):
    print('Неверные исходные данные')
    print(1)
else:
    if a!=0:
        print('квадратное')
    if a==0 and b != 0:
        print('линейное')
    if a==0 and b==0:
        print('не уравнение')
        print(1)
    if a!=0:
        d=b**2-4*a*c
        if d>=0:
            print('дискриминант = ', d)
            x1=(-b+sqrt(d))/2/a
            x2 = (-b - sqrt(d)) / 2 / a
            if x1!=x2:
                print('корень 1 = ',x1)
                print('корень 2 = ',x2)
            else:
                print('корень = ', x1)
        else:
            print("нет действительных корней")
        print(0)
    if a==0 and b != 0:
        x=-c/b
        print('корень = ',x)
        print(0)