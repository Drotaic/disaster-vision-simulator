import cv2
import numpy as np
import random

def flip_horizontal(image):
    return cv2.flip(image, 1)

def rotate_random(image):
    angle = random.uniform(-30, 30)
    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
    return cv2.warpAffine(image, M, (w, h))

def add_gaussian_noise(image):
    row, col, ch = image.shape
    mean = 0
    sigma = 15
    gauss = np.random.normal(mean, sigma, (row, col, ch)).reshape(row, col, ch)
    noisy = image + gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)

def gaussian_blur(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def brightness_contrast_shift(image):
    alpha = random.uniform(0.8, 1.2)
    beta = random.randint(-30, 30)
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

def random_crop(image, crop_size=0.8):
    h, w = image.shape[:2]
    ch, cw = int(h * crop_size), int(w * crop_size)
    y = random.randint(0, h - ch)
    x = random.randint(0, w - cw)
    return image[y:y+ch, x:x+cw]
