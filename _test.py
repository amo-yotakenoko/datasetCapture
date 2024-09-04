import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import patches
id="000000000049"
id="000000000077"




fig, ax = plt.subplots()
img = mpimg.imread(rf'images\train\{id}.jpg')
height, width = img.shape[:2] 
ax.imshow(img)
text=""
with open(rf'labels\train\{id}.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    # print(content)
for object in text.split("\n"):
    print(object)
    if object=="":
        continue


    keypoints = list(map(float, object.split()))
    x_center = keypoints[1] * width
    y_center = keypoints[2] * height
    rect_width = keypoints[3] * width
    rect_height = keypoints[4] * height
    ax.scatter(
    x_center ,  # 矩形の中心の x 座標
    y_center , # 矩形の中心の y 座標
    color='red',                # 星の色
    marker='*',                 # 星型マーカー
    s=100                        # マーカーサイズ
    )

    # Rectangle オブジェクトを作成
    rect = patches.Rectangle(
        xy=(x_center-rect_width/2, y_center-rect_height/2),  # 矩形の左下の座標
        width=rect_width,          # 矩形の幅
        height=rect_height,        # 矩形の高さ
        fill=False,                  # 塗りつぶしなし
        color='red',
    )
    ax.add_patch(rect)
    print(keypoints)
    i = 5 
    x = []
    y = []

    while i < len(keypoints)-1:
        print(f"{int(keypoints[i]*width)}\t{int(keypoints[i+1]*height)}\t{keypoints[i+2]}")
        x.append(keypoints[i]*width)
        i += 1
        y.append(keypoints[i]*height)
        i += 1
        i += 1
    ax.plot(x, y)
    ax.scatter(x, y)

    # プロットを作成

    # 画像を表示
plt.show()