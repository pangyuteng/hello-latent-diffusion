FROM continuumio/miniconda3

RUN apt-get update && apt-get install git curl vim wget -yq

WORKDIR /opt
RUN git clone https://github.com/CompVis/latent-diffusion.git

WORKDIR /opt/latent-diffusion
RUN conda env create -f environment.yaml

# Make RUN commands use the new environment:
RUN echo "conda activate ldm" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

