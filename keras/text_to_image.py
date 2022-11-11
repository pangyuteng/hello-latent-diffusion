"""
Title: Generate an image from a text prompt using StableDiffusion
Author: fchollet
Date created: 2022/09/24
Last modified: 2022/09/24
Description: Use StableDiffusion to generate an image according to a short text description.
"""
import sys
import imageio
import cv2
import numpy as np
from PIL import Image

from keras_cv.models import StableDiffusion

input_image_file_path = sys.argv[1]
image = np.array(imageio.imread(input_image_file_path))
image = cv2.resize(image, (512, 512))

mask_shape = list(image.shape)
mask_shape[-1]=1
mask = np.ones(mask_shape)*0.2

print(image.shape)
print(mask.shape)
print(dir(StableDiffusion))

prompt = "FTX CEO Sam Bankman-Fried looking sad, closeup, portrait, watercolor"
model = StableDiffusion(img_height=512, img_width=512, jit_compile=True)
img = model.inpaint(
    prompt,
    image,
    mask,
    num_resamples=1,
    batch_size=1,
    num_steps=25,
    unconditional_guidance_scale=7.5)

Image.fromarray(img[0]).save("horse.png")
print("Saved at horse.png")


#context  = model.encode_text(prompt)
#print(context.shape)
#diffusion_noise = 

# model
#     def generate_image(
#         self,
#         encoded_text,
#         batch_size=1,
#         num_steps=25,
#         unconditional_guidance_scale=7.5,
#         diffusion_noise=None,
#         seed=None,
#     ):

