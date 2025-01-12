from fastapi import FastAPI, File, UploadFile
from typing import List
from PIL import Image
import io
from embeddings import get_embeddings

app = FastAPI()


@app.post("/embed")
def process_image(file: UploadFile = File(...)) -> List[List[float]]:
    image_data = file.file.read()
    image = Image.open(io.BytesIO(image_data))
    # ...process the image...
    result = get_embeddings(image)
    return result
