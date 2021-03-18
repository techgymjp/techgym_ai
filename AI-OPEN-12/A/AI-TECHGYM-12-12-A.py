#techgym-12-12-A

#インポート
from google.cloud import automl

#モデル生成
prediction_client = automl.PredictionServiceClient()

#自分で作成したものを入れること
project_id = 'プロジェクトID'
model_id = 'モデルID'
file_path = "download.jpg"

# Get the full path of the model.
model_full_id = automl.AutoMlClient.model_path(
    project_id, "us-central1", model_id
)

# Read the file.
with open(file_path, "rb") as content_file:
    content = content_file.read()
    
image = automl.Image(image_bytes=content)
payload = automl.ExamplePayload(image=image)


# params is additional domain-specific parameters.
# score_threshold is used to filter the result
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictrequest
#閾値設定
params = {"score_threshold": "0.8"}

#リクエスト生成
request = automl.PredictRequest(
    name=model_full_id,
    payload=payload,
    params=params
)

#推論
response = prediction_client.predict(request=request)

#結果出力
print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.display_name))
    print("Predicted class score: {}".format(result.classification.score))

#インスタンス生成
client = automl.AutoMlClient()

#評価
print("List of model evaluations:")
for evaluation in client.list_model_evaluations(parent=model_full_id, filter=""):
    print("Model evaluation name: {}".format(evaluation.name))
    print(
        "Classification model evaluation metrics: {}".format(
            evaluation.classification_evaluation_metrics
        )
    )
