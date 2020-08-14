# encoding: utf-8
# author:   AimerNeige
# github:   https://www.github.com/AimerNeige
# site:     https://AimerNeige.com

from PIL import Image
import os

# change these config
DOC_NAME    = 'Example'   # The name of the PDF file output.
COMIC_PATH  = 'comic/'    # The path of the comic saved.
SAVE_PATH   = 'output/'   # The path you wants to save the output file.
USE_ABSLUTE = False       # Weather using the abslute path.
PAGE_NUMBER = 3           # The number of the page of the comic.
NAME_BEFORE = 'example_'  # Text before the number of the commic picture file.
FILE_TYPE   = '.png'      # The file type of the comic picture.
FILL_NUMBER = 2           # The length of number (add 0 to match this number).



if not USE_ABSLUTE:
    DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + '/'
    COMIC_PATH = DIR_PATH + COMIC_PATH
    SAVE_PATH = DIR_PATH + SAVE_PATH


cover_path = COMIC_PATH + NAME_BEFORE + '1'.zfill(FILL_NUMBER) + FILE_TYPE
cover = Image.open(cover_path).convert('RGB')

comic_images_list = []

for i in range(2, PAGE_NUMBER + 1):
    comic_image_path = COMIC_PATH + NAME_BEFORE + str(i).zfill(FILL_NUMBER) + FILE_TYPE
    comic_image = Image.open(comic_image_path).convert('RGB')
    comic_images_list.append(comic_image)

pdf_file_path = SAVE_PATH + DOC_NAME + '.pdf'

cover.save(pdf_file_path, save_all=True, append_images=comic_images_list)
