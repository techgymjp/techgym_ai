#AI-TECHGYM-1-11-A-1
#自然言語処理

#インポート
import urllib.request
import zipfile

# ファイル整形
import re

#ファイルダウンロード
url = 'https://www.aozora.gr.jp/cards/001847/files/57347_ruby_57225.zip'
zip = '57347_ruby_57225.zip'
urllib.request.urlretrieve(url, zip)

# ダウンロードしたzipの解凍
with zipfile.ZipFile(zip, 'r') as myzip:
    myzip.extractall()
    # 解凍後のファイルからデータ読み込み
    for myfile in myzip.infolist():
        # 解凍後ファイル名取得
        filename = myfile.filename
        # ファイルオープン時にencodingを指定してsjisの変換をする
        with open(filename, encoding='sjis') as file:
            text = file.read()

text = re.split('\-{5,}',text)[2]   # ヘッダ部分の除去
text = re.split('底本：',text)[0]   # フッタ部分の除去
text = text.replace('|', '')        # | の除去
text = re.sub('《.+?》', '', text)  # ルビの削除
text = re.sub('［＃.+?］', '',text) # 入力注の削除
text = re.sub('\n\n', '\n', text)   # 空行の削除
text = re.sub('\r', '', text)

outnum = 50
# 頭の100文字の表示 
print(text[:outnum])
print("…")
# 後ろの100文字の表示 
print(text[-outnum:])
