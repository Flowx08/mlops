import sys

sys.path.append("./src/data/")
sys.path.append("./src/models/")

from data import garbage_dataset
from hyperparameters import hyperparameters
import math
import torch


def test_corrupted_mnist():
    train, test = garbage_dataset(
        hyperparameters.batch_size, image_resize=hyperparameters.image_size
    )
    assert len(train) == 64
    assert len(test) == 16
    x, y = next(iter(train))
    assert x.shape == torch.Size(
        [
            hyperparameters.batch_size,
            3,
            hyperparameters.image_size,
            hyperparameters.image_size,
        ]
    )
    assert y.shape == torch.Size([hyperparameters.batch_size])
