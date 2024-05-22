human_age = int(input("Вкажіть вік людини: "))
if human_age < 0:
    print("від'ємний вік не існує")
elif human_age < 6:
    print("Дошкільня")
elif human_age < 18:
    print("Школяр")
elif human_age < 60:
    print("Дорослий")
else:
    print("Пенсіонер")
