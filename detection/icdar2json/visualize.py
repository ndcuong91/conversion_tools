import os
import cv2




def _string2poly(line):
    line = line.split(',')
    poly = [int(float(p)) for p in line[:8]]
    poly = [(poly[i], poly[i + 1]) for i in range(0, 8, 2)]
    name = line[-1].replace("\n","")
    return poly, name


def read_label(labels_path):
    polygon = []
    f = open(labels_path, encoding='utf8')
    lines = f.readlines()
    for line in lines:
        poly = _string2poly(line)
        polygon.append(poly)
    f.close()
    return polygon


def draw_polygon(img, polygon):
    for p_item in polygon:
        poly, name = p_item
        for i in range(len(poly)):
            cv2.line(img, poly[i], poly[(i+1)%4], (255, 255, 255), 2)
            # cv2.putText(img, str(i+1), poly[i], cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0))

        cv2.putText(img,name, poly[0],cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,0))
    return img


def draw_(img_path, labels_path):
    polygon = read_label(labels_path)
    img = cv2.imread(img_path)
    img = draw_polygon(img, polygon)
    return img



