from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("360x500")  # Pencere boyutunu ayarladık
        master.config(bg="#c0c0c0")  # Arka plan rengini gri olarak ayarladık
        master.resizable(False, False)
        
        # Giriş alanı
        self.equation = StringVar()
        self.entry_value = ""
        Entry(master, width=22, bg="#fff", font=("Arial", 24), textvariable=self.equation, bd=0).place(x=10, y=10)
        
        # Butonlar ve konumları
        button_size = 85  # Her bir butonun boyutu
        buttons = [
            ('(', 0, 70), (')', button_size, 70), ('%', 2 * button_size, 70), ('/', 3 * button_size, 70),
            ('1', 0, 70 + button_size), ('2', button_size, 70 + button_size), ('3', 2 * button_size, 70 + button_size), ('x', 3 * button_size, 70 + button_size),
            ('4', 0, 70 + 2 * button_size), ('5', button_size, 70 + 2 * button_size), ('6', 2 * button_size, 70 + 2 * button_size), ('-', 3 * button_size, 70 + 2 * button_size),
            ('7', 0, 70 + 3 * button_size), ('8', button_size, 70 + 3 * button_size), ('9', 2 * button_size, 70 + 3 * button_size), ('+', 3 * button_size, 70 + 3 * button_size),
            ('C', 0, 70 + 4 * button_size), ('0', button_size, 70 + 4 * button_size), ('.', 2 * button_size, 70 + 4 * button_size), ('=', 3 * button_size, 70 + 4 * button_size)
        ]

        # Butonları yerleştiriyoruz
        for (text, x, y) in buttons:
            if text == 'C':
                Button(master, width=9, height=3, text=text, relief="solid", bg="lightgray", 
                       command=self.clear, bd=1).place(x=x+5, y=y)
            elif text == '=':
                Button(master, width=9, height=3, text=text, relief="solid", bg="lightblue", 
                       command=self.solve, bd=1).place(x=x+5, y=y)
            elif text == 'x':
                Button(master, width=9, height=3, text=text, relief="solid", bg="white", 
                       command=lambda: self.show('*'), bd=1).place(x=x+5, y=y)
            else:
                Button(master, width=9, height=3, text=text, relief="solid", bg="white", 
                       command=lambda t=text: self.show(t), bd=1).place(x=x+5, y=y)

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
