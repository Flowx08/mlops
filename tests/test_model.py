import sys
sys.path.append('./src/data/')
sys.path.append('./src/models/')

from model import EfficientNetModel
from hyperparameters import hyperparameters
import math
import torch

def test_model():
    x = torch.rand(1, 3, hyperparameters.image_size, hyperparameters.image_size)
    model = EfficientNetModel(hyperparameters.num_classes, hyperparameters.efficientnet_num)
    y = model.foreward(x)
    assert(y.shape == torch.Size([1, hyperparameters.num_classes]))

