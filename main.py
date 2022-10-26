# This is a sample Python script.
import cv2


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
    path = r'ressources\\000000.bmp'
    img = cv2.imread(path)
    cv2.imshow('image', img)
    cv2.waitKey(0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
