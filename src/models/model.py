import torchmetrics
from torch import nn, optim
from model import *
from hyperparameters import *
import torch
from torchvision import datasets, transforms
from efficientnet_pytorch import EfficientNet
from torch import nn, optim
from pytorch_lightning import LightningModule


class EfficientNetModel(LightningModule):
    def __init__(self, num_classes, model_num=0):
        super().__init__()
        assert model_num >= 0 and model_num <= 7

        self.num_classes = num_classes

        self.accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=self.num_classes)
        #self.accuracy = torch.nn.ModuleDict({'precision' : torchmetrics.Precision()})

        # Load pre-trained model
        self.ef = EfficientNet.from_pretrained("efficientnet-b{}".format(model_num))
        features_size = [1280, 1280, 1408, 1536, 1792, 2048, 2304, 2560]

        # Override last layer for garbage classification
        self.ef._fc = nn.Sequential(
            nn.Linear(
                in_features=features_size[model_num], out_features=self.num_classes
            ),
            nn.LogSoftmax(dim=-1),
        )
        
        """
        # Freeze weights of the model except for the last layer
        for name, param in self.ef.named_parameters():
            if name.split(".")[-1] not in ["weight", "bias"]:
                param.requires_grad = False
        """

        # Set the requires_grad attribute of all layers except the last block and last layer to False
        for name, child in self.ef.named_children():
            if "_blocks.22" not in name and "_fc" not in name:
                for param in child.parameters():
                    param.requiresGrad = False

        """
        # Freeze the weights of the first layers
        for param in self.ef.parameters():
            param.requiresGrad = False

        # The last layer has different name than the previous layers
        for name, param in self.ef._fc.named_parameters():
            if name.split(".")[-1] in ["weight", "bias"]:
                param.requires_grad = True
        """

        # Define the data augmentation transforms
        self.data_augumentation = transforms.Compose(
            [
                transforms.RandomRotation(degrees=90),
                transforms.RandomAffine(degrees=0, translate=(0.2, 0.2), scale=(1, 1)),
                transforms.RandomHorizontalFlip(),
                transforms.RandomVerticalFlip(),
            ]
        )

        self.criterion = nn.NLLLoss()

    def forward(self, x):
        out = self.ef(x)
        return out

    def training_step(self, batch, batch_idx):
        x, y = batch
        x = self.data_augumentation(x)

        logits = self.forward(x)
        loss = self.criterion(logits, torch.flatten(y))

        preds = torch.argmax(logits, dim=1)
        acc = self.accuracy(preds, torch.flatten(y))

        self.log("train_loss", loss, on_step=True, on_epoch=True, logger=True)
        self.log("train_acc", acc, on_step=True, on_epoch=True, logger=True)

        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self.forward(x)
        loss = self.criterion(logits, torch.flatten(y))

        preds = torch.argmax(logits, dim=1)
        acc = self.accuracy(preds, torch.flatten(y))

        self.log("val_loss", loss, prog_bar=True)
        self.log("val_acc", acc, prog_bar=True)

        return loss

    def test_step(self, batch, batch_idx):
        x, y = batch
        logits = self.forward(x)
        loss = self.criterion(logits, torch.flatten(y))

        preds = torch.argmax(logits, dim=1)
        acc = self.accuracy(preds, torch.flatten(y))

        self.log("test_loss", loss, prog_bar=True)
        self.log("test_acc", acc, prog_bar=True)

        return loss

    def configure_optimizers(self):
        return optim.Adam(self.parameters())
