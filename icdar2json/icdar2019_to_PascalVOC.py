import json
import numpy as np
from visualize import read_label
import cv2
import base64
import os


def convert_named_polygon(named_polygon):
    shapes = []
    for p_item in named_polygon:
        poly, name = p_item

        shape = {"label": name,
                 "line_color": None,
                 "fill_color": None,
                 "shape_type": "polygon",
                 "points": poly
                 }
        shapes.append(shape)
    return shapes


def save_asjson(img_path, label_path,result_dir):
    h,w,c = cv2.imread(img_path).shape
    
    with open(img_path, mode='rb') as file:
        img = file.read()

    img_data = base64.encodebytes(img).decode("utf-8")
    file.close()

    named_polygon = read_label(label_path)
    shapes = convert_named_polygon(named_polygon)
    flag = {}
    main_structure = {
        "version": "3.16.1",
        "flags": flag,
        "shapes": shapes,
        "lineColor": [
            0,
            255,
            0,
            128
        ],
        "fillColor": [
            255,
            0,
            0,
            128
        ],
        "imagePath": img_path.split("/")[-1],
        "imageData": "",
        "imageHeight": h ,
        "imageWidth": w
    }
    json_name = os.path.basename(img_path).replace("jpg","json").replace("png","json")
    with open(os.path.join(result_dir,json_name), "w") as f:
        json.dump(main_structure, f)


for img_name in os.listdir("images"):
    txt_name = img_name.replace("jpg","txt").replace("png","txt")
    txt_path = os.path.join("labels_txt",txt_name)
    img_path = os.path.join("images",img_name)
    print(img_name, img_path)
    save_asjson(img_path,txt_path,"labels")
