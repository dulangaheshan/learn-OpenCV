import cv2 # import opencv
import numpy as np # import numpy

inputImage = cv2.imread('./images/input.jpg') # read image

cv2.imshow('Hello',inputImage) # show image 'hello = title of window'

# allow to input when image window is open
#blank = wait for anykey press 
#by placing number = specify a delay(except 0) 
cv2.waitKey(0)

cv2.destroyAllWindows() # close all open windows without this it may cause to crash the program


#shape function given by numpy 
#it help to discover the shapes of array
#inputImage saved as a array 
print(inputImage.shape)


# inputImage.shape[0] and inputImage.shape[1] and inputImage.shape[2] save height and width with pixels and RGB values


print('Height = ',int(inputImage.shape[0]))
print('Width = ',int(inputImage.shape[1]))
print('RGB = ',int(inputImage.shape[2]))


# save image('filename'+= .jpg/.png...etc)
cv2.imwrite('output.jpg',inputImage)
