# MLOPS

Overall goal of the project:
- For this project, we want to create an application that detects and classifies objects in images, using the pre-trained YOLOS model. If required, we will fine-tune this model for a specific class of object or objects. Alternatively, we can evaluate the model performance on a dataset using some best-practice scoring metrics.

Framework:
- Huggingface Transformers Repository
- Model 168. YOLOS (PyTorch)
- Link to repo: https://huggingface.co/docs/transformers/model_doc/yolos

How we include the framework in the project:
- The pre-trained model will probably do the work out of the box. We are thinking of ways that we could possibly optimise it for certain use cases.

What data are we running it on:
- Any image, although possibly with some requirements vis-a-vis what objects are in the list of classifiable objects.

What deep learning model we expect to use:
- https://huggingface.co/docs/transformers/model_doc/yolos
