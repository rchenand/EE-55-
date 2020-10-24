# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:25:06 2020

@author: rchen
"""

from PIL import Image
from IPython.display import display
import random


ima = Image.open(r"C:\Users\rchen\OneDrive\Documents\Caltech Soph\ee 55\\boat.tiff")

im = ima.load()
#im = np.array(ima)


for x in range(ima.size[0]):
    for j in range(ima.size[1]):
        im[x,j] = int(im[x,j]) + random.normalvariate(0,50)

    display(ima)