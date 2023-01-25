fizz, buzz = int(input()), int(input())
result = ['FB' if not i%fizz and not i%buzz else 'F' if not i%fizz and i%buzz != 0 else 'B' if i%fizz != 0 and not i%buzz else i for i in range(1, int(input())+1)]
print(result)