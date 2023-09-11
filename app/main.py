# app/main.py
from app import app
from flask import request, jsonify, send_file
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

@app.route('/detect', methods=['POST'])
def detect():
    try:
        url = request.json['image_url']
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        inputs = processor(images=img, return_tensors="pt")
        outputs = model(**inputs)

        # Let's only keep detections with score > 0.9
        target_sizes = torch.tensor([img.size[::-1]])
        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

        return jsonify(results)
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/detect_image', methods=['POST'])
def detect_image():
    try:
        url = request.json['image_url']
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        inputs = processor(images=img, return_tensors="pt")
        outputs = model(**inputs)

        # Let's only keep detections with score > 0.9
        target_sizes = torch.tensor([img.size[::-1]])
        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

        # Drawing bounding boxes and labels on the image
        draw = ImageDraw.Draw(img)
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            draw.rectangle(box, outline="red", width=3)
            draw.text((box[0], box[1]), f'{model.config.id2label[label.item()]}: {round(score.item(), 3)}', fill="red")

        # Save the image with detections to a BytesIO object and return it
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return send_file(img_byte_arr, mimetype='image/png')
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run()
