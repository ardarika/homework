f = open('fizz_buzz.txt', 'r')
for line in f:
    nums = line.split(' ')
    fizz, buzz = int(nums[0]), int(nums[1])
    for i in range(1, int(nums[2])+1):
        if not i%fizz and not i%buzz:
            print('FB')
        elif not i%fizz and i%buzz != 0:
            print('F')
        elif i%fizz != 0 and not i%buzz:
            print('B')
        else:
            print(i)
f.close()