fizz, buzz = int(input()), int(input())
for i in range(1, int(input())+1):
    if i%fizz == 0 and i%buzz == 0:
        print('FB')
    elif i%fizz == 0 and i%buzz != 0:
        print('F')
    elif i%fizz != 0 and i%buzz == 0:
        print('B')
    else:
        print(i)