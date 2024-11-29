import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# パスの設定
image_folder = "./images/train"
label_folder = "./labels/train"

# カスタムカラーマップ
colors = plt.cm.hsv(np.linspace(0, 1, 18)).tolist()

# 画像とラベルの読み込み
def visualize_pose(image_path, label_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # ラベルファイルの読み込み
    if os.path.exists(label_path):
        with open(label_path, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            data = line.strip().split()
            keypoints_data = data[5:]  # クラスIDを除外
            
            # 不完全なデータのチェック
            if len(keypoints_data) % 3 != 0:
                print(f"警告: {label_path} のデータ数が不正です{keypoints_data}。スキップします。")
                continue  # データ不整合の場合はスキップ
            
            # キーポイントを3要素ずつ処理
            keypoints = np.array(keypoints_data, dtype=np.float32).reshape(-1, 3)
            for i, point in enumerate(keypoints):
                x, y, conf = point
                if conf > 0.5:  # 信頼度が高い場合のみ描画
                    x = int(x * image.shape[1])
                    y = int(y * image.shape[0])
                    plt.scatter(x, y, color=colors[i % len(colors)], s=20)
    
    # 画像表示
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# すべての画像を順番に表示
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
for image_file in image_files[:5]:  # 最初の5枚のみ表示
    image_path = os.path.join(image_folder, image_file)
    label_path = os.path.join(label_folder, image_file.replace('.jpg', '.txt').replace('.png', '.txt'))
    visualize_pose(image_path, label_path)
