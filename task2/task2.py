print("Розрахунок довжини огороди та кількості саджанців")
a = int(input("Введіть довжину, м: "))
b = int(input("Введіть ширину, м: "))
perimeter = 2 * (a + b)
square = a * b
seedlings_per_meter = 4
total_seedlings = seedlings_per_meter * square
print("Довжина огорожі: ", perimeter, "метрів")
print("К-сть саджанців: ", total_seedlings, "шт")