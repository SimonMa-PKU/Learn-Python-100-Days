
print(0b100)
print(0o100)
print(0x100)

print("""This is a sentence:
            Let us do something.""")
# Plural or complex
print(3+5j + 3+3j)

a = 321
b = 12
print(a // b)
print(a % b)
print(a ** b)

a = 12
b = 1.23
c = 1 + 5j
d = 'hello'
e = 'True'
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(int('23'))
print(float('3.43'))
print(str(342))
print(chr(87))
print(ord('a'))

print(~0b1001)
print(~10)
# Ctrl + /  Pycharm annotation
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d ** %d = %d' % (a, b, a**b))

# f = float(input('Please enter a Fahrenheit degree: '))
# c = (f - 32) / 1.8
# print('%.1f F degree =\t %.1f C degree' % (f, c))

# import math
#
# radius = float(input("Please enter a radius: "))
# area = math.pi * radius * radius
# print('area = %.1f' % area)

year = int(input('Please enter a year: '))
is_leap = (year % 4 == 0 and year % 100 != 0) or \
    year % 400 ==0
print('Is this a leap year? ' + str(is_leap) +'!')

