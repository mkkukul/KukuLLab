from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("340x455")  # Pencere boyutunu küçülttük
        master.config(bg="#c0c0c0")  # Arka plan rengini gri olarak ayarladık
        master.resizable(False, False)
        
        # Giriş alanı
        self.equation = StringVar()
        self.entry_value = ""
        Entry(master, width=20, bg="#fff", font=("Arial", 24), textvariable=self.equation).place(x=10, y=10)
        
        # Butonlar ve konumları (daha yakın yerleştirilmiş)
        buttons = [
            ('(', 10, 70), (')', 85, 70), ('%', 160, 70), ('/', 235, 70),
            ('1', 10, 140), ('2', 85, 140), ('3', 160, 140), ('x', 235, 140),
            ('4', 10, 210), ('5', 85, 210), ('6', 160, 210), ('-', 235, 210),
            ('7', 10, 280), ('8', 85, 280), ('9', 160, 280), ('+', 235, 280),
            ('C', 10, 350), ('0', 85, 350), ('.', 160, 350), ('=', 235, 350)
        ]

        # Butonları yerleştiriyoruz
        for (text, x, y) in buttons:
            if text == 'C':
                Button(master, width=9, height=3, text=text, relief="flat", bg="lightgray", 
                       command=self.clear).place(x=x, y=y)
            elif text == '=':
                Button(master, width=9, height=3, text=text, relief="flat", bg="lightblue", 
                       command=self.solve).place(x=x, y=y)
            elif text == 'x':
                Button(master, width=9, height=3, text=text, relief="flat", bg="white", 
                       command=lambda: self.show('*')).place(x=x, y=y)
            else:
                Button(master, width=9, height=3, text=text, relief="flat", bg="white", 
                       command=lambda t=text: self.show(t)).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)
    
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)  # Sonuç üzerinden devam edebilmek için güncelleme
        except Exception:
            self.equation.set("Error")
            self.entry_value = ""

# Ana döngü
root = Tk()
Calculator(root)
root.mainloop()
