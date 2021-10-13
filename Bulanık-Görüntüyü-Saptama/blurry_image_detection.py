import cv2

img = cv2.imread("D:\\OpenCV\\test_images\\starwars.jpg")
blurry_img = cv2.medianBlur(img,9)

laplacian= cv2.Laplacian(blurry_img,cv2.CV_64F).var()
print(laplacian)

if laplacian < 500:
    print("blurry image")


cv2.imshow("img",img)
cv2.imshow("blurry_img",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

