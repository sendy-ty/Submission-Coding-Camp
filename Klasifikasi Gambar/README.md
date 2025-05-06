# 🐾 Image Classification with TensorFlow: Model Training &amp; Deployment Formats

## 📌 Project Summary

This project is part of the [Dicoding course: Belajar Pengembangan Machine Learning](https://www.dicoding.com/academies/185/corridor). It demonstrates the process of building an image classifier using TensorFlow, followed by converting the trained model into multiple formats suitable for deployment:

* **SavedModel** — used for server-based inference
* **TFLite** — optimized for mobile and embedded devices
* **TFJS** — for use directly in web browsers

---

## 📁 Dataset Overview

The dataset used in this project is [animals-10](https://www.kaggle.com/datasets/alessiocorrado99/animals10), which contains approximately **28,000 Images** across **10 animal categories**:

* **Original Classes**: Cat, Dog, Horse, Cow, Chicken, Butterfly, Spider, Elephant, Sheep, Squirrel
* **Source**: Collected from Google Images and manually verified
* **condition**: Raw dataset with varying resolutions and some noisy labels to simulate real-world conditions
* **Images per Class**: Between 2,000–5,000 images per category

For this project:

* only **3 randomly selected categories** were used for model simplicity
* Dataset was **augmented** to balance the number of images per class
* Final dataset was split into **80% Training** and **20% testing**

---

## 🏗️ Model Architecture

The classification model was built using TensorFlow's Keras API, employing the **MobileNetV2** architecture as a base (with ImageNet pretrained weights). The final layers include:

* Convolutional and Global Average Pooling layers
* Dropout and Batch Normalization for regularization
* Dense (fully connected) layers with softmax output

---

## ⚙️ Training Details

The model was trained using the following configuration:

* **image size**: 224 × 224 × 3 (RGB)
* **Batch Size**: 32
* **Optimizer**: Adam
* **Loss function**: Categorical Crossentropy
* **Learning rate**: 0.001
* **data augmentation**: Applied to training data (rotation, zoom, shift, flip)
* **Callbacks Used**: ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
* **Class Weight Balancing**: Enabled to address class imbalance

---

## 📉 Training Metrics

Performance of the model was visualized across training epochs:

### ✅ Accuracy

![Accuracy](accuracy.png)

### ❌ loss

![loss](loss.png)

---

## 🚀 Model Export Formats

The trained model has been exported into the following formats:

* `saved_model/` → Standard TensorFlow format (for TF Serving)
* `tflite/model.tflite` and `tflite/label.txt` → Optimized model and labels for mobile use
* `tfjs_model/` → JavaScript-compatible model for use in web applications

These files are included in the final submission archive.

---
