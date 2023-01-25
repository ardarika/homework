print('Введите сумму, которую хотите снять:')
cash_in = int(input())
nom = [10,20,50,100,200,500,1000]
nom2 = nom[::-1]

for i in nom2:
    cash_out = cash_in//i
    cash_in = cash_in % i
    print(i, '-', cash_out)