chisla = input().split()

srchisla = {}

for i in chisla:
    i = float(i)
    formatirano_chislo = '{:.1f}'.format(i)
    
    srchisla[formatirano_chislo] = srchisla.get(formatirano_chislo, 0) + 1

for num, count in srchisla.items():
    print(f'{num} - {count} times')