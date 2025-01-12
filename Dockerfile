FROM python:3.12.8-bullseye
#torchvision needs python >=3.8, <=3.12

WORKDIR /app

# download resnet50 embeddings model
ADD https://huggingface.co/jxtc/resnet-50-embeddings/resolve/main/resnet50_embeddings.onnx /app/resnet50_embeddings.onnx

COPY src/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src/*.py .

ENV UVICORN_PORT=8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
