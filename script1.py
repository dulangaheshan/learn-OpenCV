import cv2

img = cv2.imread("3.1 galaxy.jpg.jpg",0)

print(type(img))
print(img)
cv2.imshow("galaxy",img)
#img = img.T
resized_image = cv2.resize(img,(1000,500))
cv2.imshow("galaxy2",resized_image)
cv2.waitKey(0)