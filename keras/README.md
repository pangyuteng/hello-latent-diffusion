

###

```
docker build -t keras-latent-diffusion .

docker run -it -u $(id -u):$(id -g) -w $PWD -v $PWD:$PWD --runtime=nvidia keras-latent-diffusion bash

```