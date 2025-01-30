
# **PaddleOCR-Based Text Detection and Recognition**

## Overview
This project performs text detection in images by dividing them into tiles and using Optical Character Recognition (OCR) models to extract text and bounding boxes. The detected text is annotated and saved as separate image outputs.

## Features
- Loads and processes images from a specified directory
- Tiles images into smaller segments for efficient OCR processing
- Uses PaddleOCR for text detection
- Maps detected bounding boxes back to the original image
- Saves processed images with annotated text and bounding boxes
- Outputs results in a structured directory format

---

## **📂 Repository Structure**
```
📦 paddleocr-text-detection
│-- 📂 data/                         # Input images
│-- 📂 results/                      # Output images with detected text
│-- 📜 Paddle_ocr_9_oct_2024.py       # Main script for OCR processing
│-- 📜 README.md                      # Documentation
```

---

## **🚀 Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Usamaniaz219/Paddle_OCR_for_Text_Detection__Recognition.git 
   cd Paddle_OCR_for_Text_Detection_-_Recognition
   ```
2. Install dependencies:
   ```bash
   pip install torch numpy opencv-python paddleocr pillow

   ```

## Usage
### 1. Prepare the Input Data
Place your images in a directory. Supported format: `.png` (extendable to other formats).

### 2. Run the Processing Function
Use the `process_images` function to process images from a directory:

```python
process_images(directory_path, tile_width, tile_height, output_dir, overlap)
```

#### Parameters:
- `directory_path`: Path to the directory containing input images.
- `tile_width`: Width of each tile.
- `tile_height`: Height of each tile.
- `output_dir`: Directory to store results.
- `overlap`: Overlap parameter for OCR processing.

### 3. Output
The processed images with bounding boxes and detected text are saved in the specified output directory, maintaining a structured subdirectory format.

## Example
```python
process_images('input_images/', 256, 256, 'output_results/', 0.1)
```

## Notes
- The OCR model used is `PaddleOCR` with English language support.
- Ensure GPU support is available if using the `gpu=True` option.
- Adjust `tile_width` and `tile_height` to optimize detection performance.

## License
This project is open-source and available for modification and improvement.



---

## **📜 License**
This project is open-source under the MIT License.




