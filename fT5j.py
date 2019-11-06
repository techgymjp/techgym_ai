#AI-TECHGYM-1-8-A-1
#自然言語処理

from janome.tokenizer import Tokenizer
 
t = Tokenizer()
tokens = t.tokenize('すもももももももものうち')
 
for token in tokens:
    print(token)

