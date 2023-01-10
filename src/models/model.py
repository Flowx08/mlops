from pytorch_lightning import LightningModule
import torchmetrics
from torch import nn, optim
from model import *
from hyperparameters import *
import torch


class FCModel(LightningModule):
    def __init__(self):
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(1, 10, 3, stride=2, padding=1),
            nn.LayerNorm([10, 14, 14]),
            nn.ReLU(),
            nn.Conv2d(10, 20, 3, stride=2, padding=1),
            nn.LayerNorm([20, 7, 7]),
            nn.ReLU(),
            nn.Conv2d(20, 40, 3, stride=2, padding=1),
            nn.LayerNorm([40, 4, 4]),
            nn.ReLU(),
        )
        self.fc = nn.Sequential(
            nn.Linear(40 * 4 * 4, hyperparameters.model_output_size),
            nn.LogSoftmax(dim=1),
        )
        self.criterion = nn.NLLLoss()

    def foreward(self, x):
        out = self.conv(x)
        out = out.view(-1, 40 * 4 * 4)
        out = self.fc(out)
        return out

    def training_step(self, batch, batch_idx):
        x, y = batch

        logits = self.foreward(x)
        loss = self.criterion(logits, torch.flatten(y))

        preds = torch.argmax(logits, dim=1)
        accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=10)
        acc = accuracy(preds, torch.flatten(y))

        self.log("train_loss", loss, on_step=True, on_epoch=True, logger=True)
        self.log("train_acc", acc, on_step=True, on_epoch=True, logger=True)

        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self.foreward(x)
        loss = self.criterion(logits, torch.flatten(y))

        preds = torch.argmax(logits, dim=1)
        accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=10)
        acc = accuracy(preds, torch.flatten(y))

        self.log("val_loss", loss, prog_bar=True)
        self.log("val_acc", acc, prog_bar=True)

        return loss

    def test_step(self, batch, batch_idx):
        x, y = batch
        logits = self.foreward(x)
        loss = self.criterion(logits, torch.flatten(y))

        preds = torch.argmax(logits, dim=1)
        accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=10)
        acc = accuracy(preds, torch.flatten(y))

        self.log("test_loss", loss, prog_bar=True)
        self.log("test_acc", acc, prog_bar=True)

        return loss

    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=hyperparameters.learningrate)
