# This is a sample Python script.
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listLetters = [['A', 1], ['B', 3], ['C', 3], ['D', 2], ['E', 1], ['F', 4], ['G', 2], ['H', 4], ['I', 1], ['J', 8],
                   ['K', 5], ['L', 1], ['M', 3], ['N', 1], ['O', 1], ['P', 3], ['Q', 10], ['R', 1], ['S', 1], ['T', 1],
                   ['U', 1], ['V', 4], ['W', 4], ['X', 8], ['Y', 4], ['Z', 10]]
    listWords = open(r"ressources\\ods6.txt").read().splitlines()
    print_hi('PyCharm')
    path = r'ressources\\scrabbletest.png'
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    ret, thresh1 = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
    cv2.imshow('image', thresh1)
    cv2.waitKey(0)
    thresh1 = cv2.medianBlur(thresh1, 5)
    cv2.imshow('image', thresh1)
    cv2.waitKey(0)
    thresh1 = cv2.dilate(thresh1, np.ones((3, 3), np.uint8), iterations=1)
    cv2.imshow('image', thresh1)
    cv2.waitKey(0)
    mots = (pytesseract.image_to_string(thresh1, config='--psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKL'
                                                        'MNOPQRSTUVWXYZ'))
    mots = mots.replace(' ', '')
    print(mots)
