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
    thresh1 = cv2.dilate(thresh1, np.ones((5, 5), np.uint8), iterations=1)
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
    mots = (pytesseract.image_to_string(tresholedimg,
                                        config='--psm 6 -l fra --oem 0 -c tessedit_char_whitelist=ABCDEFGHIJKL'
                                               'MNOPQRSTUVWXYZ'))
    mots = mots.replace(' ', '')
    results = []
    for line in mots.split('\n'): results.append(line.strip())
    results = list(filter(None, results))
    return results
    # return [str(result) for result in results if len(result) > 1]


def score_mot(letterlist, word, dico):
    score = 0
    lst = []
    if word in dico:
        word = [i.upper() for i in word]
        for letters in word:
            lst.append(letters)
        for i in lst:
            for j in letterlist:
                if i == j[0]:
                    score = score + j[1]
        return score
    return 0


def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)


def ajoutdesindicesencommun(list_n):
    listIndex = [[] for i in range(len(list_n))]
    listMot = []
    i = 0
    for j, k in enumerate(list_n):

        if len(k) == 1:
            listIndex[i].append(j)
            i -= 1
        i += 1

    listIndex = [x for x in listIndex if len(x) > 0]

    listIndexNew = [-1 for x in listIndex]

    for k, i in enumerate(listIndex):
        mot = ''
        for j in i:
            mot += list_n[j]
            if listIndexNew[k] == -1:
                listIndexNew[k] = j
        listMot.append(mot)

    k = 0
    p = 0
    nindexlist = []
    for i, j in zip(listIndexNew, listMot):
        nindexlist = nindexlist + [i - p]
        if list_n[i - p] != j:
            list_n[i - p] = j
            for u in range(1, len(listIndex[k])):
                list_n.remove(list_n[listIndex[k][u] - p])
                p += 1

        k += 1

    return list_n, nindexlist


def demand_letter_before(mot, listletters):
    while True:
        letter = input("Quelle est la premiere lettre de " + mot + '? (si aucune appuyez sur entrée)')
        letter = letter.upper()
        if letter in listletters or letter == '':
            break
    created_word = letter + mot
    return created_word


def demand_letter_after(mot, listletters):
    while True:
        letter = input("Quelle est la derniere lettre de " + mot + '? (si aucune appuyez sur entrée)')
        letter = letter.upper()
        if letter in listletters or letter == '':
            break
    created_word = mot + letter
    return created_word


def demand_letter_both(mot, listletters_av, listletters_ap):
    while True:
        letter_av = input("Quelle est la premiere lettre de " + mot + '? (si aucune appuyez sur entrée)')
        letter_av = letter_av.upper()
        if letter_av in listletters_av or letter_av == '':
            break
    while True:
        letter_ap = input("Quelle est la derniere lettre de " + letter_av + mot + '? (si aucune appuyez sur entrée)')
        letter_ap = letter_ap.upper()
        if letter_ap in listletters_ap or letter_ap == '':
            break
    created_word = letter_av + mot + letter_ap
    print(created_word)
    return created_word


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listLetters = [['A', 1], ['B', 3], ['C', 3], ['D', 2], ['E', 1], ['F', 4], ['G', 2], ['H', 4], ['I', 1], ['J', 8],
                   ['K', 5], ['L', 1], ['M', 3], ['N', 1], ['O', 1], ['P', 3], ['Q', 10], ['R', 1], ['S', 1], ['T', 1],
                   ['U', 1], ['V', 4], ['W', 4], ['X', 8], ['Y', 4], ['Z', 10]]
    scoreA = 0
    scoreB = 0
    nbTours = 0
    listWords = open(r"ressources\\ods6.txt").read().splitlines()
    previousList = []
    new = []
    for i in range(10, 17):
        nbTours += 1
        path = fr'ressources\\IMG_2_{str(i)}.jpg'
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        thresholdedImg = traitement_images(img)
        resultList = detection_mot(thresholdedImg)
        print("result: ", resultList)
        res, resIndex = ajoutdesindicesencommun(resultList)
        for i in resIndex:
            if i == 0:
                res[i] = demand_letter_after(res[i], res[i+1])
            elif i == len(res)-1:
                res[i] = demand_letter_before(res[i], res[i-1])
            else:
                res[i] = demand_letter_both(res[i], res[i-1], res[i+1])
        print(res)
        for j in res:
            score = score_mot(listLetters, j, listWords)
            print("mot: ", j, "score: ", score)
        if nbTours > 1:
            new = [ele for ele in res]
            for a in previousList:
                if a in res:
                    new.remove(a)
        previousList = res
        print(new, "new")
