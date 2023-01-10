from transformers import AutoImageProcessor, AutoModelForObjectDetection
import torch
import click
from PIL import Image
import requests


@click.group()
def cli():
    pass


@click.command()
@click.argument("input_image")
def predict(input_image):
    print("Input image location: {}".format(input_image))

    image = Image.open(input_image)
    print(image.size)

    image_processor = AutoImageProcessor.from_pretrained("hustvl/yolos-tiny")
    model = AutoModelForObjectDetection.from_pretrained("hustvl/yolos-tiny")

    inputs = image_processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    # convert outputs (bounding boxes and class logits) to COCO API
    target_sizes = torch.tensor([image.size[::-1]])
    results = image_processor.post_process_object_detection(
        outputs, threshold=0.9, target_sizes=target_sizes
    )[0]

    for score, label, box in zip(
        results["scores"], results["labels"], results["boxes"]
    ):
        box = [round(i, 2) for i in box.tolist()]
        print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
        )


cli.add_command(predict)

if __name__ == "__main__":
    cli()
