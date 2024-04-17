import os
import numpy as np
import pandas as pd
import glob
from ultralytics import YOLO
from PIL import Image

MODEL_PATH = "./MODEL/"
IMAGE_PATH = "./IMAGES/"

image_list = os.listdir(IMAGE_PATH)
print(f'Images: {image_list}')
table_output = []

def model_run(im_path):
    run_model_path = os.path.join(MODEL_PATH, "best.pt")
    run_model = YOLO(run_model_path)
    results = run_model(im_path)
    
    for result in results:
        result_output = {"File name": im_path, "predicted":result.boxes.cls.tolist(), "result":result.boxes.conf.tolist()}
        print(result_output, end="\n")
        table_output.append(result_output)
    
        
for root, dirs, files in os.walk(IMAGE_PATH, topdown=False):
  for name in files:
      im_path = os.path.join(root, name)
      model_run(im_path)    

df = pd.DataFrame(table_output)
df.to_csv("output.csv", index=False, header=True)