print('Введите сумму, которую хотите снять:')
cash_in = int(input())
nom = [10,20,50,100,200,500,1000]

for i in nom:
    cash_out = cash_in//i
    if cash_out <= 10:
        print(i, '-', cash_out)
        cash_in = cash_in - cash_out * i
    else:
        cash_in = cash_in - i*10
        print(i, '-', 10)
