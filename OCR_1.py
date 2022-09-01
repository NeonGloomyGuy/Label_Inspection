import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def show_detected_words(data, img):
    n = len(data["text"])
    for i in range(n):
        if int(data["conf"][i]) > 80:
            (x, y, w, h) = (data["left"][i], data["top"]
                            [i], data["width"][i], data["height"][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img = cv2.putText(img, data["text"][i],
                              (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    return img


def recognized_text(data):
    with open("Recognized Text.txt", "w+") as file:
        for text in data["text"]:
            if text != "":
                file.write(text + "\n")


if __name__ == "__main__":

    img = cv2.imread("Book 3.jpg")
    img_data = pytesseract.image_to_data(
        img, config=r"--oem 1 --psm 12",  output_type=Output.DICT)
    recognized_text(img_data)
    img = show_detected_words(img_data, img)
    cv2.imshow("Recognized words in the image", img)
    cv2.waitKey(0)
