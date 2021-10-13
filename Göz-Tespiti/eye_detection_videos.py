# 1. Kullanacağımız kütüphaneyi çalışmamıza dahil edelim.
import cv2   


# 2. Kullanacağımız videoyu çalışmamıza dahil edelim.
vid = cv2.VideoCapture("...")

# 3. Kullanacağımız cascade dosyalarını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("...")
eye_cascade = cv2.CascadeClassifier("...")

#4. Sonsuz bir döngü ile her kareyi(frame) tek tek inceleyelim.
while 1:
    # 5. Her kareyi tek tek okuyalım.
    ret, frame = vid.read()
    frame = cv2.resize(frame,(480,360))
    
    # 6. Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 7. Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
    faces = face_cascade.detectMultiScale(gray)

    # 7. "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    # Şimdi de, bulduğum yüzler içinde göz arayacağım.
    roi_gray = gray[y:y+h, x:x+w]
    roi_frame = frame[y:y+h, x:x+w]

    # eye cascade dosyasını kullanarak gözlerin koordinatlarını bulalım.
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # bu koordinatlara dikdörtgen çizelim.
    for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
         
    # 8. İşlediğimiz kareleri görelim.
    cv2.imshow('video',frame)

    # 9. Programı kapatacak kodu yazalım.
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 10. Son olarak videoyu serbest bırakalım.
vid.release()
cv2.destroyAllWindows()
