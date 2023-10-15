# TODO Найдите количество книг, которое можно разместить на дискете
kol_vo_str = 100
strok = 50
symbols = 25
one_symbol = 4
volume_bait = 1024 ** 2 * 1.44

volume_book_bait = kol_vo_str * strok * symbols * one_symbol

print("Количество книг, помещающихся на дискету:", int(volume_bait // volume_book_bait))
