# MLOPS

Overall goal of the project:
- For this project, we have created an application that classifies images of different types of trash into different categories.
Since the dataset we are using has little date (about 2000 images) we use an EfficientNet model (pre-trained on the ImageNet dataset)
as starting point of our training to avoid overfitting and to improve generalization.

Framework:
- PyTorch Image Models
- EfficientNet B2

How we include the framework in the project:
- We import the pre-trained parameters using the efficientnet_pytorch package and use these as starting point of our training.

What data are we running it on:
- We are using the images from the garbage classification dataset from: https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification

