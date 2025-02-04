"""
    Utils responsible for any image resizing/adjusting.
"""

MAX_PAGE_WIDTH = 1800
MAX_PAGE_HEIGHT = 2700

def get_minimum_image_size(images):
    min_width = min(img.width for img in images)
    min_height = min(img.height for img in images)
    return min_width, min_height

def resize_images(images, min_width, min_height):
    resized_images = []
    for img in images:
        if img.width > min_width:
            img = img.resize((min_width, min_height))
        if img.width > MAX_PAGE_WIDTH:
            img = img.resize((MAX_PAGE_WIDTH, min_height))

        resized_images.append(img)
    return resized_images

