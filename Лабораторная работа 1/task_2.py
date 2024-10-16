# TODO Найдите количество книг, которое можно разместить на дискете

VOLUME_PER_SYMBOL = 4 #Байта
BITES_PER_MEGABYTE = 1024 * 1024

disk_volume = 1.44 #Мб
pages_per_book = 100 # Штук
lines_per_page = 50 # Штук
symbols_per_page = 25 #Штук

volume_in_bites = disk_volume * BITES_PER_MEGABYTE
volume_per_book = pages_per_book * lines_per_page * symbols_per_page * VOLUME_PER_SYMBOL
books_count = int(volume_in_bites // volume_per_book)

print("Количество книг, помещающихся на дискету:", books_count)

