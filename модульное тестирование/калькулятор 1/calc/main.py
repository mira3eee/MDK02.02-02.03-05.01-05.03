"""Графический интерфейс калькулятора на Tkinter."""

import tkinter as tk
from tkinter import ttk, messagebox

import calculator


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("390x390")
        self.root.resizable(False, False)
        self.memory = {"value": 0}

        tk.Label(root, text="Первое число:").place(x=20, y=20)
        self.first_entry = tk.Entry(root, width=25, font=("Arial", 12))
        self.first_entry.place(x=150, y=20)

        tk.Label(root, text="Второе число:").place(x=20, y=65)
        self.second_entry = tk.Entry(root, width=25, font=("Arial", 12))
        self.second_entry.place(x=150, y=65)

        tk.Label(root, text="Операция:").place(x=20, y=110)
        self.operation = ttk.Combobox(
            root,
            state="readonly",
            values=["Сложение (+)", "Вычитание (-)", "Умножение (*)",
                    "Деление (/)", "Степень (x^y)", "Корень (√x)",
                    "Факториал (x!)"],
            width=22
        )
        self.operation.current(0)
        self.operation.place(x=150, y=110)

        tk.Button(root, text="Вычислить", width=15, command=self.calculate).place(x=145, y=155)
        tk.Label(root, text="Результат:").place(x=20, y=210)
        self.result_entry = tk.Entry(root, width=25, font=("Arial", 12))
        self.result_entry.place(x=150, y=210)

        tk.Button(root, text="M: сохранить", width=12, command=self.save_memory).place(x=20, y=260)
        tk.Button(root, text="MR: прочитать", width=12, command=self.read_memory).place(x=145, y=260)
        tk.Button(root, text="M+: добавить", width=12, command=self.add_memory).place(x=270, y=260)
        tk.Button(root, text="MC: очистить", width=14, command=self.clear_memory).place(x=20, y=305)
        tk.Button(root, text="Очистить поля", width=14, command=self.clear_fields).place(x=150, y=305)
        tk.Button(root, text="Выход", width=12, command=root.destroy).place(x=280, y=305)

        self.memory_label = tk.Label(root, text="Память: 0")
        self.memory_label.place(x=150, y=350)

    def get_first(self):
        return float(self.first_entry.get().replace(",", "."))

    def calculate(self):
        try:
            a = self.get_first()
            operation = self.operation.get()
            if operation == "Сложение (+)":
                b = float(self.second_entry.get().replace(",", "."))
                result = calculator.add(a, b)
            elif operation == "Вычитание (-)":
                b = float(self.second_entry.get().replace(",", "."))
                result = calculator.subtract(a, b)
            elif operation == "Умножение (*)":
                b = float(self.second_entry.get().replace(",", "."))
                result = calculator.multiply(a, b)
            elif operation == "Деление (/)":
                b = float(self.second_entry.get().replace(",", "."))
                result = calculator.divide(a, b)
            elif operation == "Степень (x^y)":
                b = float(self.second_entry.get().replace(",", "."))
                result = calculator.power(a, b)
            elif operation == "Корень (√x)":
                result = calculator.square_root(a)
            else:
                result = calculator.factorial(a)

            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
        except ValueError as error:
            messagebox.showerror("Ошибка ввода или вычисления", str(error))
        except ZeroDivisionError as error:
            messagebox.showerror("Ошибка вычисления", str(error))

    def save_memory(self):
        try:
            calculator.memory_store(self.memory, float(self.result_entry.get()))
            self.update_memory_label()
        except ValueError:
            messagebox.showerror("Ошибка", "Сначала получите числовой результат.")

    def read_memory(self):
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, str(calculator.memory_read(self.memory)))

    def add_memory(self):
        try:
            calculator.memory_add(self.memory, float(self.result_entry.get()))
            self.update_memory_label()
        except ValueError:
            messagebox.showerror("Ошибка", "Сначала получите числовой результат.")

    def clear_memory(self):
        calculator.memory_clear(self.memory)
        self.update_memory_label()

    def update_memory_label(self):
        self.memory_label.config(text=f"Память: {calculator.memory_read(self.memory)}")

    def clear_fields(self):
        self.first_entry.delete(0, tk.END)
        self.second_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)


if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()
