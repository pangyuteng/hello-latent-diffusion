
```
docker build -t torch-latent-diffusion .

docker run -it -u $(id -u):$(id -g) -w $PWD -v $PWD:$PWD torch-latent-diffusion bash

```