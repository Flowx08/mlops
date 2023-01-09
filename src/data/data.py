import sys
sys.path.append('./src/models/')

import torch
import torchvision
import numpy as np
from pathlib import Path
from torch.utils.data import Dataset, DataLoader
from hyperparameters import *


class CorruptedMNIST(torch.utils.data.dataloader.Dataset):
    def __init__(self, path, train, transform=None):
        self.path = path
        if (train):
            self.file_names = list(Path(path).glob('train_*.npz'))
        else:
            self.file_names = list(Path(path).glob('test.npz'))
        self.size = 5000 * len(self.file_names)
        self.files = []
        for name in self.file_names:
            self.files.append(np.load(str(name)))
        self.transform = transform

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        fileid = int(item / 5000)
        tensor_id = item % 5000
        file = self.files[fileid]

        images = file['images']
        labels = file['labels']
        tensor = images[tensor_id]
        label = labels[tensor_id]

        torch_array = tensor
        if self.transform is not None:
            torch_array = self.transform(torch_array)

        torch_array = torch.tensor(torch_array, dtype=torch.float32)
        label = torch.tensor([label])
        return torch_array, label


def corrupted_mnist(batch_size):
    # exchange with the corrupted mnist dataset
    transforms = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize((0.5,), (0.5,)),
        ])
    train = CorruptedMNIST(path="./data/raw/corruptmnist/", transform=transforms, train=True)
    train_loader = DataLoader(train, batch_size=batch_size, shuffle=True)
    test = CorruptedMNIST(path="./data/raw/corruptmnist/", transform=transforms, train=False)
    test_loader = DataLoader(test, batch_size=batch_size, shuffle=True)
    return train_loader, test_loader

