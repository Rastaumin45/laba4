import numpy as np
import pickle

class Mass:
    def __init__(self, a, b):
        self.dlina = a
        self.massiv = b

    def slochenie(self):
        return [self.dlina + elem for elem in self.massiv]

    def vitchitanie(self):
        return [self.dlina - elem for elem in self.massiv]

    def umnochenie(self):
        return [self.dlina * elem for elem in self.massiv]

    def delenie(self):
        return [int(self.dlina / elem) if elem != 0 else "Деление на ноль" for elem in self.massiv]

def input_data():
    while True:
        try:
            a = float(input("Введите значение a: "))
            break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числовое значение для a.")

    while True:
        b_input = input("Введите элементы списка b через пробел: ")
        try:
            b = [float(x) for x in b_input.split()]
            if not b:
                raise ValueError
            break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числовые значения, разделенные пробелом.")

    return a, b

def save_to_text_file(filename, data):
    """Сохранение данных в текстовый файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)

def save_to_binary_file(filename, data):
    """Сохранение данных в бинарный файл."""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def read_from_binary_file(filename):
    """Чтение данных из бинарного файла."""
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    a, b = input_data()
    calc = Mass(a, b)

    # Результаты вычислений
    slochenie_result = calc.slochenie()
    vitchitanie_result = calc.vitchitanie()
    umnochenie_result = calc.umnochenie()
    delenie_result = calc.delenie()

    # Создаем текстовые выводы
    results_text = (
        f"Сложение: {slochenie_result}\n"
        f"Вычитание: {vitchitanie_result}\n"
        f"Умножение: {umnochenie_result}\n"
        f"Деление: {delenie_result}\n"
    )

    # Сохранение текстовых данных в файл
    save_to_text_file('results.txt', results_text)
    print("Результаты сохранены в файл 'results.txt'.")

    # Сохранение данных в бинарный файл
    results_data = {
        "Сложение": slochenie_result,
        "Вычитание": vitchitanie_result,
        "Умножение": umnochenie_result,
        "Деление": delenie_result
    }
    save_to_binary_file('results.bin', results_data)
    print("Результаты сохранены в бинарный файл 'results.bin'.")

    # Чтение из бинарного файла
    loaded_data = read_from_binary_file('results.bin')
    print("\nДанные, считанные из бинарного файла:")
    print(loaded_data)

if __name__ == "__main__":
    main()