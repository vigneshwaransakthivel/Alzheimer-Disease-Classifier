# Quick Start Guide

Get up and running in 5 minutes!

---

## What You'll Get

A working Alzheimer's disease classifier with:

* 99.97% accuracy
* Interactive web interface
* Explainable AI visualizations

---

## Prerequisites

* Python 3.12 installed
* Internet connection (for downloading packages and model)
* NVIDIA GPU (optional, for faster inference)

---

## 5-Minute Setup

### Step 1: Clone Repository (30 seconds)

```bash
git clone https://github.com/YOUR-USERNAME/alzheimer-ai.git
cd alzheimer-ai
```

### Step 2: Install Dependencies (3–5 minutes)

```bash
pip install -r requirements.txt
```

### Step 3: Download Model (1 minute)

1. Download from Google Drive (~100 MB)
2. Place the file at:

```text
outputs/checkpoints/best_model.pth
```

### Step 4: Run Application (10 seconds)

```bash
streamlit run app/streamlit_app.py
```

### Step 5: Test It

1. The application opens in your browser (`http://localhost:8501`)
2. Upload a brain MRI image
3. Receive a prediction with Grad-CAM visualization

**Test images available in:**

```text
dataset/split/test/NonDemented/
dataset/split/test/MildDemented/
dataset/split/test/ModerateDemented/
dataset/split/test/VeryMildDemented/
```

---

## Example Usage

### Example 1: Healthy Brain

```text
Upload: dataset/split/test/NonDemented/[any-file].jpg
Expected Result: Non Demented (~100% confidence)
```

### Example 2: Alzheimer's Patient

```text
Upload: dataset/split/test/ModerateDemented/[any-file].jpg
Expected Result: Moderate Demented (~100% confidence)
```

---

## Troubleshooting

### ModuleNotFoundError: No module named 'torch'

```bash
pip install torch torchvision
```

### FileNotFoundError: best_model.pth

Ensure the model file exists at:

```text
outputs/checkpoints/best_model.pth
```

### CUDA Out of Memory

Edit `configs/config.py`:

```python
BATCH_SIZE = 8
```

### Application Won't Start

Try a different port:

```bash
streamlit run app/streamlit_app.py --server.port 8502
```

---

## Expected Performance

Predictions should be:

* Fast: Less than 1 second per image
* Accurate: 99.97% test accuracy
* High confidence on most predictions
* Grad-CAM visualizations highlighting relevant brain regions

---

## Next Steps

### Explore the Project

* Read `README.md` for full documentation
* Review `IMPROVEMENTS.md` for future enhancements
* Follow `DEPLOYMENT_GUIDE.md` for deployment instructions

### Experiment

* Test different MRI images
* Analyze Grad-CAM visualizations
* Compare prediction confidence scores

### Train Your Own Model

```bash
# Prepare dataset
py -3.12 -m src.split_dataset

# Start training
py -3.12 -m src.train

# Evaluate results
py -3.12 -m src.evaluate
```

Training typically takes approximately 2.5 hours on an RTX 3050 GPU.

---

## You're All Set

Your Alzheimer's disease classification system is ready to use.

For detailed documentation, see `README.md`.

For deployment instructions, see `DEPLOYMENT_GUIDE.md`.

---

Built using PyTorch, Streamlit, and ResNet50.
