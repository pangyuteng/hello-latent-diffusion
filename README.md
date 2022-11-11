###  keras-latent-diffusion

```
testing repo to see if its feasible to train
latent-diffusion with only a few gpus 

```
### notes

```
https://github.com/CompVis/latent-diffusion

nice clear schematic of model components:
https://raw.githubusercontent.com/CompVis/latent-diffusion/main/assets/modelfigure.png


x (image) --encoder--> z  (latent space)
z         --diffusion process--> z_t 
zt --(denoisng u-net with transformer)^--> z t-1
loop until -> z (t=0) --decoder--> x_hat

^ add tau_o to u-net for conditioning?

encoder: https://github.com/keras-team/keras-cv/blob/master/keras_cv/models/generative/stable_diffusion/image_encoder.py

decoder: https://github.com/keras-team/keras-cv/blob/master/keras_cv/models/generative/stable_diffusion/decoder.py

denoising-unet: https://github.com/keras-team/keras-cv/blob/master/keras_cv/models/generative/stable_diffusion/diffusion_model.py


training described in https://github.com/CompVis/latent-diffusion/blob/main/README.md

train encoder and decoder with loss?
using x -> encoder ->??? -> decoder -> x_hat



```

### ref 

```

OG / torch stable diffusion:
https://github.com/CompVis/latent-diffusion
https://github.com/CompVis/stable-diffusion

keras stable diffusion:
https://github.com/keras-team/keras-cv/tree/master/keras_cv/models/generative/stable_diffusion

nice examples:
https://keras.io/examples/generative/ddim

https://keras.io/examples/generative/vq_vae

https://keras.io/examples/generative/random_walks_with_stable_diffusion



```