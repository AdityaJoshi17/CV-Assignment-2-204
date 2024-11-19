import cv2
import numpy as np

def translate(image, tx, ty):
    rows, cols = image.shape[:2]
    matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, matrix, (cols, rows))

def scale(image, fx, fy):
    return cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)

def rotate(image, angle):
    rows, cols = image.shape[:2]
    center = (cols // 2, rows // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, matrix, (cols, rows))

def shear(image, shx, shy):
    rows, cols = image.shape[:2]
    matrix = np.float32([[1, shx, 0], [shy, 1, 0]])
    return cv2.warpAffine(image, matrix, (cols + 100, rows + 100))

def apply_transformations(image_path):
    image = cv2.imread(image_path)
    outputs = {
        "translated": translate(image, 50, 50),
        "scaled": scale(image, 1.5, 1.5),
        "rotated": rotate(image, 45),
        "sheared": shear(image, 0.5, 0.5)
    }
    for key, transformed_image in outputs.items():
        cv2.imwrite(f'static/{key}.jpg', transformed_image)
    return outputs
