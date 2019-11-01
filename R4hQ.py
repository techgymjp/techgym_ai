import io
import os

# Google Cloud client libraryをインポートする
from google.cloud import vision
from google.cloud.vision import types

# クライアントをインスタンス化する
client = vision.ImageAnnotatorClient()

# ファイル名を変更して画像を指定する
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources/face_surprise.jpg')

def detect_labels(path):
    """ファイル内のラベルを検出する"""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

def detect_faces(path):
    """画像から顔を検出する"""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

# detect_labels(file_name)
