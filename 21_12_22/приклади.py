a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)

num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'виграло')
else:
    print('число', num2, 'виграло')

num = 7
if (num <0):
    print('Number is smaller than Zero')
elif (num> 0):
    print('Number is greater than Zero')
else: print('Number is Zero')

