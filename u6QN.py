#AI-TECHGYM-1-8-A-4
#自然言語処理

from janome.tokenizer import Tokenizer

#形態素解析のオブジェクト
text = Tokenizer()

tokens = text.tokenize('すもももももももものうち', wakati=True)
print(tokens)

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()
 
#読み込んだデータを形態素解析
lines = txt.split("\r\n")
for i in lines:
    text_c = text.tokenize(i,wakati=True)   
    print(text_c)

print("\n")
