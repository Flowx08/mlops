# MLOPS

Overall goal of the project:
- For this project, we want to create an application that classifies images of trash into different categories.
Since the dataset used has little date (about 2000 images) we use an EfficientNet model pre-trained on ImageNet dataset
as starting point of our training to avoid overfitting and improve generalization.

Framework:
- PyTorch Image Models
- EfficientNet B2

How we include the framework in the project:
- We import the pre-trained parameters using the efficientnet_pytorch package and we use them as starting point of our training.

What data are we running it on:
- We are going to use images from the garbage classification dataset from: https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification

