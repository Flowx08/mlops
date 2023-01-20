---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

Group 32

### Question 2
> **Enter the study number for each member in the group**
>
> Answer:

*s202795, s212969, s133192*

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

We used the pre-trained EfficientNet B2 model from the list of PyTorch Image Models (https://arxiv.org/abs/1905.11946). We trained the last 2 layer of the EfficientNet B2 model on the task of garbage recognition, while freezing the parameters of the other layers. Using this framework allowed us to reach good classification accuracy (93% on 6 classes) with little training data (around 2000 images).

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
> Answer:

For meaning our dependencies we used python3 pip for managing the required packages and DVC for the data dependencies.
We put all the packages required for the code in a 'requirements.txt' file and the DVC dependencies files in data.dvc and models.dvc.
A new team member would just need to do the following to get started:
- Clone the project's repository onto their local machine.
- Create a virtual environment using python 3.x
- Activate the virtual environment.
- Install the dependencies listed in the project's requirements or package file using 'pip install -r requirements.txt'.
- Pull the data from Google drive by running 'dvc pull'.

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
> Answer:

We used the cookie cutter template and we filled out every folder except the folder 'references' which was not required since it was a small project and we did not need any reading material to share.
The final structure of our repository is the following:
- Data: here we store all the dataset images + other data required for testing. This folder is created and populated after running 'dvc pull'.
- Models: here we store all the trained models parameters. This folder is created and populated after running 'dvc pull'.
- Notebooks: here we store 2 jupyter notebooks, one used for preliminaty testing of the framework and another one to train contains code to train the model using google collab, by fetching out git repository and running the appropriate scripts.
- requirements.txt: In this file we store all the python3 pip packages needed to run our code and tests.
- Scripts: where we store all the utility scripts for building docker, running the code, formatting the style ecc
- src: the source code for training and deployment
- tests: unit testing
- app.dockerfile: dockerfile for deployment
- train.dockerfile: dockerfile for training

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
> Answer:

We used the Black framework to format our python code in the ./src/ and ./tests/ folders.
These concepts are important in larger projects because they help to ensure consistency and readability in the codebase. Consistent code formatting and naming conventions make it easier for developers to understand and navigate the code, which can improve productivity and reduce errors.


## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement?**
>
> Answer:

We implemented 2 tests: one for testing the loading the dataset and the other one for testing the  loading of the model and the feedforeward pass.

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> **Answer length: 100-200 words.**
> Answer:

Our code coverage was 76%. Interestingly most source code files had a coverage of 100% except for src/models/model.py which has a coverage of 56% since we haven't tested all the 
model methods.
Even if the code coverage was 100% that would not guarantee that the code is error-free. For example, it is possible for a test suite to be written poorly and not cover all possible scenarios, even if all lines of code are executed. Additionally, 100% code coverage does not take into account other factors such as proper handling of edge cases, security vulnerabilities, and performance issues.

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Answer:

Because we did the vast majority of the work on this project while sitting together, we did not use pull requests at all, and only used branches very little. Our use of branches was mostly just for the sake of the exercise, since we are a 3 person who who mostly sat together. We organized the branches in 'main' branch and 'dev' branch. The idea was to push our commit to the dev branch and only merge the dev branch with the main branch when we were sure that the code was working properly.

Branches and pull requests can improve version control because they reduce the risk of code conflicts and errors. This is because each branch is a separate copy of the codebase, which allows developers to make changes without affecting the main codebase. This allows developers to experiment with new features, fix bugs, or refactor code without affecting the main codebase. Once the changes have been tested and are ready to be merged back into the main codebase, a developer creates a pull request. A pull request is a request for other developers to review and approve the changes made on a branch. Other developers can review the code, comment on it, and suggest changes. This allows teams to catch and fix issues before they're merged into the main codebase. Once the changes are approved, the pull request can be merged into the main codebase. This ensures that only stable, well-reviewed changes are added to the main codebase, which helps to maintain the overall stability and quality of the codebase.

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Answer:

Yes, we did use DVC for managing the data in our project. It mostly helped us to share the data between us, since datasets are typically too large to be stored on a Git repository. In particular we used it to share the content of the ./data/ folder (containinig the dataset) and the ./models/ folder (containing the trained models parameters).

In addition to this, DVC is very useful when needing to reproduce experiment, as it can track and store both inputs, dependencies and parameters, and due to its cache system, each team member can selectively access the parts of the data which are needed, instead of having to download the whole thing.

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
> Answer:

--- question 11 fill here ---
TODO

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
> Answer:

We used hydra to store all the hyperparameters for each experiment. When we wanted to run an experiment we would pass the filepath of the config.yaml that we wanted to use, to the training script as  follows:
```
python3 ./src/models/train_models.py train --config_file=./src/models/config.yaml
```

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
> Answer:

Since we used yaml config files to store the experiment parameters and used hydra to load those parameters, reproducing experiments was straightforeward: when reproducing a particular experiment we would pass the appropriate config file path to the python script and all the correct hyperparameters would be used for the training (as explained in the previous answer).

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
> Answer:

> [Screenshot 1](figures/wandb_screenshot_1.png)
> [Screenshot 2](figures/wandb_screenshot_2.png)
The pictures included show graphs from our logs in weight and bias. In particular we decided to monitor the loss and accuracy on the trainingset and testingset while training.  These metrics are important because they provide a way to evaluate the performance of a model, and help to identify areas where the model can be improved. Additionally, they can be used to compare different models and select the best one for a given task. In particular the loss it's usefull to see if the training is going well. Over time we expect the loss to keep going down if the neural network is converging to a solution. The accuracy on the testset is useful to see the generalization capabilities of the model and to compare it to other trained models in order to choose which one to use for the deployment phase.

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
> Answer:

In our project we made 2 different docker images: one for training the model and one for deploying it with fastapi. The first docker images is created using the config file train.dockerfile
in our repository while the other one is created using the app.dockerfile. We made some bash script to easily build and run the docker images. We build the image by running ./scripts/docker_app_build.sh and we execute the image by using the script ./scripts/docker_app_run.sh.

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
> Answer:

Since our code base was small we did not perform any debudding and most errors could be easily fixed given the python error logs messages. We did use the python debugger (pdb) as exercise on the code and it showed that the code was working as intended.

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
> Answer:

We used the following GCP services:
- Compute Engine: A service that allows users to create and manage virtual machines on the cloud, with various options for configuring CPU, memory, storage, and networking. The service also offers features such as autoscaling, load balancing, snapshots, Preemptible VMs, and Custom Machine Types to help manage and optimize the usage of resources.
- Container Registry: It is a fully-managed, scalable, and secure service that can be used to store, manage and distribute Docker images.
- Cloud Run: This service is a fully-managed serverless platform for deploying and scaling containerized applications on Google Cloud. It allows for automatic scaling, security, and monitoring of stateless containers with support for a wide range of languages and frameworks, and integration with other Google Cloud services.

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 50-100 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

--- question 18 fill here ---
TODO

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

--- question 19 fill here ---

### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:

--- question 20 fill here ---
TODO

### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

--- question 21 fill here ---
TODO

### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> Answer:

We made a REST api to access our model using fastAPI in python. We also made a small web page to send request to the REST api and we served also the web page through fastAPI as a static file. We deployed the app fist locally by running our deployment code with uvicorn http server inside a docker container. We invoced our deployted service using 'docker run' which in turn has uvicorn as entry point that runs our fastapi code. We the deployed the app on the cloud using Google cloud. To do that we send the app image to the container registry and than we executed it with Cloud run service.

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

--- question 23 fill here ---

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:

--- question 24 fill here ---

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
> *
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

[Our System diagram](figures/mlops.png).
Our system has 2 main actors: the developer and the user.
The developer is able to train the model and test the deployment by pulling the git repository on his machine and running the appropiate docker image for either training or local deployment of the model. The docker container downloads the datasets and the models using DVC, and runs the appropriate code. Weight and Bias is used to monitor the training process.
The developer can use a script to upload the latest docker image on the Google Container registry to use for cloud deployment. Finally the developer can use Google Run to deploy the image to the cloud so that it is available to be used publicly by any user.
The user can access the app using a browser. A webpage sends http request to our app
and the results are returned and displayed to the user.


### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

--- question 26 fill here ---

### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:

--- question 27 fill here ---
