# 1. Kullanacağımız kütüphaneyi çalışmamıza dahil edelim.
import cv2   


# 2. Webcam'den veya harici bir kameradan görüntü almak için 0,1 gibi değerler yazarız. Webcam için bu değer '0' dır.
vid = cv2.VideoCapture(0)

# 3. Kullanacağımız cascade dosyasını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("...")

#4. Sonsuz bir döngü ile her kareyi(frame) tek tek inceleyelim.
while 1:
    
    # 5. Her kareyi tek tek okuyalım.
    ret, frame = vid.read()
    
    # 6. Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 7. Şimdi de cascade dosyamızı kullanarak her bir kare üzerindeki yüzlerin koordinarlarını bulalım.
    faces = face_cascade.detectMultiScale(gray, 1.4, 1)

    # 7. "faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    # 8. İşlediğimiz kareleri görelim.
    cv2.imshow('video',frame)

    # 9. Programı kapatacak kodu yazalım.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# 10. Son olarak videoyu serbest bırakalım.
vid.release()
cv2.destroyAllWindows()
