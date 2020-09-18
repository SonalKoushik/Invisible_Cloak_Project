import cv2

cp = cv2.VideoCapture(0)

while cp.isOpened():
    ret, back = cp.read()

    if ret:
        cv2.imshow("image", back)

        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('image.jpg', back)
            break


cp.release()
cv2.destroyAllWindows()

