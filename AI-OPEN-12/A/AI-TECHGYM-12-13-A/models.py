import flaski.database
import flaski.dbmodels
import http.client, urllib.request, urllib.parse, urllib.error, base64
from google.cloud import automl

project_id = 'プロジェクトID'
model_id = 'モデルID'

# モデルAPIの呼び出し
def callAPI(uploadFile):
	# 予測用インスタンスの作成
	prediction_client = automl.PredictionServiceClient()
	model_full_id = automl.AutoMlClient.model_path(
		project_id,
		"us-central1",
		model_id
	)
	
	#ファイルオープン
	with open(uploadFile, "rb") as content_file:
		content = content_file.read()
	
	#ペイロード設定
	image = automl.Image(image_bytes=content)
	payload = automl.ExamplePayload(image=image)

	# 予測確率のしきい値（割合）
	params = {"score_threshold": "0.8"}
	
	#リクエスト生成
	request = automl.PredictRequest(
		name=model_full_id,
		payload=payload,
		params=params
	)

	#予測を実行する
	response = prediction_client.predict(request=request)

	#結果を格納する
	result = []
	for pred in response.payload:
		if len(get_flower_data(pred.display_name)) != 0:
			result.append(get_flower_data(pred.display_name))

	return result

# 花情報をDBから取得し辞書型で返す
def get_flower_data(flowername):
	ses = flaski.database.db_session()
	flower_master = flaski.dbmodels.FlowerMaster
	flower_data = ses.query(flower_master).filter(flower_master.flower_name == flowername).first()

	flower_data_dict = {}

	if not flower_data is None:
		flower_data_dict['flower_name'] = flower_data.flower_name
		flower_data_dict['wiki_url']        = flower_data.wiki_url
		flower_data_dict['picture_path']    = flower_data.picture_path
		flower_data_dict['copyright_owner'] = flower_data.copyright_owner
		flower_data_dict['copyright_url']   = flower_data.copyright_url

	return flower_data_dict
