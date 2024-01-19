import cv2
import numpy as np
import random
from PIL import Image, ImageDraw


def cut_random_pattern_portion(pattern_path):
    # Open the pattern image
    pattern = Image.open(pattern_path)

    # Convert JPEG to RGBA if it's in a different mode
    pattern = pattern.convert("RGBA")

    # Get the size of the pattern image
    pattern_width, pattern_height = pattern.size

    # Randomly select the top-left corner for the 25x256 portion
    x_offset = random.randint(0, pattern_width - 256)
    y_offset = random.randint(0, pattern_height - 256)

    # Cut out the 25x256 portion
    pattern_portion = pattern.crop((x_offset, y_offset, x_offset + 256, y_offset + 256))

    return pattern_portion

def create_random_fading_patterned_circle_image(size):
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    radius = random.randint(20, 80)
    transition_length = random.randint(5, 20)*2+1

    pattern_path = "pattern.jpeg"
    cut_pattern = cut_random_pattern_portion(pattern_path).save("cut_pattern.png")
    src = cv2.imread('cut_pattern.png')
    mask = np.zeros_like(src)
    print(mask.shape)
    print(mask.dtype)
    cv2.circle(mask, (x, y), radius, (255, 255, 255), thickness=-1)
    mask_blur = cv2.GaussianBlur(mask, (transition_length, transition_length), 0)
    dst = src * (mask_blur / 255)

    return dst

def create_random_fading_white_circle_image(size):
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    radius = random.randint(20, 80)
    transition_length = random.randint(5, 20)*2+1

    pattern_path = "pattern.jpeg"
    cut_pattern = cut_random_pattern_portion(pattern_path).save("cut_pattern.png")
    src = cv2.imread('cut_pattern.png')
    mask = np.zeros_like(src)
    print(mask.shape)
    print(mask.dtype)
    cv2.circle(mask, (x, y), radius, (255, 255, 255), thickness=-1)
    mask_blur = cv2.GaussianBlur(mask, (transition_length, transition_length), 0)

    return mask_blur


# pattern_path = "pattern.jpeg"
#
# cut_pattern = cut_random_pattern_portion(pattern_path).save("cut_pattern.png")
# src = cv2.imread('cut_pattern.png')
# mask = np.zeros_like(src)
#
# print(mask.shape)
# # (225, 400, 3)
#
# print(mask.dtype)
# # uint8
# cv2.circle(mask, (200, 100), 50, (255, 255, 255), thickness=-1)
# cv2.fillConvexPoly(mask, np.array([[330, 50], [300, 200], [360, 150]]), (255, 255, 255))
# mask_blur = cv2.GaussianBlur(mask, (71, 71), 0)
#
# dst = src * (mask_blur / 255)


image_size = (256, 256)

# Number of images with random circles
num_images = 5

# Create and save multiple images
for image_index in range(num_images):
    dst = create_random_fading_patterned_circle_image(image_size)
    cv2.imwrite(f"./dataset/trainB/00{image_index + 1}.png", dst)
    white = create_random_fading_white_circle_image(image_size)
    cv2.imwrite(f"./dataset/trainA/00{image_index + 1}.png", white)

