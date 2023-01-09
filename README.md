# MLOPS

OVERALL GOAL OF PROJECT:
- For this project, we want to create a drag-and-drop UI for a pre-trained image super-scaler, that allows the user to upload a low resolution image that will be super-scaled into a downloadable high-resolution version of the same image.

FRAMEWORK:
- Huggingface Transformers Repository
- Model 131. Swin2SR (PyTorch)
- Link to repo: https://huggingface.co/docs/transformers/main/model_doc/swin2sr?fbclid=IwAR2mjgms1a1nNWAweFZItsr6JqtLua0M3L3zD6Hi0KZAXLUuKIys9tu39ds

HOW WE INCLUDE THE FRAMEWORK IN THE PROJECT:
- The pre-trained model will probably do the work out of the box. We are thinking of ways that we could possibly optimise it for certain use cases, but are unsure what a sensible use-case could be. Are are unsure if it is a hard requirement that we do some kind of optimisation on the pre-trained model.

WHAT DATA WE ARE RUNNING IT ON:
- Any image, although possibly with some requirements vis-a-vis the minimum or maximum resolution.

WHAT DEEP LEARNING MODEL WE EXPECT TO USE:
- https://huggingface.co/docs/transformers/main/model_doc/swin2sr?fbclid=IwAR2mjgms1a1nNWAweFZItsr6JqtLua0M3L3zD6Hi0KZAXLUuKIys9tu39ds
