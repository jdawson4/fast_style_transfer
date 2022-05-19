# Author: Jacob Dawson
# Adapting code from: https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2
# Example images from Wikimedia Commons:
# https://commons.wikimedia.org/wiki/File:Metro_Center_station,_DC.JPG
# https://commons.wikimedia.org/wiki/File:VanGogh-starry_night.jpg


import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

content_image_path = "metro_center.jpg" # make sure this points to the right photo!
style_image_path = "starry_night.jpg" # make sure this points to the right photo!

# Load content and style images (see example in the attached colab).
content_image = plt.imread("content_images/"+content_image_path)
style_image = plt.imread("style_images/"+style_image_path)

# Convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]. Example using numpy:
content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
content_image = tf.image.resize(content_image, (1000,1600))
style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.

# Optionally resize the images. It is recommended that the style image is about
# 256 pixels (this size was used when training the style transfer network).
# The content image can be any size.
style_image = tf.image.resize(style_image, (256, 256))

# Load image stylization module.
model = tf.keras.models.load_model("magenta_arbitrary_image_stylization")

# Stylize image.
outputs = model(tf.constant(content_image), tf.constant(style_image))
stylized_image = outputs[0]

# a simple and ugly way of displaying photos:
#plt.imshow(stylized_image.numpy()[0])
#plt.show()

# tensorflow processing???
stylized_image = tf.keras.utils.array_to_img(stylized_image[0])

# save to file:
tf.keras.preprocessing.image.save_img('stylized_images/'+content_image_path, stylized_image, scale=False)