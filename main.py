# This is a sample Python script.
import cv2
import numpy as np
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def traitement_images(im):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    ret, thresh1 = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
    cv2.imshow('image', thresh1)
    cv2.waitKey(0)
    thresh1 = cv2.medianBlur(thresh1, 5)
    cv2.imshow('image', thresh1)
    cv2.waitKey(0)
    thresh1 = cv2.dilate(thresh1, np.ones((4, 4), np.uint8), iterations=1)
    cv2.imshow('image', thresh1)
    cv2.waitKey(0)
    thresh1 = cv2.erode(thresh1, np.ones((5, 5), np.uint8), iterations=1)
    cv2.imshow('image', thresh1)
    cv2.waitKey(0)
    width = int(thresh1.shape[1] * 50 / 100)
    height = int(thresh1.shape[0] * 50 / 100)
    dim = (width, height)
    thresh1 = cv2.resize(thresh1, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow('image', thresh1)
    cv2.waitKey(0)
    return thresh1


def detection_mot(tresholedimg):
    mots = (pytesseract.image_to_string(tresholedimg, config='--psm 11 -c tessedit_char_whitelist=ABCDEFGHIiJKL'
                                                             'MNOPQRSTUVWXYZ'))
    mots = mots.replace(' ', '')
    results = []
    for line in mots.split('\n'): results.append(line.strip())
    results = list(filter(None, results))
    return results
    # return [str(result) for result in results if len(result) > 1]


def score_mot(letterlist, word):
    score = 0
    lst = []
    word = [i.upper() for i in word]
    for letters in word:
        lst.append(letters)
    for i in lst:
        for j in letterlist:
            if i == j[0]:
                score = score + j[1]
    return score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listLetters = [['A', 1], ['B', 3], ['C', 3], ['D', 2], ['E', 1], ['F', 4], ['G', 2], ['H', 4], ['I', 1], ['J', 8],
                   ['K', 5], ['L', 1], ['M', 3], ['N', 1], ['O', 1], ['P', 3], ['Q', 10], ['R', 1], ['S', 1], ['T', 1],
                   ['U', 1], ['V', 4], ['W', 4], ['X', 8], ['Y', 4], ['Z', 10]]
    scoreA = 0
    scoreB = 0
    nbTours = 0
    listWords = open(r"ressources\\ods6.txt").read().splitlines()
    path = r'ressources\\IMG_5.jpg'
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    thresholdedImg = traitement_images(img)
    resultList = detection_mot(thresholdedImg)
    print(resultList)
    mot = str(resultList)

