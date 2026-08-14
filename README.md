# NeuroVision AI

**Deep Learning for Alzheimer's Disease Classification from Brain MRI Images**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)

---

> **Note:** The trained model file is hosted separately due to size constraints. Download it from Google Drive or train your own model. See the "Download Pre-trained Model" section below.

---

## Table of Contents

* Overview
* Features
* Project Structure
* Installation
* Dataset
* Training
* Running the Application
* Model Architecture
* Evaluation Metrics
* Explainable AI
* Results
* Disclaimer

---

## Overview

NeuroVision AI is a deep learning system that classifies brain MRI scans into four stages of Alzheimer's disease:

1. Non Demented — No signs of dementia
2. Very Mild Demented — Early-stage cognitive decline
3. Mild Demented — Moderate cognitive impairment
4. Moderate Demented — Significant cognitive impairment

The system uses a ResNet50 architecture with transfer learning and provides Grad-CAM visualizations to explain predictions.

---

## Features

* ResNet50-based deep learning model with transfer learning
* Interactive Streamlit web application
* Comprehensive evaluation metrics
* Grad-CAM visual explanations
* Mixed Precision Training (AMP)
* Automatic model checkpointing
* Experiment tracking and training logs

---

## Project Structure

```text
Alzheimer_prediction-main/
├── app/
│   ├── streamlit_app.py
│   ├── inference.py
│   └── __init__.py
├── configs/
│   ├── config.py
│   └── __init__.py
├── dataset/
│   ├── raw/combined_images/
│   └── split/
├── models/
│   ├── resnet50.py
│   └── __init__.py
├── src/
│   ├── train.py
│   ├── engine.py
│   ├── dataset.py
│   ├── dataloader.py
│   ├── metrics.py
│   ├── gradcam.py
│   ├── losses.py
│   ├── optimizer.py
│   ├── scheduler.py
│   ├── checkpoint.py
│   ├── logger.py
│   ├── preprocess.py
│   ├── split_dataset.py
│   ├── evaluate.py
│   ├── visualization.py
│   └── utils.py
├── notebooks/
│   └── 01_EDA.ipynb
├── outputs/
│   ├── checkpoints/
│   ├── logs/
│   └── plots/
├── requirements.txt
└── README.md
```

---

## Installation

### Prerequisites

* Python 3.8 or higher
* NVIDIA GPU with CUDA support (recommended)
* 8GB or more RAM
* 10GB or more available storage

### Clone the Repository

```bash
cd Alzheimer_prediction-main
```

### Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Verify Installation

```bash
python models/resnet50.py
```

---

## Download Pre-trained Model

The trained model (`best_model.pth`, approximately 100 MB) is not included in the repository because of GitHub file-size limits.

### Option 1: Use the Pre-trained Model

1. Download `best_model.pth` from the provided Google Drive folder.
2. Place it in:

```text
outputs/checkpoints/best_model.pth
```

3. Launch the application.

### Option 2: Train the Model Yourself

Requirements:

* NVIDIA GPU recommended
* Approximately 2.5–3 hours training time on RTX 3050

Follow the training instructions below.

---

## Dataset

### Dataset Structure

```text
dataset/raw/combined_images/
├── NonDemented/
├── VeryMildDemented/
├── MildDemented/
└── ModerateDemented/
```

### Split the Dataset

```bash
python src/split_dataset.py
```

Generated splits:

* Train: 70%
* Validation: 15%
* Test: 15%

---

## Training

### Configuration

Modify hyperparameters in `configs/config.py`:

```python
IMAGE_SIZE = 224
NUM_CLASSES = 4
BATCH_SIZE = 32
EPOCHS = 30
LEARNING_RATE = 1e-4
WEIGHT_DECAY = 1e-4
```

### Start Training

```bash
python src/train.py
```

### Training Features

* Automatic Mixed Precision (AMP)
* Learning Rate Scheduling
* Best Model Saving
* Progress Monitoring
* CSV-based Logging

---

## Running the Application

### Launch Streamlit

```bash
streamlit run app/streamlit_app.py
```

Application URL:

```text
http://localhost:8501
```

### Usage

1. Upload an MRI image.
2. View predicted Alzheimer's stage.
3. Review confidence scores.
4. Examine class probabilities.
5. Analyze Grad-CAM visualizations.

---

## Model Architecture

### ResNet50 with Transfer Learning

* Backbone: ResNet50 pretrained on ImageNet
* Input Size: 224 × 224 × 3
* Output Classes: 4
* Parameters: ~25 Million

### Architecture

```text
Input (224×224×3)
    ↓
ResNet50 Backbone
    ↓
Global Average Pooling
    ↓
Fully Connected Layer (2048 → 4)
    ↓
Output Probabilities
```

### Transfer Learning Workflow

1. Load ImageNet pretrained ResNet50 weights.
2. Replace final classification layer.
3. Fine-tune on Alzheimer's MRI data.

---

## Evaluation Metrics

The model is evaluated using:

* Accuracy
* Balanced Accuracy
* Precision
* Recall
* F1 Score
* Matthews Correlation Coefficient (MCC)
* ROC-AUC

A confusion matrix and class-wise evaluation are also generated.

---

## Explainable AI

### Grad-CAM

Grad-CAM highlights image regions that influenced model predictions.

Benefits:

* Improves model interpretability
* Supports visual validation
* Increases transparency in medical AI systems

### Interpretation

* Red/Yellow: High influence
* Blue/Green: Low influence

---

## Results

### Expected Performance

Typical results on a balanced dataset:

| Metric   | Range     |
| -------- | --------- |
| Accuracy | 85–95%    |
| F1 Score | 0.85–0.95 |
| ROC-AUC  | 0.90–0.98 |

### Evaluation

```bash
python src/evaluate.py
```

Outputs include:

* Classification report
* Confusion matrix
* ROC curves
* Class-wise metrics
* Grad-CAM visualizations

---

## Project Results

### Overall Performance

| Metric        | Value  |
| ------------- | ------ |
| Test Accuracy | 99.97% |
| F1 Score      | 0.9997 |
| ROC-AUC       | 1.0000 |
| MCC           | 0.9996 |
| Error Rate    | 0.03%  |

### Per-Class Performance

| Class              | Precision | Recall | F1 Score | Test Images |
| ------------------ | --------- | ------ | -------- | ----------- |
| Non Demented       | 100.0%    | 100.0% | 100.0%   | 1,920       |
| Very Mild Demented | 99.9%     | 100.0% | 99.9%    | 1,681       |
| Mild Demented      | 100.0%    | 99.9%  | 99.9%    | 1,500       |
| Moderate Demented  | 100.0%    | 100.0% | 100.0%   | 1,500       |

### Training Details

* Dataset Size: 44,000 MRI images
* Train Images: 30,800
* Validation Images: 6,600
* Test Images: 6,601
* GPU: NVIDIA RTX 3050 (6GB)
* Training Time: Approximately 2.5 hours
* Best Model: Epoch 27

---

## Disclaimer

### Research Use Only

NeuroVision AI is intended solely for research and educational purposes.

It is:

* Not a medical diagnostic tool
* Not approved for clinical use
* Not a replacement for professional medical evaluation

Important considerations:

1. Clinical decisions should never be based solely on this model.
2. Diagnoses must be performed by qualified healthcare professionals.
3. MRI interpretation requires medical expertise.
4. Machine learning models can produce incorrect predictions.
5. Results may not generalize to all patient populations.

---

## Troubleshooting

### ModuleNotFoundError

```text
ModuleNotFoundError: No module named 'models'
```

**Solution:** Run scripts from the project root directory.

### Missing Model File

```text
FileNotFoundError: best_model.pth not found
```

**Solution:** Download or train the model before inference.

### CUDA Out of Memory

Reduce batch size in `configs/config.py`.

### Slow Training

Verify GPU availability:

```python
import torch
print(torch.cuda.is_available())
```

Expected output:

```python
True
```

---

## License

This project is intended for educational and research purposes. Ensure appropriate permissions for any datasets used.

---

## Acknowledgments

* PyTorch
* Streamlit
* ResNet (He et al.)
* Grad-CAM (Selvaraju et al.)
