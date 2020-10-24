# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 20:54:17 2020

@author: rchen
"""


from PIL import Image
import numpy as np
from IPython.display import display
import random


ima = Image.open(r"C:\Users\rchen\OneDrive\Documents\Caltech Soph\ee 55\\boat.tiff")

im = ima.load()
#im = np.array(ima)


for x in range(ima.size[0]):
    for j in range(ima.size[1]):
        if im[x,j] < 127:
            im[x,j] = (0)

        else:
            im[x,j] = (255)
    

    display(ima)
    
    