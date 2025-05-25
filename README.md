# Disaster Vision Simulator

This tool simulates realistic disaster-zone drone imagery to help AI models train under chaotic, imperfect, real-world conditions. It includes augmentation tools for noise, motion blur, lighting variation, and occlusion.

## 🚁 Purpose
UAVs in disaster zones encounter:
- Smoke, dust, poor lighting
- Cracks or people at odd angles
- Blur and obstruction

This simulator applies those conditions to training data, boosting AI robustness for real deployment.

## 🧪 Features
- Gaussian blur
- Random rotation and flips
- Gaussian noise
- Contrast and brightness shift
- Zoom and random crop

## 📁 Structure
- `augmentor/`: Augmentation functions (importable)
- `notebooks/`: Demo with visualizations
- `assets/`: Example augmentations
- `data/`: Your training images

## 🛠️ How to Use
1. Place images in `data/`
2. Run the notebook or use functions in your training pipeline

## 🔮 Future Work
- Batch processing for full datasets
- Augmentation labels for segmentation tasks
