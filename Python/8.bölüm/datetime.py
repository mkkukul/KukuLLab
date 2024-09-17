# import datetime
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"Turkish_Turk.1254")

a = datetime.now()
# a = a.
tam_tarih = datetime.strptime(a,"%c")