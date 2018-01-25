from PIL import Image
import pyocr
import pyocr.builders
import cv2
import os
import shutil

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]

langs = tool.get_available_languages()
lang = langs[0]

def img_to_str(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp = 'temp'+path[-4:]
    cv2.imwrite(temp, gray)
    img = Image.open(temp)
    txt = tool.image_to_string(
        img,
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    word_boxes = tool.image_to_string(
        img,
        lang="eng",
        builder=pyocr.builders.WordBoxBuilder()
    )
    line_and_word_boxes = tool.image_to_string(
        Image.open('test.png'), 
        lang="eng",
        builder=pyocr.builders.LineBoxBuilder()
    )
    os.remove(temp)
    return txt, word_boxes, line_and_word_boxes
