from datetime import datetime
import locale

# Yerel ayarı Türkçe olarak ayarlıyoruz
locale.setlocale(locale.LC_ALL, "Turkish_Turkey")  # Veya "tr_TR"

# Şu anki tarihi alıyoruz
a = datetime.now()

# Ayın adını almak için "%B" formatını kullanıyoruz
tam_tarih = datetime.strftime(a, "%B")

# Türkçe ay adını ekrana yazdırıyoruz
print(tam_tarih)
