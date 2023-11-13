n = int(input())

ocenki = {}

for _ in range(n):
    u4enik, ocenka = input().split()
    ocenka = float(ocenka)
    
    if u4enik in ocenki:
        ocenki[u4enik].append(ocenka)
    else:
        ocenki[u4enik] = [ocenka]

for u4enik, grades in ocenki.items():
    average_grade = sum(grades) / len(grades)
    ocenki[u4enik] = (grades, average_grade)

for u4enik, (grades, average_grade) in ocenki.items():
    grades_str = " ".join(map(str, grades))
    print(f"{u4enik} -> {grades_str} (avg: {average_grade:.2f})")
