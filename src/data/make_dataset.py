# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import torch
import torchvision
import numpy as np
from pathlib import Path

class CorruptedMNISTLoader(torch.utils.data.dataloader.Dataset):
    def __init__(self, path, train, transform=None):
        self.path = path
        if train:
            self.file_names = list(Path(path).glob("train_*.npz"))
        else:
            self.file_names = list(Path(path).glob("test.npz"))
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

        images = file["images"]
        labels = file["labels"]
        tensor = images[tensor_id]
        label = labels[tensor_id]

        torch_array = tensor
        if self.transform is not None:
            torch_array = self.transform(torch_array)

        torch_array = torch.tensor(torch_array, dtype=torch.float32)
        label = torch.tensor([label])
        return torch_array, label


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    raw_path = "./data/raw/"
    processed_path = "./data/processed/"
    
    # exchange with the corrupted mnist dataset
    transforms = torchvision.transforms.Compose(
        [
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize((0.5,), (0.5,)),
        ]
    )
    logger.info('loading trainingset...')
    train = CorruptedMNISTLoader(
        path=(raw_path + "corruptmnist/"), transform=transforms, train=True
    )
    logger.info('done')
    logger.info('loading testingset...')
    test = CorruptedMNISTLoader(
        path=(raw_path + "corruptmnist/"), transform=transforms, train=False
    )
    logger.info('done')

    logger.info('Prepricessing trainining set...')
    train_x = []
    train_y = []
    for i, (x, y) in enumerate(train):
        train_x.append(x)
        train_y.append(y)
        if i % 200 == 0:
            print("{}%".format((i / len(train)) * 100))
    torch.save(train_x, processed_path + 'train_x.pt')
    torch.save(train_y, processed_path + 'train_y.pt')
    logger.info('done')
    
    logger.info('Prepricessing testing set...')
    test_x = []
    test_y = []
    for i, (x, y) in enumerate(test):
        test_x.append(x)
        test_y.append(y)
        if i % 200 == 0:
            print("{}%".format( (i / len(test)) * 100))
    torch.save(test_x, processed_path + 'test_x.pt')
    torch.save(test_y, processed_path + 'test_y.pt')
    logger.info('done')



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
