from PIL import Image

# 画像を開く
image = Image.open("eggplant-gfa258d0e9_1280.jpg")

# 解像度を指定してリサイズ
new_size = (600, 600)  # 新しい解像度を指定
resized_image = image.resize(new_size)

# リサイズした画像を保存
resized_image.save("output38.jpg")
