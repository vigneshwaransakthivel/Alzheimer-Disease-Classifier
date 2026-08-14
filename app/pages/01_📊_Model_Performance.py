"""
=========================================================
NeuroVision AI - Model Performance Dashboard

Displays training results, evaluation metrics, and
visualizations.

Author  : CP
Project : NeuroVision AI
=========================================================
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# Paths
# =========================================================

PROJECT_ROOT = Path(__file__).parent.parent.parent
EVAL_DIR = PROJECT_ROOT / "outputs" / "evaluation"
LOG_DIR = PROJECT_ROOT / "outputs" / "logs"

# =========================================================
# Main Dashboard
# =========================================================

def main():
    
    st.title("📊 Model Performance Dashboard")
    
    st.write("Comprehensive evaluation metrics and training history.")
    
    st.divider()
    
    # =====================================================
    # Test Set Performance
    # =====================================================
    
    st.header("🎯 Test Set Performance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Accuracy", "99.97%")
    
    with col2:
        st.metric("F1 Score", "0.9997")
    
    with col3:
        st.metric("ROC-AUC", "1.0000")
    
    with col4:
        st.metric("Test Images", "6,601")
    
    st.divider()
    
    # =====================================================
    # Per-Class Performance
    # =====================================================
    
    st.header("📋 Per-Class Performance")
    
    # Load classification report
    class_data = {
        "Class": ["Non Demented", "Very Mild Demented", "Mild Demented", "Moderate Demented"],
        "Precision": [1.000, 0.999, 1.000, 1.000],
        "Recall": [1.000, 1.000, 0.999, 1.000],
        "F1-Score": [1.000, 0.999, 0.999, 1.000],
        "Support": [1920, 1681, 1500, 1500]
    }
    
    df = pd.DataFrame(class_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # =====================================================
    # Visualizations
    # =====================================================
    
    st.header("📈 Evaluation Visualizations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Confusion Matrix")
        confusion_matrix_path = EVAL_DIR / "confusion_matrix.png"
        if confusion_matrix_path.exists():
            st.image(str(confusion_matrix_path), use_container_width=True)
        else:
            st.info("Confusion matrix not found. Run evaluation first.")
    
    with col2:
        st.subheader("ROC Curves")
        roc_curve_path = EVAL_DIR / "roc_curve.png"
        if roc_curve_path.exists():
            st.image(str(roc_curve_path), use_container_width=True)
        else:
            st.info("ROC curves not found. Run evaluation first.")
    
    st.divider()
    
    # =====================================================
    # Error Analysis
    # =====================================================
    
    st.header("🔍 Error Analysis")
    
    st.write("**Misclassified Images:** 2 out of 6,601 (0.03% error rate)")
    
    misclassified_path = EVAL_DIR / "misclassified.csv"
    if misclassified_path.exists():
        df_errors = pd.DataFrame({
            "Image": ["aug_9871_mildDem650.jpg", "aug_9911_b658960d-2ef1-4ca9-a1ed-90cf02021b4f.jpg"],
            "Ground Truth": ["Mild Demented", "Mild Demented"],
            "Prediction": ["Very Mild Demented", "Very Mild Demented"],
            "Confidence": ["79.71%", "67.82%"]
        })
        st.dataframe(df_errors, use_container_width=True, hide_index=True)
        
        st.info(
            "⚠️ Both errors occurred on augmented images (notice 'aug_' prefix) "
            "and involved adjacent severity stages (Mild → Very Mild), "
            "which are the most difficult to distinguish clinically."
        )
    
    st.divider()
    
    # =====================================================
    # Training History
    # =====================================================
    
    st.header("📊 Training History")
    
    st.write("**Best Model:** Epoch 27/30")
    st.write("**Training Time:** ~2.5 hours with RTX 3050 GPU")
    
    # Key metrics progression
    epochs_data = {
        "Epoch": [1, 5, 10, 15, 20, 27, 30],
        "Val Accuracy": [0.9497, 0.9930, 0.9985, 0.9994, 0.9994, 0.9998, 0.9997],
        "Val F1 Score": [0.9494, 0.9930, 0.9985, 0.9994, 0.9994, 0.9998, 0.9997]
    }
    
    df_history = pd.DataFrame(epochs_data)
    st.line_chart(df_history.set_index("Epoch"))
    
    st.divider()
    
    # =====================================================
    # Model Information
    # =====================================================
    
    st.header("ℹ️ Model Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Architecture:** ResNet50")
        st.write("**Parameters:** 23.5M")
        st.write("**Training Images:** 30,800")
        st.write("**Validation Images:** 6,600")
    
    with col2:
        st.write("**Test Images:** 6,601")
        st.write("**Batch Size:** 16")
        st.write("**Epochs:** 30")
        st.write("**Optimizer:** Adam")


if __name__ == "__main__":
    main()
