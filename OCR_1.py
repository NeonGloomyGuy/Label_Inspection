import cv2
import pytesseract
from pytesseract import Output

# path to the ocr engine
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def show_detected_words(data, img):
    '''Receives the data dictionary of the image and the image, puts rectangles
    in all the detected words and returns de image'''
    n = len(data["text"])  # number of words detected
    for i in range(n):
        if int(data["conf"][i]) > 60:
            (x, y, w, h) = (data["left"][i], data["top"]  # coordinates of each detected word
                            [i], data["width"][i], data["height"][i])
            # draw the rectangles in the image
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img = cv2.putText(img, data["text"][i],
                              (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)  # put the recognized word above each rect
    return img


def recognized_text(data):
    '''Stores and filters recognized words in a .txt file'''
    with open("Recognized Text.txt", "w+") as file:
        for text in data["text"]:
            if text != "":
                file.write(text + "\n")


if __name__ == "__main__":

    img = cv2.imread("Book 3.jpg")  # image in the same directory
    img_data = pytesseract.image_to_data(
        img, config=r"--oem 2 --psm 6",  output_type=Output.DICT)  # engine modes and page segmetation (still researching)
    recognized_text(img_data)
    img = show_detected_words(img_data, img)
    cv2.imshow("Recognized words in the image", img)  # show image
    cv2.waitKey(0)
