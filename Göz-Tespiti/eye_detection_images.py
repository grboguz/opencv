# 1. Kullanacağımız kütüphaneyi çalışmamıza dahil edelim.
import cv2   


# 2. Kullanacağımız videoyu çalışmamıza dahil edelim.
img = cv2.imread("...")

# 3. Kullanacağımız cascade dosyalarını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("...")
eye_cascade = cv2.CascadeClassifier("...")

# 6. Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
# 7. Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
faces = face_cascade.detectMultiScale(gray)

# 8. "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# 9. Şimdi de, bulduğum yüzler içinde göz arayacağım. 
gray2 = gray[y:y+h, x:x+w]
img2 = img[y:y+h, x:x+w]

# 10. eye cascade dosyasını kullanarak gözlerin koordinatlarını bulalım.
eyes = eye_cascade.detectMultiScale(gray2)

# 11. bu koordinatlara dikdörtgen çizelim.
for (ex,ey,ew,eh) in eyes:
	cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
         
# 12. İşlediğimiz resmi görelim.
cv2.imshow('image',img)

# 13. Programı kapatacak kodu yazalım.
cv2.waitKey(0)
cv2.destroyAllWindows()
