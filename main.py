# encoding: utf-8
# author:   AimerNeige
# github:   https://www.github.com/AimerNeige
# site:     https://AimerNeige.com

from PIL import Image
import os

# change these config
DOC_NAME = 'Example'  # The name of the PDF file output.
COMIC_PATH = 'comic/'  # The path of the comic saved.
SAVE_PATH = 'output/'  # The path you wants to save the output file.
USE_ABSOLUTE = False  # Weather using the absolute path.
NAME_BEFORE = 'example_'  # Text before the number of the comic picture file.
NAME_AFTER = ''  # Text after the number of the comic picture file.
START_NUMBER = 1  # start number
END_NUMBER = 3  # The number of the page of the comic.
FILL_NUMBER = 2  # The length of number (add 0 to match this number).
NEED_FILL = True  # if need to fill number 1 to 001
FILE_TYPE = '.png'  # The file type of the comic picture.


if not USE_ABSOLUTE:
    DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + '/'
    COMIC_PATH = DIR_PATH + COMIC_PATH
    SAVE_PATH = DIR_PATH + SAVE_PATH

cover_filled_number = str(START_NUMBER).zfill(
    FILL_NUMBER) if NEED_FILL else str(START_NUMBER)
cover_path = COMIC_PATH + NAME_BEFORE + \
    cover_filled_number + NAME_AFTER + FILE_TYPE
print("Solving", cover_path, START_NUMBER, "of", END_NUMBER)
cover = Image.open(cover_path).convert('RGB')

comic_images_list = []

for i in range(START_NUMBER + 1, END_NUMBER + 1):
    filled_number = str(i).zfill(FILL_NUMBER) if NEED_FILL else str(i)
    comic_image_path = COMIC_PATH + NAME_BEFORE + \
        filled_number + NAME_AFTER + FILE_TYPE
    print("Solving", comic_image_path, i, "of", END_NUMBER)
    try:
        comic_image = Image.open(comic_image_path).convert('RGB')
        comic_images_list.append(comic_image)
    except:
        print("\n", "Warning!", comic_image_path, "not exist", "\n")
        continue

pdf_file_path = SAVE_PATH + DOC_NAME + '.pdf'

print("Writing", pdf_file_path)
cover.save(pdf_file_path, save_all=True, append_images=comic_images_list)
