import argparse
import sys
import torch
import torch.nn as nn
import click
from hyperparameters import *
import wandb

sys.path.append("./src/data/")
from data import garbage_dataset

from model import EfficientNetModel
from pytorch_lightning import Trainer
from pytorch_lightning.loggers import WandbLogger


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--config_file",
    default="./src/models/config.yaml",
    help="Config file path with hyperparameters",
)
def train(config_file):
    hyperparameters = OmegaConf.load(config_file)
    print("Training model...")
    print("Learning rate: {}".format(hyperparameters.learningrate))
    print("Batch size: {}".format(hyperparameters.batch_size))
    print("Model path: {}".format(hyperparameters.save_model_path))

    # Load dataset
    print("Loading dataset...")
    trainset, testset = garbage_dataset(
        hyperparameters.batch_size, image_resize=hyperparameters.image_size
    )
    print("Done")

    model = EfficientNetModel(
        hyperparameters.num_classes, model_num=hyperparameters.efficientnet_num
    )

    # Setup wandb
    print("Setup wandb...")
    wandb.init(project="garbage-recognition", entity="32b", name="EfficientNetModel")
    wandb.config = {
        "learning_rate": hyperparameters.learningrate,
        "epochs": hyperparameters.epochs,
        "batch_size": hyperparameters.batch_size,
    }
    wandb_logger = WandbLogger(name="EfficientNetModel")
    wandb_logger.watch(model)
    print("Done")

    # Train
    print("Training...")
    trainer = Trainer(default_root_dir=hyperparameters.save_model_path, logger=wandb_logger)
    trainer.fit(model, trainset, testset)
    print("Done")

    torch.save(model.state_dict(), hyperparameters.save_model_path + "model.pth")
    print("Model saved at {}".format(hyperparameters.save_model_path + "model.pth"))


@click.command()
@click.argument("model_checkpoint")
def evaluate(model_checkpoint):
    print("Evaluating until hitting the ceiling")
    print("Model checkpint path: {}".format(model_checkpoint))

    # Load dataset
    print("Loading dataset...")
    trainset, testset = garbage_dataset(
        hyperparameters.batch_size, image_resize=hyperparameters.image_size
    )
    print("Done")

    # Setup wandb
    print("Setup wandb...")
    wandb.init(project="garbage-recognition", entity="32b", name="EfficientNetModel")
    wandb.config = {
        "learning_rate": hyperparameters.learningrate,
        "epochs": hyperparameters.epochs,
        "batch_size": hyperparameters.batch_size,
    }
    wandb_logger = WandbLogger()
    print("Done")

    # Evaluate
    model = EfficientNetModel(
        hyperparameters.num_classes, model_num=hyperparameters.efficientnet_num
    )
    model.load_state_dict(torch.load(model_checkpoint))
    trainer = Trainer(logger=wandb_logger)
    trainer.test(model, testset)
    print("Done")


cli.add_command(train)
cli.add_command(evaluate)


if __name__ == "__main__":
    cli()
