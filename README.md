# VisionHub: AI-Powered Image Search Engine

**VisionHub** 是一款基于 Meta AI 的 **DINOv2** 自监督视觉模型开发的高性能图像检索系统。它能够对万级规模（13.5k+）的底库进行毫秒级深度语义搜索，并提供沉浸式的响应式 Web 交互界面。

## 🌟 核心特性 (Key Features)

* **深度语义索引**：利用 DINOv2 (ViT-Base) 提取 768 维特征向量，超越传统像素比对，实现理解图像内容的语义搜索。
* **工业级鲁棒性**：
* **断点续传**：支持万级数据提取过程中意外中断后的秒级恢复。
* **自动清洗**：内置异常拦截机制，自动过滤并记录损坏或格式异常的图片。


* **极致搜索体验**：
* **批量拖拽**：支持全页面 Drag & Drop 拦截，一次性上传并检索多张图片。
* **响应式布局**：基于 Tailwind CSS 打造，适配多端设备。
* **沉浸式预览**：集成 Lightbox 毛玻璃灯箱效果，支持置信度分数显示与一键下载。


## 🛠️ 技术栈 (Tech Stack)

* **Core Model**: DINOv2 (ViT-B/14)
* **Backend**: Python, Flask, NumPy (Vector Optimization)
* **Frontend**: JavaScript ES6+, Tailwind CSS, HTML5 Drag & Drop API
* **Database**: NPY (Binary Vector Storage)

## 🚀 快速开始 (Quick Start)

### 1. 环境准备

```bash
git clone https://github.com/YourUsername/VisionHub.git
cd VisionHub
pip install -r requirements.txt

```

### 2. 构建特征索引

将图片放入指定目录后运行提取脚本。该脚本具备 **Checkpoint** 保护机制，每处理 10 张图自动存档：

```bash
python build_gallery.py

```

### 3. 启动应用

```bash
python app.py

```

访问 `http://127.0.0.1:5000` 即可开始检索。

## 📊 性能表现 (Performance)

在实验环境下对 13,503 张图片进行测试：

* **特征提取偏移量 (Diff)**：保持在 0.03-0.04 极低区间，聚类极度稳定。
* **检索响应时间**：基于 NumPy 矩阵点积运算，单次查询耗时 < 500ms。

## 📂 项目结构 (Project Structure)


## 📝 许可证 (License)

本项目遵循 MIT 协议。

---
