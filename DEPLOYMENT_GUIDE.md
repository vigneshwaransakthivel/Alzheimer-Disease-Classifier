# Deployment Guide

Complete guide for sharing your Alzheimer's AI project.

---

## Step 1: Upload Model to Google Drive

### Why Google Drive?

* Free (15 GB storage)
* Easy sharing
* Reliable downloads
* No GitHub file-size limitations

### Instructions

#### Locate Your Trained Model

```text
outputs/checkpoints/best_model.pth
```

Approximate size: 100 MB

#### Upload to Google Drive

1. Open Google Drive.
2. Click **New → File Upload**.
3. Select `best_model.pth`.
4. Wait for the upload to complete.

#### Create a Shareable Link

1. Right-click the uploaded file.
2. Select **Share**.
3. Change access to **Anyone with the link**.
4. Copy the generated link.

#### Update README.md

Replace the placeholder model link with your Google Drive link.

Example:

```text
https://drive.google.com/file/d/1ABC...XYZ/view?usp=sharing
```

---

## Step 2: Push Code to GitHub

### Create a Repository

1. Open GitHub.
2. Click **+ → New Repository**.

### Repository Settings

* Repository Name: `alzheimer-disease-classifier`
* Description: Deep learning system for Alzheimer's disease classification
* Visibility: Public or Private
* Do not initialize with a README

### Push Your Project

```bash
# Navigate to project folder
cd c:\Users\vigne\Downloads\Alzheimer_prediction-main\Alzheimer_prediction-main

# Initialize repository
git init

# Add files
git add .

# Commit changes
git commit -m "Initial commit: Alzheimer's AI Classifier"

# Add remote repository
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Files Included

Included:

* Source code
* README.md
* requirements.txt
* Configuration files
* Documentation

Excluded:

* Model checkpoints
* Dataset files
* Training outputs
* Cache files

---

## Step 3: Deploy to Streamlit Cloud (Optional)

### Benefits

* Public web application
* No installation required for users
* Free hosting for public repositories
* Automatic deployment updates

### Deployment Steps

#### Create a Streamlit Cloud Account

1. Visit Streamlit Community Cloud.
2. Sign in with GitHub.

#### Create a New App

* Repository: Your GitHub repository
* Branch: `main`
* Main file: `app/streamlit_app.py`

#### Download Model Automatically

Add the following code:

```python
import gdown
import os

MODEL_PATH = "outputs/checkpoints/best_model.pth"
GDRIVE_ID = "YOUR_FILE_ID"

if not os.path.exists(MODEL_PATH):
    gdown.download(
        f"https://drive.google.com/uc?id={GDRIVE_ID}",
        MODEL_PATH,
        quiet=False
    )
```

Add to `requirements.txt`:

```text
gdown
```

#### Deploy

1. Click **Deploy**.
2. Wait a few minutes.
3. Your application becomes available through a public URL.

Example:

```text
https://your-app-name.streamlit.app
```

### Update README

Add a live demo section:

```markdown
## Live Demo

Try the application here:

https://your-app-name.streamlit.app
```

---

## Step 4: Create a Demo Video (Recommended)

### Suggested Content

1. Open the application.
2. Upload an MRI image.
3. Display prediction results.
4. Demonstrate Grad-CAM visualization.
5. Show confidence scores.

### Recording Tools

* Xbox Game Bar (Windows)
* Loom
* OBS Studio

### Hosting

* YouTube
* Google Drive
* Vimeo

Add the video link to your README.

---

## Step 5: Add Screenshots

### Recommended Screenshots

* Application homepage
* Prediction page
* Grad-CAM visualization
* Confusion matrix
* ROC curve

### Organize Images

```bash
mkdir docs/images
```

### README Example

```markdown
## Screenshots

### Application Interface
![Interface](docs/images/app-interface.png)

### Prediction Results
![Prediction](docs/images/prediction.png)

### Grad-CAM Visualization
![Grad-CAM](docs/images/gradcam.png)
```

---

## Final Checklist

* [ ] Upload model to Google Drive
* [ ] Add model link to README
* [ ] Push project to GitHub
* [ ] Verify `.gitignore`
* [ ] Verify installation instructions
* [ ] Verify requirements.txt
* [ ] Deploy application (optional)
* [ ] Record demo video (optional)
* [ ] Add screenshots (optional)

---

## What Users Can Do

### Explore the Repository

* Review source code
* Read documentation
* Understand implementation details

### Use the Application

* Access deployed Streamlit app
* Upload MRI scans
* View predictions and Grad-CAM outputs

### Run Locally

```bash
git clone https://github.com/username/repository.git
cd repository

pip install -r requirements.txt

streamlit run app/streamlit_app.py
```

### Train Their Own Model

```bash
py -3.12 -m src.train
```

---

## Use Cases

### Portfolio Projects

```text
GitHub: github.com/username/alzheimer-ai
Live Demo: your-app.streamlit.app

Built an Alzheimer's disease classification system
using deep learning and explainable AI techniques.
```

### Educational Use

* Learn medical image classification
* Explore transfer learning
* Understand Grad-CAM explainability

### Collaboration

* Fork repository
* Submit pull requests
* Report issues
* Propose improvements

---

## Best Practices

1. Keep the README concise and clear.
2. Provide a live demo when possible.
3. Include screenshots.
4. Highlight key results early.
5. Add a software license.
6. Cite datasets and external resources.
7. Keep dependencies updated.
8. Document deployment steps clearly.

---

## Example README Header

````markdown
# NeuroVision AI - Alzheimer's Disease Classifier

Deep learning system for Alzheimer's disease classification from brain MRI scans.

[![Python](https://img.shields.io/badge/Python-3.12-blue)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.5-red)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

## Live Demo

https://your-app.streamlit.app

## Download Model

https://drive.google.com/...

## Quick Start

```bash
git clone https://github.com/username/repository.git
cd repository

pip install -r requirements.txt

streamlit run app/streamlit_app.py
```

## Results

- 99.97% Test Accuracy
- 0.9997 F1 Score
- 1.0000 ROC-AUC
- Only 2 misclassifications on the test set
````

---

Your project is ready to be shared through GitHub, Streamlit Cloud, and portfolio platforms.
