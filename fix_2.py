from PIL import Image

# 画像を開く
image = Image.open("appetite-g78de9cd27_1280.jpg")

# リサイズしたいサイズを指定
new_width = 600
new_height = 600

# アスペクト比を維持しながらリサイズ
image.thumbnail((new_width, new_height))

# リサイズした画像を保存
image.save("output19.jpg")
