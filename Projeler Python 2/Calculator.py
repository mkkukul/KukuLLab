from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)
        
        # Giriş alanı
        self.equation = StringVar()
        self.entry_value = ""
        Entry(master, width=17, bg="#fff", font=("Arial Bold", 24), textvariable=self.equation).place(x=0, y=0)
        
        # Butonları yerleştiriyoruz
        buttons = [
            ('(', 10, 70), (')', 90, 70), ('%', 170, 70), ('/', 250, 70),
            ('1', 10, 140), ('2', 90, 140), ('3', 170, 140), ('x', 250, 140),
            ('4', 10, 210), ('5', 90, 210), ('6', 170, 210), ('-', 250, 210),
            ('7', 10, 280), ('8', 90, 280), ('9', 170, 280), ('+', 250, 280),
            ('C', 10, 350), ('0', 90, 350), ('.', 170, 350), ('=', 250, 350)
        ]

        # Butonların konumlarını ve işlevlerini tanımlıyoruz
        for (text, x, y) in buttons:
            if text == 'C':
                Button(master, width=11, height=4, text=text, relief="flat", bg="white", 
                       command=self.clear).place(x=x, y=y)
            elif text == '=':
                Button(master, width=11, height=4, text=text, relief="flat", bg="lightblue", 
                       command=self.solve).place(x=x, y=y)
            elif text == 'x':
                Button(master, width=11, height=4, text=text, relief="flat", bg="white", 
                       command=lambda: self.show('*')).place(x=x, y=y)
            else:
                Button(master, width=11, height=4, text=text, relief="flat", bg="white", 
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
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ""

# Ana döngü
root = Tk()
Calculator(root)
root.mainloop()
