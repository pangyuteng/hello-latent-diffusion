docker build -t torch-latent-diffusion .

docker run -it -u $(id -u):$(id -g) -v /radraid:/radraid torch-latent-diffusion bash
conda activate ldm