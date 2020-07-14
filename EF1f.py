#techgym-10-1-Q



#画像データの読み込みと可視化

image_dir =
print("directory path:", image_dir)
print()

# フォルダ内のファイル名のリストを取得
image_files =

# 画像のファイル名を出力
print(image_files)
print()

# 画像の枚数を出力


image_path =
print("image path:", image_path)

# cv2を使い、画像を1枚読み込む
img =
print(type(img))

print(img)
print(img)

# BGRのまま可視化した場合とRGBに変換して可視化した場合の比較
plt.figure(figsize=(11,11))
plt.subplot(1,2,1)
plt.title("BGR")
plt.
plt.subplot(1,2,2)
plt.title("RGB")
# 「::-1」は反転の意味（BGRの反転がRGB）
plt.
plt.show()


image_path =
img = 

# BGRのまま可視化した場合とRGBに変換して可視化した場合の比較
plt.figure(figsize=(11,11))
plt.subplot(1,2,1)
plt.title("BGR")
plt.
plt.subplot(1,2,2)
plt.title("RGB")
# 「::-1」は反転の意味（BGRの反転がRGB）
plt.
plt.show()

