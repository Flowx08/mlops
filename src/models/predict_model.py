import argparse
import sys
import torch
import torch.nn as nn
import click
import numpy as np

from model import EfficientNetModel
from hyperparameters import *
from PIL import Image


def predict_garbage(model_checkpoint, image_path):
    print("Evaluating until hitting the ceiling")
    print(model_checkpoint)

    model = EfficientNetModel(
        hyperparameters.num_classes, model_num=hyperparameters.efficientnet_num
    )
    model.load_state_dict(torch.load(model_checkpoint))
    model.eval()

    # Load the image
    img = Image.open(image_path)
    img = img.resize((hyperparameters.image_size, hyperparameters.image_size))
    img = np.array(img)
    img = torch.tensor(img)
    img = img.div(255)  # Normalize
    img = img.unsqueeze(0)
    img = img.permute(0, 3, 1, 2)
    print(img.shape)

    logits = model.forward(img)
    result = logits.argmax(dim=1)

    return int(result.item())
