island_side = int(input("Введіть сторону острова: "))
quantities_of_robinzones = int(input("Введіть кількість розбінзонів: "))
norm_of_square = int(input("Введіть норму площі: "))
square = island_side**2
possible_of_robinzons = square // norm_of_square - quantities_of_robinzones
if possible_of_robinzons > quantities_of_robinzones:
    print("Ще можна поселити", possible_of_robinzons, "робінзонів")
else:
    print("Більше не можна поселити робінзонів")
