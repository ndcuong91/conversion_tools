import os
import json

def pt_labels_to_string(pt_lbl):
    result_str = ""
    for pt,lbl in pt_lbl:
        points = ""

        for point in pt:
            points += "{},{},".format(
                int(float(point[0])),
                int(float(point[1])))
        line = "{}{}".format(points,lbl)
        result_str+= line+"\n"
    return result_str    

def read_json(path):
    pt_labels = []
    with open(path) as json_file:  
        data = json.load(json_file)
        shapes = data["shapes"]
        for shape in shapes:
            point = shape["points"]
            label = shape["label"]
            pt_labels.append((point,label))
    return pt_labels        

