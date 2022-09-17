import cv2
import numpy as np
from imutils.object_detection import non_max_suppression


def template_matching(img, tmp):
    ''' Template matching function, pass the image and the template'''

    (tH, tW) = tmp.shape[:2]  # unpack the dimensions of our template
    treshold = 0.8
    imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(
        imageGray, templateGray, cv2.TM_CCOEFF_NORMED)  # type numpy.ndarray
    # Found all of the coincidences according to our treshold
    (yCoords, xCoords) = np.where(result >= treshold)
    rects = []            # List of rectangles
    for (x, y) in zip(xCoords, yCoords):
        # Append all of the coincidences in the list
        rects.append((x, y, x + tW, y + tH))
    pick = non_max_suppression(np.array(rects))     # Non-Maxima Suppression
    print("[INFO] {} matched locations *after* NMS".format(len(pick)))
    for (startX, startY, endX, endY) in pick:      # loop over the final bounding boxes
        cv2.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 2)
    return img


if __name__ == "__main__":

    # image in the same directory
    img = cv2.imread("Template_matching_example.jpg")
    template = cv2.imread("Template.jpg")
    final_image = template_matching(img, template)
    cv2.imshow('Found Symbols', final_image)
    cv2.waitKey(0)
