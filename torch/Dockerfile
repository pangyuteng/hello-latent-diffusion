FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-runtime
RUN apt-get update && apt-get install git curl vim wget -yq

WORKDIR /opt
COPY requirements.txt .
RUN pip install -r requirements.txt

