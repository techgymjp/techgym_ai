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
    'resources/logo_google.jpg')

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

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('sorrow: {}'.format(likelihood_name[face.sorrow_likelihood]))
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

def detect_logos(path):
    """画像からロゴを検出する"""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)


# detect_labels(file_name)
# detect_faces(file_name)
detect_logos(file_name)
