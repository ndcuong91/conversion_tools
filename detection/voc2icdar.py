from core_io.pascal_voc_io import XML_EXT
from core_io.pascal_voc_io import PascalVocWriter
from core_io.pascal_voc_io import PascalVocReader
import os.path
import sys

try:
    from PyQt5.QtGui import QImage
except ImportError:
    from PyQt4.QtGui import QImage

# Search all pascal annotation (xml files) in this folder
def voc2icdar(voc_dir, icdar_dir):
    for file in os.listdir(voc_dir):
        if file.endswith(".xml"):
            print(file)
            annotation_no_xml = os.path.splitext(file)[0]

            imagePath = voc_dir + "/" + annotation_no_xml + ".jpg"

            image = QImage()
            image.load(imagePath)
            imageShape = [image.height(), image.width(), 1 if image.isGrayscale() else 3]
            imgFolderName = os.path.basename(voc_dir)
            imgFileName = os.path.basename(imagePath)


            # Read classes.txt
            classListPath = voc_dir + "/" + "classes.txt"

            # Read VOC file
            filePath = voc_dir + "/" + file
            tVocParseReader = PascalVocReader(filePath)
            shapes = tVocParseReader.getShapes()
            num_of_box = len(shapes)

            gt_txt=''
            for i in range(num_of_box):
                label = shapes[i][0]
                xmin = str(shapes[i][1][0][0])
                ymin = str(shapes[i][1][0][1])
                xmax = str(shapes[i][1][2][0])
                ymax = str(shapes[i][1][2][1])
                line=','.join([xmin,ymin,xmax,ymin,xmax,ymax,xmin,ymax,label])
                gt_txt+=line+'\n'
            gt_txt=gt_txt.rstrip('\n')
            save_file_path=icdar_dir + "/" + annotation_no_xml + ".txt"
            with open(save_file_path, 'w',encoding='utf8') as f:
                f.write(gt_txt)

if __name__ == '__main__':
    voc_dir=r'/home/cuongnd/PycharmProjects/aicr/viText/viText/viData/viReceipts/anno_voc'
    icdar_dir=r'/home/cuongnd/PycharmProjects/aicr/viText/viText/viData/viReceipts/anno_icdar'
    if voc_dir=='':
        voc_dir = sys.argv[1]
    voc2icdar(voc_dir, icdar_dir)