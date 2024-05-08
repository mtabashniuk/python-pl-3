photo_size = 3020 * 2016 * 3
storage_space = int(input("Введіть обсяг карти памяті, Гб: ")) * 1073741824
saved_photoes = int(input("Введіть к-сть збережених фото: "))
used_storage = saved_photoes * photo_size
unused_storage = storage_space - used_storage
possible_photoes_quantity = unused_storage // photo_size
print("Ще можна зберегти", possible_photoes_quantity, "фото")
