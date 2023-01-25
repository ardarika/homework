f = open('fizz_buzz.txt', 'r')
f2 = open('fb_w.txt', 'w')
for line in f:
    nums = line.split(' ')
    fizz, buzz = int(nums[0]), int(nums[1])
    for i in range(1, int(nums[2])+1):
        if not i%fizz and not i%buzz:
            print('FB')
            f2.write('FB' + '\n')
        elif not i%fizz and i%buzz != 0:
            print('F')
            f2.write('F' + '\n')
        elif i%fizz != 0 and not i%buzz:
            print('B')
            f2.write('B' + '\n')
        else:
            print(i)
            f2.write(str(i) + '\n')
f2.close()
f.close()
