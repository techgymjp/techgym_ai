#AI-TECHGYM-1-11-A-2
#自然言語処理

#インポート
import urllib.request
import zipfile

#ファイル整形
import re

#Janome
from janome.tokenizer import Tokenizer

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

#インスタンスの生成 
t = Tokenizer()

#対象の品詞
obj_list = ['名詞', '動詞','形容詞']

# テキストを引数として、形態素解析の結果で対象のみを配列で抽出する関数を定義 
def extract_words(s):
    tokens = t.tokenize(s)
    r = [token.base_form for token in tokens if token.part_of_speech.split(',')[0] in obj_list]
    return r

# 全体のテキストを句点('。')で区切った配列
sentences = text.split('。')

# それぞれの文章を単語リストに変換(処理に数分かかります)
word_list = [extract_words(sentence) for sentence in sentences]

#一部を確認 
for word in word_list[0:3]:
    print(word)
