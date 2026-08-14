cmd# 🧠 NeuroVision AI

**Deep Learning for Alzheimer's Disease Classification from Brain MRI Images**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)

---

> **📥 Note:** The trained model file is hosted separately due to size constraints. [Download here](https://drive.google.com/drive/folders/1kEMJwnUIE7o01MtlFGrfA9owV7ApgMhs?usp=sharing) or train your own. See [Download Pre-trained Model](#-download-pre-trained-model) section.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Dataset](#dataset)
- [Training](#training)
- [Running the Application](#running-the-application)
- [Model Architecture](#model-architecture)
- [Evaluation Metrics](#evaluation-metrics)
- [Explainable AI](#explainable-ai)
- [Results](#results)
- [Disclaimer](#disclaimer)

---

## 🎯 Overview

NeuroVision AI is a deep learning system that classifies brain MRI scans into four stages of Alzheimer's disease:

1. **Non Demented** - No signs of dementia
2. **Very Mild Demented** - Early stage cognitive decline
3. **Mild Demented** - Moderate cognitive impairment
4. **Moderate Demented** - Significant cognitive impairment

The system uses a **ResNet50** architecture with transfer learning and provides **Grad-CAM visualizations** to explain predictions.

---

## ✨ Features

- 🔬 **State-of-the-art CNN Architecture** - ResNet50 with transfer learning
- 🎨 **Interactive Web Interface** - Streamlit-based application for easy use
- 📊 **Comprehensive Metrics** - Accuracy, Precision, Recall, F1, MCC, ROC-AUC
- 🔍 **Explainable AI** - Grad-CAM heatmaps showing which brain regions influenced predictions
- ⚡ **Mixed Precision Training** - Faster training with automatic mixed precision (AMP)
- 💾 **Automatic Checkpointing** - Saves best model based on validation F1 score
- 📈 **Training Logs** - Detailed CSV logs for experiment tracking

---

## 📁 Project Structure

```
Alzheimer_prediction-main/
├── app/
│   ├── streamlit_app.py          # Interactive web application
│   ├── inference.py               # Model loading and prediction
│   └── __init__.py
├── configs/
│   ├── config.py                  # Central configuration file
│   └── __init__.py
├── dataset/
│   ├── raw/combined_images/       # Raw MRI images by class
│   └── split/                     # Train/val/test splits (created during training)
├── models/
│   ├── resnet50.py                # ResNet50 architecture
│   └── __init__.py
├── src/
│   ├── train.py                   # Main training script
│   ├── engine.py                  # Training and validation loops
│   ├── dataset.py                 # Custom PyTorch Dataset
│   ├── dataloader.py              # Data loading utilities
│   ├── metrics.py                 # Evaluation metrics
│   ├── gradcam.py                 # Grad-CAM implementation
│   ├── losses.py                  # Loss functions
│   ├── optimizer.py               # Optimizer configuration
│   ├── scheduler.py               # Learning rate scheduler
│   ├── checkpoint.py              # Model checkpoint utilities
│   ├── logger.py                  # Training logger
│   ├── preprocess.py              # Data preprocessing
│   ├── split_dataset.py           # Dataset splitting utility
│   ├── evaluate.py                # Model evaluation script
│   ├── visualization.py           # Plotting utilities
│   └── utils.py                   # Helper functions
├── notebooks/
│   └── 01_EDA.ipynb               # Exploratory data analysis
├── outputs/                       # Created during training
│   ├── checkpoints/               # Model checkpoints
│   ├── logs/                      # Training logs
│   └── plots/                     # Visualization plots
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- NVIDIA GPU with CUDA support (recommended for training)
- 8GB+ RAM
- 10GB+ disk space for dataset and models

### Step 1: Clone the Repository

```bash
cd Alzheimer_prediction-main
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python models/resnet50.py
```

If successful, you should see the model summary and a confirmation message.

---

## � **Download Pre-trained Model**

**⚠️ IMPORTANT:** The trained model file (`best_model.pth`, ~100MB) is **not included** in this repository due to GitHub's 100MB file size limit.

### **Option 1: Use Pre-trained Model** ⭐ Recommended

1. **Download the trained model:**
   - [📥 Google Drive - NeuroVision AI Model](https://drive.google.com/drive/folders/1kEMJwnUIE7o01MtlFGrfA9owV7ApgMhs?usp=sharing) (~100MB)
   - Download `best_model.pth` from the folder
   
2. **Place the file in the correct location:**
   ```
   outputs/checkpoints/best_model.pth
   ```

3. **Skip to [Running the Application](#running-the-application)**

### **Option 2: Train Your Own Model**

If you prefer to train from scratch:
- **Requirements:** NVIDIA GPU with CUDA support (recommended)
- **Training time:** ~2.5-3 hours with RTX 3050
- **Instructions:** See [Training](#training) section below

**Then you can proceed to use the application!**

---

## �📊 Dataset

### Dataset Structure

Organize your MRI images in the following structure:

```
dataset/raw/combined_images/
├── NonDemented/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── VeryMildDemented/
│   ├── image1.jpg
│   └── ...
├── MildDemented/
│   ├── image1.jpg
│   └── ...
└── ModerateDemented/
    ├── image1.jpg
    └── ...
```

### Preparing the Dataset

Before training, split the dataset into train/validation/test sets:

```bash
python src/split_dataset.py
```

This will create:
- `dataset/split/train/` (70% of data)
- `dataset/split/val/` (15% of data)
- `dataset/split/test/` (15% of data)

---

## 🏋️ Training

### Configuration

Edit `configs/config.py` to adjust hyperparameters:

```python
IMAGE_SIZE = 224          # Input image size
NUM_CLASSES = 4           # Number of disease stages
BATCH_SIZE = 32           # Batch size for training
EPOCHS = 30               # Number of training epochs
LEARNING_RATE = 1e-4      # Initial learning rate
WEIGHT_DECAY = 1e-4       # L2 regularization
```

### Start Training

```bash
python src/train.py
```

### Training Features

- **Automatic Mixed Precision (AMP)** - Faster training on CUDA GPUs
- **Learning Rate Scheduling** - Reduces LR on validation loss plateau
- **Best Model Saving** - Automatically saves model with best validation F1 score
- **Progress Bars** - Real-time training progress with tqdm
- **Comprehensive Logging** - Saves all metrics to CSV files

### Monitoring Training

Training logs are saved to `outputs/logs/` with filenames like:
```
experiment_ResNet50_bs32_lr0.0001_YYYYMMDD_HHMMSS.csv
```

Each log contains:
- Epoch number
- Training and validation loss
- Accuracy, Precision, Recall, F1, MCC
- ROC-AUC score
- Learning rate
- GPU memory usage
- Training time per epoch

---

## 🖥️ Running the Application

### Prerequisites

You need a trained model checkpoint at `outputs/checkpoints/best_model.pth`

### Launch the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

The application will open in your web browser at `http://localhost:8501`

### Using the Application

1. **Upload an MRI Image** - Click "Browse files" and select a brain MRI (JPG, JPEG, or PNG)
2. **View Prediction** - The model will classify the image into one of 4 stages
3. **Check Confidence** - See the prediction confidence percentage
4. **Explore Probabilities** - View probability distribution across all classes
5. **Examine Grad-CAM** - See which brain regions influenced the prediction

---

## 🧬 Model Architecture

### ResNet50 with Transfer Learning

- **Backbone**: ResNet50 pre-trained on ImageNet
- **Input**: 224×224×3 RGB images
- **Output**: 4-class probability distribution
- **Total Parameters**: ~25 million
- **Trainable Parameters**: ~25 million (full fine-tuning)

### Architecture Details

```
Input (224×224×3)
    ↓
ResNet50 Backbone (pre-trained)
    ├── Conv1 → BN → ReLU → MaxPool
    ├── Layer1 (3 residual blocks)
    ├── Layer2 (4 residual blocks)
    ├── Layer3 (6 residual blocks)
    └── Layer4 (3 residual blocks)
    ↓
Global Average Pooling
    ↓
Fully Connected (2048 → 4)
    ↓
Output (4 logits)
```

### Transfer Learning Strategy

The model uses **transfer learning** to leverage features learned from ImageNet:
1. Load pre-trained ResNet50 weights
2. Replace final classification layer (1000 → 4 classes)
3. Fine-tune entire network on Alzheimer's MRI dataset

---

## 📈 Evaluation Metrics

The model is evaluated using multiple metrics to ensure robust performance:

### Classification Metrics

- **Accuracy** - Overall classification accuracy
- **Balanced Accuracy** - Accounts for class imbalance
- **Precision** - Positive predictive value (weighted average)
- **Recall** - Sensitivity (weighted average)
- **F1 Score** - Harmonic mean of precision and recall
- **Matthews Correlation Coefficient (MCC)** - Balanced measure for imbalanced datasets
- **ROC-AUC** - Area under the receiver operating characteristic curve (one-vs-rest)

### Confusion Matrix

The confusion matrix shows the distribution of predictions vs. ground truth across all four classes.

---

## 🔍 Explainable AI

### Grad-CAM (Gradient-weighted Class Activation Mapping)

NeuroVision AI uses **Grad-CAM** to provide visual explanations for predictions:

- **What it does**: Highlights regions of the brain MRI that most influenced the model's decision
- **How it works**: Uses gradients flowing into the final convolutional layer to create a heatmap
- **Why it matters**: Increases transparency and trust in AI predictions, especially critical for medical applications

### Interpreting Grad-CAM

- **Red/Yellow regions** - Areas that strongly influenced the prediction
- **Blue/Green regions** - Areas with less influence
- **Clinical relevance** - Helps verify the model is focusing on medically relevant brain structures

---

## 📊 Results

### Expected Performance

With proper training on a balanced dataset, you should expect:

- **Validation Accuracy**: 85-95%
- **Validation F1 Score**: 0.85-0.95
- **ROC-AUC**: 0.90-0.98

*Note: Actual performance depends on dataset quality, size, and class balance.*

### Evaluation Script

To evaluate the trained model on the test set:

```bash
python src/evaluate.py
```

This generates:
- Classification report
- Confusion matrix
- ROC curves
- Per-class performance metrics
- Grad-CAM visualizations for sample predictions

---

## 🏆 **Project Results**

This model achieves **state-of-the-art performance** on Alzheimer's disease classification:

### **Performance Metrics:**
- ✅ **Test Accuracy:** 99.97% (6,599 correct out of 6,601 images)
- ✅ **F1 Score:** 0.9997
- ✅ **ROC-AUC:** 1.0000 (Perfect discrimination)
- ✅ **MCC:** 0.9996
- ✅ **Error Rate:** 0.03% (only 2 misclassifications)

### **Per-Class Performance:**
| Class | Precision | Recall | F1-Score | Test Images |
|-------|-----------|--------|----------|-------------|
| Non Demented | 100.0% | 100.0% | 100.0% | 1,920 |
| Very Mild Demented | 99.9% | 100.0% | 99.9% | 1,681 |
| Mild Demented | 100.0% | 99.9% | 99.9% | 1,500 |
| Moderate Demented | 100.0% | 100.0% | 100.0% | 1,500 |

### **Key Achievements:**
- 🎯 Only 2 errors in 6,601 test images (both on augmented/edge cases)
- 🧠 Model correctly identifies clinically relevant brain regions (hippocampus, ventricles)
- ✅ Validated on external images (Google Images) with 100% confidence
- 📊 Research-grade evaluation with confusion matrix, ROC curves, and Grad-CAM

**Training Details:**
- Dataset: 44,000 MRI images (30,800 train / 6,600 val / 6,601 test)
- GPU: NVIDIA RTX 3050 (6GB VRAM)
- Training Time: ~2.5 hours (30 epochs)
- Best Model: Epoch 27

---

## ⚠️ Disclaimer

**RESEARCH USE ONLY**

NeuroVision AI is an experimental machine learning system developed for **research and educational purposes only**. 

- ❌ **NOT a medical diagnostic tool**
- ❌ **NOT approved for clinical use**
- ❌ **NOT a substitute for professional medical evaluation**

**Important Notes:**

1. This system should **never** be used to make clinical decisions
2. All diagnoses must be made by qualified healthcare professionals
3. MRI interpretation requires extensive medical training and expertise
4. Machine learning models can make errors and have biases
5. Performance metrics are based on specific datasets and may not generalize

**If you or someone you know is concerned about cognitive health, please consult a qualified healthcare provider.**

---

## 🛠️ Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'models'`
- **Solution**: Make sure you're running scripts from the project root directory

**Issue**: `FileNotFoundError: best_model.pth not found`
- **Solution**: Train the model first using `python src/train.py` or download pre-trained weights

**Issue**: CUDA out of memory
- **Solution**: Reduce `BATCH_SIZE` in `configs/config.py` (try 16 or 8)

**Issue**: Training is very slow
- **Solution**: Make sure PyTorch is using GPU. Check with:
  ```python
  import torch
  print(torch.cuda.is_available())  # Should be True
  ```

---

## 📝 License

This project is for educational and research purposes. Please ensure you have appropriate permissions for any datasets used.

---

## 🙏 Acknowledgments

- **PyTorch** - Deep learning framework
- **Streamlit** - Web application framework
- **ResNet** - He et al., "Deep Residual Learning for Image Recognition"
- **Grad-CAM** - Selvaraju et al., "Grad-CAM: Visual Explanations from Deep Networks"

---

For questions, issues, or contributions, please open an issue on the project repository.

---

**Built with ❤️ for advancing Alzheimer's research through AI**
