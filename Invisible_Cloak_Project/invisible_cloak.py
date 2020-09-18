import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('image.jpg')

kernel = np.ones((5,5),np.uint8)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)

        red = np.uint8 ([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

        l_red = np.array([155,25,0])
        u_red = np.array([179, 255, 255])

        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask", mask)

        part1 = cv2.bitwise_and(back, back, mask=mask)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=mask)

        final_img = part1+part2

        opening = cv2.morphologyEx(final_img, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        cv2.imshow("cloak", closing)

        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
