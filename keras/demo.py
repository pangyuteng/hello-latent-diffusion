

# tfds.image.Lsun

"""
+ implement latent diffusion "E.2.2 Inpainting"
For our experiments on image-inpainting in Sec. 4.5, we used the code of [88] to generate synthetic masks. We use a fixed
set of 2k validation and 30k testing samples from Places [108]. During training, we use random crops of size 256 × 256
and evaluate on crops of size 512 × 512. This follows the training and testing protocol in [88] and reproduces their reported
metrics (see † in Tab. 7). We include additional qualitative results of LDM-4, w/ attn in Fig. 21 and of LDM-4, w/o attn, big,
w/ ft in Fig. 22.
"""
