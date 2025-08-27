import cv2
import os
import numpy as np


def binarize_image(image, threshold=128):
    alpha = 1.4
    beta = 20
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Переводим в оттенки серого
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # BGR, а не RGB!
    else:
        gray_image = image

    # Инвертированная бинаризация
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY_INV)

    # Морфологическая очистка от шума
    kernel = np.ones((3, 3), np.uint8)
    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

    return binary_image


def process_image_file(input_path, output_path, threshold=128):
    image = cv2.imread(input_path)
    if image is None:
        print(f"[Ошибка] Не удалось загрузить: {input_path}")
        return

    binary_image = binarize_image(image, threshold)
    cv2.imwrite(output_path, binary_image)
    print(f"[OK] Сохранено: {output_path}")

def binarize_images_in_directory(input_dir, output_dir, threshold=220):
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.heic', '.heif')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"[Создана папка] {output_dir}")

    files = os.listdir(input_dir)
    if not files:
        print(f"[Пусто] В папке {input_dir} нет файлов.")
        return

    for filename in files:
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_name = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_dir, output_name)

            print(f"[Обработка] {filename}")
            process_image_file(input_path, output_path, threshold)
        else:
            print(f"[Пропущено] {filename} — не поддерживается")

input_directory = r'input_dir/'
output_directory = r'output_dir/'

binarize_images_in_directory(input_directory, output_directory)