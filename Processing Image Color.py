#!/usr/bin/env python
# coding: utf-8

# In[24]:


from PIL import Image, ImageFilter
import os

def process_image(file_path: str) -> None:
    """
    Opens an image, applies various filters, and saves the processed images.

    Args:
    file_path (str): The path to the input image file.
    """
    try:
        path = "/path/to/your/directory"  # Define the path variable with the correct path
        with Image.open(file_path) as img:
            img.show()

            blur_img = img.filter(ImageFilter.BLUR)
            blur_img.show()

            gray_img = img.convert('L')
            gray_img.show()

            edge_img = img.filter(ImageFilter.FIND_EDGES)
            edge_img.show()
            edge_img.save("finaledit1.png")
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
    except PermissionError:
        print(f"Permission denied to access file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = os.path.join("C:\\Users\\USER\\Desktop\\Bored Banana.jfif")
process_image(file_path)




# In[ ]:




# In[ ]:




