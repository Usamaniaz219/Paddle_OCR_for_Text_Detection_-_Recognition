
# **PaddleOCR-Based Text Detection and Recognition**

This repository contains a script, `Paddle_ocr_9_oct_2024.py`, for detecting and recognizing text in images using **PaddleOCR** and **OpenCV**. The script divides images into tiles, applies OCR, and saves detected text along with bounding boxes.

---

## **📌 Features**
- **Tile-based OCR processing** to handle large images efficiently.
- **PaddleOCR for text detection and recognition**, supporting angled text.
- **Bounding box extraction and annotation** on images.
- **Automatic text overlay and storage** in a structured format.
- **Output saved with detected text and bounding boxes** for analysis.

---

## **📂 Repository Structure**
```
📦 paddleocr-text-detection
│-- 📂 data/                         # Input images
│-- 📂 results/                      # Output images with detected text
│-- 📜 Paddle_ocr_9_oct_2024.py       # Main script for OCR processing
│-- 📜 requirements.txt               # Dependencies
│-- 📜 README.md                      # Documentation
```

---

## **🚀 Installation**
1. Clone the repository:
   ```bash
   git clone 
   cd paddleocr-text-detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **🛠️ Usage**
### **Run the Script**
Modify the image directory paths in `Paddle_ocr_9_oct_2024.py` and run:
```bash
python Paddle_ocr_9_oct_2024.py
```

### **Inputs**
- **Image Folder:** The script reads images from the specified directory.
- **Tile Dimensions:** Images are divided into `1024x1024` tiles.
- **Overlap:** (Currently set to `0`, can be adjusted.)

### **Outputs**
- **Processed images with bounding boxes** in the `results/` directory.
- **Bounding box annotations** on blank images for better visibility.
- **Extracted text stored with the corresponding image name.**

---

## **📜 License**
This project is open-source under the MIT License.




