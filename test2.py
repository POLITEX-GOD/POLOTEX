a = int(input("Введите число: "))
print(a * 2)
if a > 0:
    print("положительное")
elif a == 0:
    print("ноль")
else:
    print("отрицательное")
try:
    n = int(input("число: "))
except ValueError:
    print("это не число")