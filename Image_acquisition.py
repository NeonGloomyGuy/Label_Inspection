'''Image_acquisition'''
import cv2
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
i = 0
j = 0

if not (cap.isOpened() and cap2.isOpened()):
    print("Could not open video device")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

while True:    
    # Capture frame-by-frame    
    ret, frame = cap.read()   
    ret2, frame2 = cap2.read() 

    cv2.imshow('TOP TEXT', frame)
    cv2.imshow('BOTTOM TEXT', frame2)
    
    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('s'):    
        cv2.imwrite("Camera 1 {}.jpg".format(i), frame)
        i = i + 1
    
    if cv2.waitKey(1) & 0xFF == ord('d'):    
        cv2.imwrite("Camera 2 {}.jpg".format(j), frame2)
        i = i + 1
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        cap.release()
        cv2.destroyAllWindows()
    
