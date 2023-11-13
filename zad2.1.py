koli = int(input())


parking = []

for _ in range(koli):
    event = input().split(', ')
    inout, reg_n = event[0], event[1]

    if inout == "IN":
        parking.append(reg_n)
    elif inout == "OUT" and reg_n in parking:
        parking.remove(reg_n)

if parking:
    for kola in parking:
        print(kola)
else:
    print("Parking is Empty")
