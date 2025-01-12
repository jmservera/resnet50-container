import onnxruntime
from PIL import ImageFile
from typing import List
from torchvision import transforms


def load_and_preprocess_image(img: ImageFile):
    # Define the same preprocessing as used in training
    preprocess = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
                                 0.229, 0.224, 0.225]),
        ]
    )

    # Preprocess the image
    img_preprocessed = preprocess(img)

    # Add batch dimension
    return img_preprocessed.unsqueeze(0).numpy()


def get_embeddings(img: ImageFile) -> List[List[float]]:
    # Load and preprocess an image (replace with your image path)
    input_data = load_and_preprocess_image(img)

    # Run inference
    outputs = session.run(None, {input_name: input_data})

    # The output should be a single tensor (the embeddings)
    embeddings = outputs[0]

    # Flatten the embeddings
    embeddings = embeddings.reshape(embeddings.shape[0], -1)

    return embeddings


onnx_model_path = "resnet50_embeddings.onnx"


# Use GPU (CUDA) if available
# session = ort.InferenceSession(model_path, providers=['CUDAExecutionProvider'])

# Alternatively, use CPU
# session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])

session = onnxruntime.InferenceSession(
    onnx_model_path)

input_name = session.get_inputs()[0].name
