import os
from PIL import Image
from typing import List


def collect_images_from_folders(folder_list: List[str]) -> list[Image]:
    """
        Собирает изображения из указанных папок.

        Аргументы:
        folder_list (list): Список путей к папкам, из которых нужно собрать изображения.

        Возвращает:
        list: Список объектов изображений (тип данных PIL.Image.Image), собранных из указанных папок.
        """
    images = []
    for folder_name in folder_list:
        if os.path.exists(folder_name):
            for filename in os.listdir(folder_name):
                if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                    img_path = os.path.join(folder_name, filename)
                    img = Image.open(img_path)
                    images.append(img)
        else:
            print(f"Папка {folder_name} не найдена.")
    return images


def save_images_as_tiff(images: list[Image], output_file: str) -> None:
    """
        Сохраняет изображения в формате TIFF.

        Аргументы:
        images (list): Список объектов изображений (тип данных PIL.Image.Image), которые нужно сохранить.
        output_file (str): Путь к файлу TIFF, в который нужно сохранить изображения.
    """
    if images:
        images[0].save(output_file, save_all=True, append_images=images[1:])
        print(f"Файл {output_file} успешно создан!")
    else:
        print("В указанных папках не найдено изображений.")


def collect_images_from_folders_in_directory(directory_path: str, folder_list: list[str]) -> list[Image]:
    """
        Собирает изображения из папок, перечисленных в определенной директории.

        Аргументы:
        directory_path (str): Путь к основной директории, в которой нужно искать папки.
        folder_list (list): Список имен папок, из которых нужно собрать изображения.

        Возвращает:
        list: Список объектов изображений (тип данных PIL.Image.Image), собранных из указанных папок.
    """
    images = []
    for folder_name in os.listdir(directory_path):
        if folder_name in folder_list:
            folder_path = os.path.join(directory_path, folder_name)
            images.extend(collect_images_from_folders([folder_path]))
    return images
