
Angka = int(input('Jumlah bilangan : '))

for num in range(2,42):
    prima = True
    for i in range(2,num):
        if (num%i==0):
            prima = False
    if prima:
       print (num)