import imageio
import requests
import matplotlib.pyplot as plt
import IPython.display as dp

img="https://i.pinimg.com/originals/e2/05/4b/e2054b0c108f943fa58d98b8a4d37cd5.png"
dp.Image(requests.get(img).content)

source_img = imageio.imread(img)

import numpy as np

def grayscaleimg(rgb): 
  return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gryscl_img = grayscaleimg(source_img)

inv_img = (255 - gryscl_img)
plt.imshow(inv_img)

import scipy.ndimage
blurred_img = scipy.ndimage.filters.gaussian_filter(inv_img, sigma=5)
plt.imshow(blurred_img)
def dodging(blur_img, gryscl_img):
    resultant_dodge=blur_img*255/(255-gryscl_img) 
    resultant_dodge[resultant_dodge>255]=255
    resultant_dodge[gryscl_img==255]=255
    return resultant_dodge.astype('uint8')
target_img= dodging(blurred_img, gryscl_img)

import matplotlib.pyplot as plt
plt.imshow(target_img, cmap="gray")
plt.imsave('target_image.png', target_img, cmap='gray', vmin=0, vmax=255)

