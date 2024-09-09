from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import cv2
import numpy as np

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Path to the image
img_path = '/media/usama/SSD/Data_13_aug_2024_temp_latest_1/A/tx_bee_cave.jpg'
image = cv2.imread(img_path)

# Perform OCR
result = ocr.ocr(image, cls=True)

# Read the image using OpenCV
output_image = cv2.imread(img_path)

# Iterate over the OCR results
for idx in range(len(result)):
    res = result[idx]
    boxes = [line[0] for line in res]

    # Iterate over the boxes
    for box in boxes:
        coordinates = np.array(box, dtype=np.int32)  # Ensure dtype is int32
        coordinates = coordinates.reshape((-1, 1, 2))  # Reshape if needed

        # Draw the polygon on the image
        cv2.polylines(output_image, [coordinates], isClosed=True, color=(0, 255, 0), thickness=2)

# Save the output image
cv2.imwrite("/media/usama/SSD/Usama_dev_ssd/result/tx_bee_cave.jpg", output_image)



































# # import paddleocr
# from paddleocr import PaddleOCR,draw_ocr
# from PIL import Image
# import cv2
# from PIL import ImageFont
# import numpy as np
# # Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# # You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# # to switch the language model in order.
# ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
# img_path = '/media/usama/SSD/Data_13_aug_2024_temp_latest_1/A/tx_bee_cave.jpg'
# result = ocr.ocr(img_path, cls=True)
# output_image = cv2.imread(img_path)
# # print("result",result)
# for idx in range(len(result)):
#     res = result[idx]
#     # for line in res:
#     #     print(line)
#     #     None
    

# # if len(result) > 0:
#     # # Extract the bounding box coordinates and text from the result
#     # bounding_boxes = [bbox for bbox, _, _ in result]
#     # boxes = [line[0] for line in result]
#     # for bbox in bounding_boxes:
#     boxes = [line[0] for line in res]
#         # boxes = [[[[1129.0, 80.0], [1641.0, 90.0], [1640.0, 135.0], [1128.0, 125.0]], ('LAKEWAY CITYLIMITS', 0.9763332009315491)]]

#     # Load an image (replace 'image.jpg' with your image file)
#     # image = cv2.imread('/media/usama/SSD/Data_13_aug_2024_temp_latest_1/A/tx_bee_cave.jpg')

#         # Iterate over the boxes
#     for box in boxes:
#         print(box)
#         coordinates = np.array(box[0], dtype=np.int32)
#     # Draw the polygon on the image
#         cv2.polylines(output_image, [coordinates], isClosed=True, color=(0, 255, 0), thickness=2)

#     cv2.imwrite("/media/usama/SSD/Usama_dev_ssd/result/tx_bee_cave.jpg",output_image)
# #     print("boxes")
#         # print(bbox)
     
#         # mapped_bbox = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
#         mapped_bbox = np.array(bbox, dtype=np.int32)
#         mapped_bbox = mapped_bbox.reshape((-1, 1, 2))
#         # bounding_boxes.append(mapped_bbox)
#         output_image = cv2.polylines(output_image, [mapped_bbox], isClosed=True, color=(0, 255, 0), thickness=2)
# cv2.imwrite("result_easy_ocr_129.jpg",output_image)

# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, font_path='~/.local/share/fonts/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('/media/usama/SSD/Usama_dev_ssd/result/result_tx_bee_cave.jpg')
# # cv2.imwrite('result.jpg',im_show)


# import os

# relative_path = './fonts/simfang.ttf'
# absolute_path = os.path.abspath(relative_path)
# print("Absolute path is:", absolute_path)

# if os.path.exists(absolute_path):
#     print("Font file exists at:", absolute_path)
# else:
#     print("Font file does not exist at:", absolute_path)