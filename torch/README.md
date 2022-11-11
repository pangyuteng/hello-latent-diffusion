
```
# clone repos to /mnt
git@github.com:pangyuteng/hello-latent-diffusion.git
https://github.com/CompVis/latent-diffusion.git

# build pytorch container in this dir
# `requirement.txt` based on https://github.com/CompVis/latent-diffusion/blob/e66308c7f2e64cb581c6d27ab6fbeb846828253b/environment.yaml

docker build -t torch-latent-diffusion .
docker run --runtime=nvidia -it -w $PWD -v /mnt:/mnt torch-latent-diffusion bash

# cd to latent-diffusion repo and train

python main.py --base configs/latent-diffusion/ffhq-ldm-vq-4.yaml -t --gpus 0,1

```
