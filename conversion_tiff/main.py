from function import collect_images_from_folders_in_directory, save_images_as_tiff


def main():
    # путь к основной директории, в которой нужно искать папки для сбора изображений
    directory_path = 'G:\dir'
    folder_list = ['1369_12_Наклейки 3-D_3', '1388_2_Наклейки 3-D_1', '1388_6_Наклейки 3-D_2',
                   '1388_12_Наклейки 3-D_3']
    output_file = 'Result.tif'

    try:
        images = collect_images_from_folders_in_directory(directory_path, folder_list)
        save_images_as_tiff(images, output_file)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
