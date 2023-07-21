from PIL import Image

# 画像を開く
image = Image.open("broccoli-gbe09760b5_1280.jpg")

# リサイズしたいサイズを指定
new_width = 600
new_height = 600

# アスペクト比を維持しながらリサイズ
width, height = image.size
aspect_ratio = width / height

if aspect_ratio > 1:
    new_height = int(new_width / aspect_ratio)
else:
    new_width = int(new_height * aspect_ratio)

resized_image = image.resize((new_width, new_height))

# リサイズした画像を保存
resized_image.save("output24.jpg")
