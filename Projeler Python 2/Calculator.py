from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("360x475")
        master.config(bg="#c0c0c0")  # Gri arka plan rengi
        master.resizable(False, False)
        
        # Giriş alanı
        self.equation = StringVar()
        self.entry_value = ""
        Entry(master, width=22, bg="#fff", font=("Arial", 24), textvariable=self.equation).place(x=10, y=10)
        
        # Butonlar ve konumları
        buttons = [
            ('(', 10, 70), (')', 95, 70), ('%', 180, 70), ('/', 265, 70),
            ('1', 10, 145), ('2', 95, 145), ('3', 180, 145), ('x', 265, 145),
            ('4', 10, 220), ('5', 95, 220), ('6', 180, 220), ('-', 265, 220),
            ('7', 10, 295), ('8', 95, 295), ('9', 180, 295), ('+', 265, 295),
            ('C', 10, 370), ('0', 95, 370), ('.', 180, 370), ('=', 265, 370)
        ]

        # Butonları yerleştiriyoruz
        for (text, x, y) in buttons:
            if text == 'C':
                Button(master, width=10, height=3, text=text, relief="flat", bg="lightgray", 
                       command=self.clear).place(x=x, y=y)
            elif text == '=':
                Button(master, width=10, height=3, text=text, relief="flat", bg="lightblue", 
                       command=self.solve).place(x=x, y=y)
            elif text == 'x':
                Button(master, width=10, height=3, text=text, relief="flat", bg="white", 
                       command=lambda: self.show('*')).place(x=x, y=y)
            else:
                Button(master, width=10, height=3, text=text, relief="flat", bg="white", 
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
