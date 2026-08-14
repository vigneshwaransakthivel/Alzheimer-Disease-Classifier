# ⚡ Quick Start Guide

Get up and running in 5 minutes!

---

## 🎯 **What You'll Get:**

A working Alzheimer's disease classifier with:
- 99.97% accuracy
- Interactive web interface
- Explainable AI visualizations

---

## 📋 **Prerequisites:**

- Python 3.12 installed
- Internet connection (for downloading packages & model)
- (Optional) NVIDIA GPU for faster inference

---

## 🚀 **5-Minute Setup:**

### **Step 1: Clone Repository** (30 seconds)
```bash
git clone https://github.com/YOUR-USERNAME/alzheimer-ai.git
cd alzheimer-ai
```

### **Step 2: Install Dependencies** (3-5 minutes)
```bash
pip install -r requirements.txt
```

### **Step 3: Download Model** (1 minute)
1. Download from [Google Drive](https://drive.google.com/drive/folders/1kEMJwnUIE7o01MtlFGrfA9owV7ApgMhs?usp=sharing) (~100MB)
2. Place file at: `outputs/checkpoints/best_model.pth`

### **Step 4: Run Application** (10 seconds)
```bash
streamlit run app/streamlit_app.py
```

### **Step 5: Test It!**
1. App opens in browser (http://localhost:8501)
2. Upload a brain MRI image
3. Get instant prediction with Grad-CAM visualization!

**Test images available at:**
```
dataset/split/test/NonDemented/
dataset/split/test/MildDemented/
dataset/split/test/ModerateDemented/
dataset/split/test/VeryMildDemented/
```

---

## 🎮 **Try These Examples:**

### **Example 1: Healthy Brain**
```
Upload: dataset/split/test/NonDemented/[any-file].jpg
Expected: "Non Demented" with ~100% confidence
```

### **Example 2: Alzheimer's Patient**
```
Upload: dataset/split/test/ModerateDemented/[any-file].jpg
Expected: "Moderate Demented" with ~100% confidence
```

---

## 🐛 **Troubleshooting:**

### **"ModuleNotFoundError: No module named 'torch'"**
```bash
# PyTorch not installed
pip install torch torchvision
```

### **"FileNotFoundError: best_model.pth"**
```bash
# Model file missing or in wrong location
# Make sure it's at: outputs/checkpoints/best_model.pth
```

### **"CUDA out of memory"**
```python
# Edit configs/config.py
BATCH_SIZE = 8  # Reduce from 16
```

### **App won't start**
```bash
# Check if port 8501 is already in use
# Try different port:
streamlit run app/streamlit_app.py --server.port 8502
```

---

## 📊 **Expected Performance:**

When you run the app, predictions should be:
- ⚡ **Fast:** <1 second per image
- 🎯 **Accurate:** 99.97% on test images
- 💯 **Confident:** Most predictions show 100% confidence
- 🧠 **Smart:** Grad-CAM highlights relevant brain regions

---

## 🎓 **Next Steps:**

### **Explore the Project:**
- Check `README.md` for detailed documentation
- View `IMPROVEMENTS.md` for enhancement ideas
- Read `DEPLOYMENT_GUIDE.md` to share your project

### **Experiment:**
- Try different MRI images
- Examine Grad-CAM visualizations
- Check prediction confidence scores

### **Train Your Own:**
```bash
# Prepare dataset
py -3.12 -m src.split_dataset

# Start training (~2.5 hours with GPU)
py -3.12 -m src.train

# Evaluate results
py -3.12 -m src.evaluate
```

---

## 🎉 **You're All Set!**

Your Alzheimer's AI classifier is ready to use!

**Questions?** Check the full [README.md](README.md)

**Want to deploy?** See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

**Built with ❤️ using PyTorch, Streamlit, and ResNet50**
