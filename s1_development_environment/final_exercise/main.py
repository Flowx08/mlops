import argparse
import sys
import torch
import torch.nn as nn
import click

from data import mnist
from model import FCModel


@click.group()
def cli():
    pass


@click.command()
@click.option("--lr", default=1e-3, help='learning rate to use for training')
def train(lr):
    print("Training day and night")
    print(lr)

    model = FCModel()
    train_set, _ = mnist()
    
    criterion = nn.NLLLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    epochs = 2

    model.train()

    # Training loop
    for epoch in range(epochs):
        mean_loss = 0.0
        
        # Iterate over the train_set
        for it, (x, y) in enumerate(train_set):

            # Forward pass
            logits = model(x)
            loss = criterion(logits, y)
            mean_loss += loss;

            # Backward pass
            optimizer.zero_grad()
            loss.backward()

            # Update the model weights
            optimizer.step()

            if (it % 100 == 0):
                mean_loss /= 100
                print("Epoch {}, it {}, MeanLoss: {}".format(epoch, it, mean_loss))
                mean_loss = 0.0

        torch.save(model.state_dict(), 'model.pth')
        print("model saved!")




@click.command()
@click.argument("model_checkpoint")
def evaluate(model_checkpoint):
    print("Evaluating until hitting the ceiling")
    print(model_checkpoint)

    # TODO: Implement evaluation logic here
    model = FCModel()
    model.load_state_dict(torch.load(model_checkpoint))
    _, test_set = mnist()

    criterion = nn.NLLLoss()
    model.eval()

    total_correct = 0
    for it, (x, y) in enumerate(test_set):
        logits = model(x)
        loss = criterion(logits, y)
        total_correct += logits.argmax(dim=1).eq(y).sum().item()

    print("Accuracy: {}".format(total_correct / len(test_set)))


cli.add_command(train)
cli.add_command(evaluate)


if __name__ == "__main__":
    cli()


    
    
    
    
