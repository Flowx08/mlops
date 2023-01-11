import argparse
import sys
import torch
import torch.nn as nn
import click

from model import FCModel

@click.group()
def cli():
    pass

@click.command()
@click.argument("model_checkpoint")
@click.argument("datafile")
def predict(model_checkpoint, data):
    print("Evaluating until hitting the ceiling")
    print(model_checkpoint)

    # TODO: Implement evaluation logic here
    model = FCModel()
    model.load_state_dict(torch.load(model_checkpoint))
    _, test_set = mnist()

    model.eval()

    transform = (torchvision.transforms.Normalize((0.5,), (0.5,)),)
    x = torch.as_tensor(np.load(datafile))
    x = transform(x)

    logits = model(x)
    loss = criterion(logits, y)
    result = logits.argmax(dim=1)

    print("Result: {}".format(result))


cli.add_command(predict)

if __name__ == "__main__":
    cli()
