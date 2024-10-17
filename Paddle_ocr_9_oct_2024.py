import numpy as np
import easyocr
import cv2
import math
import os
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

bounding_boxes = []

def load_image(image_path):
    image = cv2.imread(image_path)
    
    return image

def calculate_num_rows_and_cols(image, tile_width, tile_height):
    # Calculate the number of rows and columns
    num_rows = math.ceil(image.shape[0] / tile_height)
    num_cols = math.ceil(image.shape[1] / tile_width)
    return num_rows, num_cols

def extract_tile(image, start_x, start_y, tile_width, tile_height):
    # Extract the tile from the image
    end_x = min(start_x + tile_width, image.shape[1])
    end_y = min(start_y + tile_height, image.shape[0])
    return image[start_y:end_y, start_x:end_x]

def detect_text_in_tile(image, tile_width, tile_height, ocr, overlap, output_dir, image_name):
    # Create a specific directory for the current image inside the output directory
    image_dir = os.path.join(output_dir, image_name)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # List to store bounding boxes
    bounding_boxes = []

    # Copy of the original image
    output_image = np.copy(image)
   
    
    # Get image dimensions
    image_height, image_width = image.shape[:2]

    # Calculate the number of rows and columns based on tile dimensions
    num_rows, num_cols = calculate_num_rows_and_cols(image, tile_width, tile_height)

    # Counter for naming the blank images for each bounding box
    bbox_counter = 0

    # Iterate over each tile in the image
    for r in range(num_rows):
        for c in range(num_cols):
            # Calculate the starting coordinates of the tile
            start_x = c * tile_width
            start_y = r * tile_height

            # Extract the tile from the image
            tile = extract_tile(image, start_x, start_y, tile_width, tile_height)

            # Perform OCR on the tile
            result = ocr.ocr(tile, cls=True)

            # Check if any text and bounding boxes were detected
            if len(result) > 0:
                for idx in range(len(result)):
                    res = result[idx]
                    
                    if np.any(res):
                        # Extract bounding boxes and the detected text
                        boxes_tile = [line[0] for line in res]
                        texts_tile = [line[1][0] for line in res]

                        # Map the bounding box coordinates back to the original image coordinates
                        for bbox, text in zip(boxes_tile, texts_tile):
                            try:
                                [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = bbox
                            except ValueError:
                                continue

                            # Adjust bounding box coordinates to fit the original image
                            x1 += start_x
                            y1 += start_y
                            x2 += start_x
                            y2 += start_y
                            x3 += start_x
                            y3 += start_y
                            x4 += start_x
                            y4 += start_y

                            # Store the mapped bounding box
                            mapped_bbox = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
                            mapped_bbox = np.array(mapped_bbox, dtype=np.int32).reshape((-1, 1, 2))
                            bounding_boxes.append(mapped_bbox)

                            # Create a blank image with the same resolution as the original image
                            blank_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
                            output_image_1 = np.copy(image)
                            # Draw the bounding box on the blank image
                            blank_image = cv2.polylines(output_image_1, [mapped_bbox], isClosed=True, color=(0, 255, 0), thickness=2)
                           
                            # Calculate the position for placing the text (middle of the bounding box)
                            x_text1, y_text1 = int(x1), int(y1)
                            x_text2, y_text2 = int(x3), int(y3)
                            x_text = (x_text1 + x_text2) // 2
                            y_text = (y_text1 + y_text2) // 2

                            # Draw the text in white
                            cv2.putText(output_image_1, text, (x_text, y_text), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

                            # Save the blank image with the bounding box and text in the specific image directory
                            output_path = os.path.join(image_dir, f"bbox_{bbox_counter}.jpg")
                            cv2.imwrite(output_path, output_image_1)

                            bbox_counter += 1

                            # Optionally, draw the bounding box and text on the original image
                            output_image = cv2.polylines(output_image, [mapped_bbox], isClosed=True, color=(0, 0, 255), thickness=2)
                            cv2.putText(output_image, text, (x_text, y_text), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    return bounding_boxes, output_image

def process_images(directory_path, tile_width, tile_height, output_dir,overlap):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(directory_path):
        if filename.endswith(".png"):  # Add other extensions if needed
            image_path = os.path.join(directory_path, filename)
            ori_image_name = os.path.splitext(os.path.basename(image_path))[0]
            print("Original image name:", ori_image_name)
            image = load_image(image_path)
            if image is not None:
                # Resize image to be a multiple of tile_width and tile_height
                # resized_image = resize_image_to_multiple(image, tile_width, tile_height)
                # reader = easyocr.Reader(['en'], gpu=True)  # this needs to run only once to load the model into memory
                ocr = PaddleOCR(use_angle_cls=True, lang='en',det_db_unclip_ratio=2.0)
                bounding_boxes, output_image = detect_text_in_tile(image, tile_width, tile_height, ocr,overlap,output_dir,ori_image_name)
                # cv2.imwrite("paddle_page_o.jpg",output_image)
                output_file_path = os.path.join(output_dir, f"{ori_image_name}_detected_bbox_result_text_for_default_parameter_settings.jpg")
                # cv2.imwrite(output_file_path, output_image)
            else:
                print(f"Failed to read {image_path}")

# Directory containing the images
image_directory = '/home/usama/Downloads/remaining_images-20241009T055410Z-001/remaining_images/'
output_dir = "/media/usama/SSD/Usama_dev_ssd/ocr_based_text_detection/paddle_ocr_detection_and_recognition_results_on_blank_image_9_oct_2024_latest/"
tile_width = 1024
tile_height = 1024
overlap = 0

process_images(image_directory, tile_width, tile_height, output_dir,overlap)
