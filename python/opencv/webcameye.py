import cv2
scale_factor = 1.2
min_neighbors = 3
min_size = (50, 50)
def detect():
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt.xml")
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors,minSize=min_size)
        if len(rects) >= 0:
            for (x, y, w, h) in rects:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imshow('Face Detection on Video', img)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break
    cap.release()
def main():
    detect()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
