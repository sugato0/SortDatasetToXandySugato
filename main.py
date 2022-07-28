
import numpy as np
import glob
import cv2

def crop_res_img(image):

    coef: int
    crop_image: image
    #make square for picture

    if np.shape(image)[0] > np.shape(image)[1]:

        coef = np.shape(image)[0] - np.shape(image)[1]
        if coef % 2 != 0:
            coef -= 1
        #print(coef)
        crop_image = image[int(coef/2):int(np.shape(image)[0] - coef/2)]
    elif np.shape(image)[0] < np.shape(image)[1]:
        coef = np.shape(image)[1] - np.shape(image)[0]
        if coef % 2 != 0:
            coef -= 1
        #print(coef)
        crop_image = image[:, int(coef/2):int(np.shape(image)[1] - coef/2):]
    else:
        coef = 0
        crop_image = image

    #print(res_image)
    res_image = cv2.resize(crop_image,(28,28))
    return res_image

def img_preparation(image):
    img_res = crop_res_img(image)
    gray = cv2.cvtColor(img_res, cv2.COLOR_BGR2GRAY)

    # binary images by threshold
    th, gray_th = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # invert images (white-black to black-white)
    gray_inv = cv2.bitwise_not(gray_th)
    return gray_inv
#shuffle 2 arrays
def shuffle_in_unison(a, b):
    assert len(a) == len(b)
    shuffled_a = np.empty(np.shape(a)[0], dtype=type(a))
    shuffled_b = np.empty(np.shape(b)[0], dtype=type(b))
    permutation = np.random.permutation(len(a))
    for old_index, new_index in enumerate(permutation):
        shuffled_a[new_index] = a[old_index]
        shuffled_b[new_index] = b[old_index]
    return shuffled_a, shuffled_b
#open sourse with pictures
#https://drive.google.com/drive/folders/1pO3MfTe_tRljVeqcF1ERRB_0NZQwpXby?usp=sharing
files = glob.glob ("D:\data_sign_language_numbers\Sign Language for Numbers/*/*.jpg")


#read pictures with opencv
np_files = np.array([cv2.imread(file) for file in files])

X = []
y = []

j = 0
key = -1

for i in np_files:

    if i is None:
        continue
    #every 1500 change key
    if j % 1500 == 0:
        key+=1
    #append values and keys
    y.append(key)
    X.append(img_preparation(i))

    j+=1

X_shufled,y_shufled = shuffle_in_unison(X,y)
#print(X_shufled)
#print(y_shufled)

np.savez("X.npz",X)
np.savez("y.npz",y)










