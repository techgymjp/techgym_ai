import io
import os

# Google Cloud client libraryをインポートする
from google.cloud import vision
from google.cloud.vision import types

# クライアントをインスタンス化する
client = vision.ImageAnnotatorClient()

def detect_labels(path):
    """ファイル内のラベルを検出する"""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations


