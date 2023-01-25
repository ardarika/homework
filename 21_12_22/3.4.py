num = int(input())

#3
for i in range(1,num+1):
    if num%i==0:
        print(i)

#4
while num:
    last_digit = num%10
    num //= 10
    print(last_digit)