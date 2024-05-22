quantity_of_legs = int(input("Введіть кількість ніг:"))
quantity_of_eyes = int(input("Введіть кількість очей:"))
if quantity_of_legs == 4 and quantity_of_eyes == 2:
    print("Це кіт")
elif quantity_of_legs == 8 and quantity_of_eyes == 8:
    print("Це павук")
elif quantity_of_legs == 6 and quantity_of_eyes == 2:
    print("Це жучок")
elif quantity_of_legs == 0 and quantity_of_eyes >= 100:
    print("Це морський гребінець")
else:
    print("Невідома тварина")