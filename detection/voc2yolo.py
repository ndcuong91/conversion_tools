from core_io.pascal_voc_io import XML_EXT
from core_io.pascal_voc_io import PascalVocWriter
from core_io.pascal_voc_io import PascalVocReader
from core_io.yolo_io import YoloReader
from core_io.yolo_io import YOLOWriter
import os.path
import sys

try:
    from PyQt5.QtGui import QImage
except ImportError:
    from PyQt4.QtGui import QImage

# Search all pascal annotation (xml files) in this folder
def voc2yolo(voc_dir):
    for file in os.listdir(voc_dir):
        if file.endswith(".xml"):
            annotation_no_xml = os.path.splitext(file)[0]

            imagePath = voc_dir + "/" + annotation_no_xml + ".jpg"

            image = QImage()
            image.load(imagePath)
            imageShape = [image.height(), image.width(), 1 if image.isGrayscale() else 3]
            imgFolderName = os.path.basename(voc_dir)
            imgFileName = os.path.basename(imagePath)

            writer = YOLOWriter(imgFolderName, imgFileName, imageShape, localImgPath=imagePath)

            # Read classes.txt
            classListPath = voc_dir + "/" + "classes.txt"
            classesFile = open(classListPath, 'r')
            classes = classesFile.read().strip('\n').split('\n')
            classesFile.close()

            # Read VOC file
            filePath = voc_dir + "/" + file
            tVocParseReader = PascalVocReader(filePath)
            shapes = tVocParseReader.getShapes()
            num_of_box = len(shapes)

            for i in range(num_of_box):
                label = classes.index(shapes[i][0])
                xmin = shapes[i][1][0][0]
                ymin = shapes[i][1][0][1]
                x_max = shapes[i][1][2][0]
                y_max = shapes[i][1][2][1]

                writer.addBndBox(xmin, ymin, x_max, y_max, label, 0)

            writer.save(targetFile=voc_dir + "/" + annotation_no_xml + ".txt")


if __name__ == '__main__':
    voc_dir=''
    if voc_dir=='':
        voc_dir = sys.argv[1]
    voc2yolo(voc_dir)