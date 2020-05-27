import cv2 as cv
import numpy as np
from scipy.ndimage.filters import median_filter

def show(final):
    print('display')
  #  cv.imshow('Temple', final)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Insert any filename with path
img = cv.imread('1.jpg')

def white_balance_loops(img):
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
    return result

def laplacian_contrast_weight(image):
    return cv.Laplacian(image, cv.CV_64F) 


def custom_white_balance(img):
    red_ch = np.average(img[:,:,2])
    green_ch = np.average(img[:,:,1])
    blue_ch = np.average(img[:,:,0])
    img1 = img.copy()
    img1[:,:,2] = img[:,:,2]+(0.005*((green_ch-red_ch)*(1-(img[:,:,2]*img[:,:,1]))))
    img1[:,:,0] = img[:,:,0]+(0.005*((green_ch-blue_ch)*(1-(img[:,:,1]*img[:,:,0]))))
    return img1

def unsharp_masking(image):
    gaussian_3 = cv.GaussianBlur(image, (9,9), 100.0)
    unsharp_image = cv.addWeighted(image, 1.5, gaussian_3, -0.5, 0, image)
    
    # Calculate the sharpened image
    return unsharp_image

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")
  
    # apply gamma correction using the lookup table
    return cv.LUT(image, table)

final =  white_balance_loops(img)
show(final)
cv.imwrite('result4.jpg', custom_white_balance(final))
cv.imwrite('result5.jpg', unsharp_masking(custom_white_balance(final)))
cv.imwrite('result6.jpg', adjust_gamma(custom_white_balance(final),0.8))
#cv.imwrite('result7.jpg', laplacian_contrast_weight(unsharp_masking(custom_white_balance(final))))

b = img.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = img.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = img.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0
# cv.imwrite('b.jpg', b)
# cv.imwrite('g.jpg', g)
# cv.imwrite('r.jpg', r)

