FROM tensorflow/tensorflow:2.10.0-gpu-jupyter

WORKDIR /opt
COPY requirements.txt .
RUN pip install -r requirements.txt

# "Unimplemented: DNN library is not found https://github.com/google/jax/issues/4920"
RUN pip uninstall jax && pip install jax[cuda]