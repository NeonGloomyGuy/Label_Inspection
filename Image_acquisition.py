'''Image_acquisition'''
import cv2
cap = cv2.VideoCapture(0)
i = 0

if not (cap.isOpened()):
    print("Could not open video device")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:    
    # Capture frame-by-frame    
    ret, frame = cap.read()    

    cv2.imshow('TOP TEXT', frame)
    
    #Waits for a user input to quit the application    
    if cv2.waitKey(1) & 0xFF == ord('s'):    
        cv2.imwrite("ET {}.jpg".format(i), frame)
        i = i + 1
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
cap.release()
cv2.destroyAllWindows()