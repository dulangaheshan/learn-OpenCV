#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2


# In[3]:


image = cv2.imread('./images/input.JPG')


# In[4]:


cv2.imshow("original",image)
cv2.waitKey()
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert to gray scale
cv2.imshow("gray",gray_image)
cv2.waitKey()


# In[4]:


#faster way
img = cv2.imread('./images/input.jpg',0)
cv2.imshow("gray",img)
cv2.waitKey(0)


# In[ ]:




