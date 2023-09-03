import os

# ---------------------------------------------------------------------------------------------------------------------

""" 1) Напишите функцию группового переименования файлов. Она должна:
1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
2. принимать параметр количество цифр в порядковом номере.
3. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
4. принимать параметр расширение конечного файла.
5. принимать диапазон сохраняемого оригинального имени.
Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""


# ---------------------------------------------------------------------------------------------------------------------


def group_renaming(directory, wanted_name, num_digits, initial_extension, final_extension, name_range=None):
    # Проверяем на существование каталога
    if not os.path.exists(directory):
        print('Такого каталога не существует')
        return
    # Пробегаемся по папке
    for filename in os.listdir(directory):
        # Если файл заканчивается на начальном расширении
        if filename.endswith(initial_extension):
            # То сплитуем файл и берем только имя файла
            base_name = os.path.splitext(filename)[0]

        if name_range:
            start, end = name_range
            if start < 0:
                start = 0
            if end > len(base_name):
                end = len(base_name)
            base_name = base_name[start:end]

        if base_name != '__init__':
            count = 1
            while os.path.exists(os.path.join(directory, f"{wanted_name}{count:0{num_digits}d}.{final_extension}")):
                count += 1

            new_filename = f"{wanted_name}{count:0{num_digits}d}.{final_extension}"

            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Переименован {filename} в {new_filename}")
        else:
            print(f"{filename} не будет переименован из-за __init__")

group_renaming('D:\\PycharmProjects\\rename_files', 'result_name', 2, 'ipynb', 'pptx', (3, 6))



# ---------------------------------------------------------------------------------------------------------------------

""" 2) Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами."""

# ---------------------------------------------------------------------------------------------------------------------

folder_path = 'D:\\PycharmProjects\\rename_files'

if not os.path.exists(folder_path):
    os.mkdir(folder_path)

file_name = '__init__.py'
file_path = os.path.join(folder_path, file_name)

code = """
def main():
    pass


if __name__ == '__main__':
    main()
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)
# ---------------------------------------------------------------------------------------------------------------------
