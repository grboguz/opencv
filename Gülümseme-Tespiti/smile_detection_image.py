import cv2


img = cv2.imread('...')

smile_cascade = cv2.CascadeClassifier('...')
face_cascade = cv2.CascadeClassifier('...')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    roi_gray = gray[x:x+w,y:y+h] 
    roi_img = img[x:x+w,y:y+h]

    smiles = smile_cascade.detectMultiScale(roi_gray,1.3,5)
    for (ex,ey,ew,eh) in smiles:
        cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()   
