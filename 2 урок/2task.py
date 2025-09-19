age = int(input())
if age < 18:
    print("Молодой")
elif age >= 18 and age < 60:
    print("Взрослый")
elif age >= 60:
    print("Пожилой")