# Drosou Maria
# Department of Informatics And Computer Engineering, University of West Attica
# e-mail: cs151046@uniwa.gr
# A.M.: 151046

import cv2
import numpy as np


def add_random_noise(image, rows, columns, channels):
    noisy = np.zeros((columns, rows, channels))
    for c in range(channels):
        for x in range(columns):
            for y in range(rows):
                noisy[x, y, c] = abs(round(image[x, y, c]
                                           + 0.05 * np.random.rand() * image[x, y, c]
                                           - 0.05 * np.random.rand() * image[x, y, c]))
    noisy = np.array(noisy, dtype='uint8')
    return noisy


def template_matching(image, image_h, image_w, template_img, template_h, template_w, info):
    image_bgr = np.copy(image)
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    # run the template matching
    res = cv2.matchTemplate(image_gray, template_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.64
    loc = np.where(res >= threshold)

    # mark the corresponding location(s)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image_bgr, pt, (pt[0] + template_w, pt[1] + template_h),
                      (0, 255, 255), 2)

    # and illustrate the results
    title = "Image " + info
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, image_bgr)
    cv2.resizeWindow(title, image_h, image_w)

    cv2.waitKey()


# load the image to check
img_rgb = cv2.imread('InputData/image.jpg')
width, height, num_of_channels = img_rgb.shape

# load the template image we look for
template = cv2.imread('InputData/template.jpg', 0)
w, h = template.shape[::-1]

np.random.seed(5)

# run template matching without blurring
for i in range(0, 5):
    information = str(i * 5) + "%" + " noise"
    template_matching(img_rgb, height, width, template, h, w, information)
    if i < 4:
        img_rgb = add_random_noise(img_rgb, height, width, num_of_channels)

# run template matching with blurring
for i in range(0, 5):
    img_blur = cv2.GaussianBlur(img_rgb, (5, 5), 0)
    information = str(i * 5) + "%" + " noise with blur"
    template_matching(img_blur, height, width, template, h, w, information)
    if i < 4:
        img_rgb = add_random_noise(img_rgb, height, width, num_of_channels)

cv2.destroyAllWindows()
