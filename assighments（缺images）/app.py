import os
import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory
from preprocess_image import center_crop
from dinov2_numpy import Dinov2Numpy

app = Flask(__name__)

# --- 配置 ---
IMAGE_DIR = "gallery_images"
WEIGHT_PATH = "vit-dinov2-base.npz"
FEATURES_PATH = "gallery_features.npy"
NAMES_PATH = "gallery_names.npy"

# --- 初始化模型与数据 ---
print("正在加载 DINOv2 引擎，请稍候...")
raw_weights = np.load(WEIGHT_PATH, allow_pickle=True)
weights_dict = {k: raw_weights[k] for k in raw_weights.files}
model = Dinov2Numpy(weights_dict)

features_db = np.load(FEATURES_PATH)  # (N, 768)
names_db = np.load(NAMES_PATH)        # (N,)
norm_db = np.linalg.norm(features_db, axis=1) # 预计算模长加速

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_DIR, filename)

@app.route('/search', methods=['POST'])
def search_api():
    files = request.files.getlist('image')
    if not files:
        return jsonify({"error": "没有接收到图片"}), 400

    all_results = []
    for file in files:
        temp_path = f"temp_{file.filename}"
        file.save(temp_path)
        
        try:
            # 1. 提取特征
            query_tensor = center_crop(temp_path)
            query_feat = model(query_tensor).squeeze() # (768,)
            
            # 2. 余弦相似度计算 (矩阵运算)
            norm_q = np.linalg.norm(query_feat)
            similarities = np.dot(features_db, query_feat) / (norm_db * norm_q)
            
            # 3. 取前 10 名
            top10_idx = np.argsort(similarities)[-10:][::-1]
            matches = []
            for idx in top10_idx:
                matches.append({
                    "name": names_db[idx],
                    "score": float(similarities[idx])
                })
            
            all_results.append({
                "query_name": file.filename,
                "matches": matches
            })
        except Exception as e:
            print(f"处理 {file.filename} 出错: {e}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    return jsonify(all_results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)