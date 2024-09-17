# from datetime import datetime
# import locale

# # Yerel ayarı Türkçe olarak ayarlıyoruz
# try:
#     locale.setlocale(locale.LC_ALL, "Turkish")  # veya "tr_TR.UTF-8"
# except locale.Error:
#     print("Yerel ayar desteklenmiyor!")

# # Şu anki tarihi alıyoruz
# a = datetime.now()

# # Ayın adını almak için "%B" formatını kullanıyoruz
# tam_tarih = datetime.strftime(a, "%B")

# # Türkçe ay adını ekrana yazdırıyoruz
# print(tam_tarih)


# from datetime import datetime
# from babel.dates import format_date

# a = datetime.now()
# tam_tarih = format_date(a, locale='tr_TR')

# print(tam_tarih)
from datetime import datetime
import locale

# Yerel ayarı Türkçe olarak ayarlıyoruz (Windows için doğru ayar)
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")

# Şu anki tarihi alıyoruz
a = datetime.now()

# Ayın adını almak için "%B" formatını kullanıyoruz
tam_tarih = datetime.strftime(a, "%B")

# Türkçe ay adını ekrana yazdırıyoruz
print(tam_tarih)
