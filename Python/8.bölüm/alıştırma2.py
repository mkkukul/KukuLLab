import subprocess as sp
# subprocess.call("notepad.exe") notpad
# subprocess.call("C:\Program Files\Microsoft Office\Office16\EXCEL.EXE")

while True:
    seçim_yap = input("1-Notepad\n2-Excel\n3-Google\n4-Hesap Makinesi\n")
    if seçim_yap == "1":
        sp.call("notepad.exe")
    elif seçim_yap == "2":
        sp.call("C:\Program Files\Microsoft Office\Office16\EXCEL.EXE")
    elif seçim_yap == "3":
        sp.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    elif seçim_yap == "4":
        sp.call("calc.exe")
        