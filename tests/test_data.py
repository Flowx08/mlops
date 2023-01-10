import sys

sys.path.append("./src/data/")
sys.path.append("./src/models/")

from data import corrupted_mnist
from hyperparameters import hyperparameters
import math
import torch


def test_corrupted_mnist():
    train, test = corrupted_mnist(hyperparameters.batch_size)
    assert len(train) == math.ceil(25000 / hyperparameters.batch_size)
    assert len(test) == math.ceil(5000 / hyperparameters.batch_size)
    x, y = next(iter(train))
    assert x.shape == torch.Size([hyperparameters.batch_size, 1, 28, 28])
    assert y.shape == torch.Size([hyperparameters.batch_size, 1])
