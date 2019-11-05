#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:17:44 2019

@author: keiji2
"""

import cv2
import numpy as np
img_src1 = cv2.imread('back.png',1)
img_src2 = cv2.imread('front.png',1)

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgmask = fgbg.apply(img_src1)
fgmask = fgbg.apply(img_src2)

#cv2.imshow('frame',fgmask)
#
bg_diff_path = './diff.jpg'
cv2.imwrite(bg_diff_path,fgmask)
#
img_diff = cv2.imread('diff.jpg', cv2.IMREAD_GRAYSCALE)
whitePixels = np.count_nonzero(img_diff)
blackPixels = img_diff.size - whitePixels

#whitePixels = np.count_nonzero(fgmask)
#blackPixels = fgmask.size - whitePixels
print(whitePixels / blackPixels * 100)
#
#k = cv2.waitKey(0) & 0xFF
#if k == 27:
#    cv2.destroyAllWindows()
