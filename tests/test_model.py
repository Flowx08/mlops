import sys

sys.path.append("./src/data/")
sys.path.append("./src/models/")

from model import FCModel
from hyperparameters import hyperparameters
import math
import torch


def test_model():
    x = torch.rand(1, 28, 28)
    model = FCModel()
    y = model.foreward(x)
    assert y.shape == torch.Size([1, 10])
