from ultralytics import YOLO
from PIL import Image, ImageDraw

import output

model = YOLO(r"best_yolov8x.pt")

def process_image(image_path):
    """Process the given image and save it as 'processed.png'."""
    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        # Placeholder for defect detection with a model
        pred_results = model(image_path)  # Ensure your model's prediction method is called correctly
        num_defects = len(pred_results[0].boxes.cls)
        class_list = [model.names[int(cls)] for cls in pred_results[0].boxes.cls]

        if pred_results[0].masks:
            for mask in pred_results[0].masks.cpu():
                for polygon in mask.xy:
                    draw.polygon(polygon, outline=(0, 255, 0), width=5)

            text = f"Defective Sample. \n\nNumber of defects: {num_defects}. \n\nDefect Classes: {' '.join(class_list)}"
        else:
            text = "No Defects Found"

        img.save("processed.png")
        global life
        life = output.returnoutput(pred_results[0].boxes.cls)
        return text
    except Exception as e:
        print(f"Error processing image: {e}")
        return "Error in processing the image."




