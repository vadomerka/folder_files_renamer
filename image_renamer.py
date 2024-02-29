import os

"""
Программа переименовывает все файлы в папке по порядку создания. 
Сортировка по порядку создания происходит только внутри одной папки.
Ввод: путь к верхней папке.
"""


def image_renamer(path, files_to_rename):
    """
    Метод сортирует все файлы внутри папки по дате создания, и переименовывает,
    используя общий индекс файлов.
    :param path: путь к папке.
    :param files_to_rename: список всех файлов внутри этой папки.
    :return: ничего
    """
    # Индекс файлов. Увеличивается от количества переименнованных файлов.
    global file_index
    # Оставляем только существующие файлы.
    files_to_rename_filtered = []
    for file in files_to_rename:
        old_file_name = os.path.join(path, file)
        if os.path.isfile(old_file_name):
            files_to_rename_filtered.append(old_file_name)
    # Сортируем файлы по времени создания внутри папки.
    files_to_rename_sorted = sorted(files_to_rename_filtered,
                                    key=lambda x: os.path.getmtime(x), reverse=True)
    # Переименовываем файлы с помощью индекса.
    for old_file_name in files_to_rename_sorted:
        new_file_name = os.path.join(path, "op_" + str(file_index) + ".png")
        os.rename(old_file_name, new_file_name)
        file_index += 1
    return


print("Введите путь к папке для переименования.")
original_folder_name = input()
file_index = 1
# Перебираем все дерево файлов.
for folder_data in [x for x in os.walk(original_folder_name)]:
    base_folder, sub_folders, files = folder_data
    image_renamer(base_folder, files)

