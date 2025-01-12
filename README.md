# Resnet50 embeddings container

This is a simple container to get the embeddings of an image using a resnet50 model. The model is loaded from an onnx file from this project: https://huggingface.co/jxtc/resnet-50-embeddings and published on https://hub.docker.com/r/jmservera/resnet50-embeddings


## Local run

To run this file locally you need to download the embeddings onnx file with:

```bash
curl -L https://huggingface.co/jxtc/resnet-50-embeddings/resolve/main/resnet50_embeddings.onnx -o resnet50_embeddings.onnx
```

Then copy some jpeg images inside the folder and run:

```bash
python test.py
```

## Build and run the container

To build the container run:

```bash
docker build -t resnet50-embeddings .
```

And to run the container:

```bash
docker run -p 8000:8000 resnet50-embeddings
```

You can change the port using the `UVICORN_PORT` environment variable.

Once the container is running you can test the container with something like this:

```bash
curl -F "file=@./island.jpeg" http://localhost:8000/embed
```

Or use some code like this:

```python
import requests

url = "http://localhost:8000/embed"
files = {'file': open('image.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```