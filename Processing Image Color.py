#!/usr/bin/env python
# coding: utf-8

# In[24]:


from PIL import Image, ImageFilter
import sys

img = Image.open("C:\\Users\\hp\\Downloads\\download.jpg")
img.show()

blur_img = img.filter(ImageFilter.BLUR)
blur_img.show()

gray_img = img.convert('L')
gray_img.show()

edge_img = img.filter(ImageFilter.FIND_EDGES)
edge_img.show()
edge_img = edge_img.save("finaledit1.png")



#techdevscommunity
#@techie_devs


# In[ ]:





# In[ ]:




