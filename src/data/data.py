import sys

sys.path.append("./src/models/")

import torch
from torchvision import datasets, transforms
import numpy as np
from pathlib import Path
from torch.utils.data import Dataset, DataLoader
from hyperparameters import *
from efficientnet_pytorch import EfficientNet
from torch.utils.data import random_split

def garbage_dataset(batch_size, image_resize=224):
    # Load data
    transform = transforms.Compose([transforms.Resize([image_resize, image_resize]),
                                    transforms.ToTensor()])
    dataset = datasets.ImageFolder('./data/raw/garbage/', transform=transform)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Split the dataset into training and test sets
    train_size = int(0.8 * len(dataset))
    test_size = len(dataset) - train_size
    trainset, testset = random_split(dataset, [train_size, test_size])

    trainset_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True)
    testset_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=True)

    return trainset_loader, testset_loader
