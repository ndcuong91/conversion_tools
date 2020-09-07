from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import glob, os
from PIL import Image
from tqdm import tqdm

def txtToXml(list_files, img_dir, icdar_anno_dir, output_voc_dir):
    for txt_file in tqdm(glob.glob(icdar_anno_dir + '/*.txt')):
        base_name = os.path.basename(txt_file).split('.')[0]
        print(base_name)
        if len(list_files)>0:
            if base_name not in list_files:
                print('not in list_files',base_name)
                continue
        print('convert',base_name)
        img_path=os.path.join(img_dir, base_name + '.jpg')
        if not os.path.exists(img_path):
            img_path=os.path.join(img_dir, base_name + '.png')

        im = Image.open(img_path)
        width = im.size[0]
        height = im.size[1]
        tree = open(txt_file, 'r', encoding='UTF-8')
        node_root = Element('annotation')
        node_folder = SubElement(node_root, 'folder')
        node_folder.text = 'images'
        node_filename = SubElement(node_root, 'filename')
        node_filename.text = base_name + '.jpg'
        node_size = SubElement(node_root, 'size')
        node_width = SubElement(node_size, 'width')
        node_width.text = str(width)
        node_height = SubElement(node_size, 'height')
        node_height.text = str(height)
        node_depth = SubElement(node_size, 'depth')
        node_depth.text = '3'
        node_segmented = SubElement(node_root, 'segmented')
        node_segmented.text = '0'
        root = tree.readlines()
        for i, line in enumerate(root):
            line_str = line.split('\t')[0].replace('\n', '')
            #separate coordinate with value
            idx = -1
            for i in range(0, 8):
                idx = line_str.find(',', idx + 1)

            coordinates=line_str[:idx]
            val = line_str[idx+1:]
            left, top, right, _, _, bottom, _, _ = coordinates.split(",")
            node_object = SubElement(node_root, 'object')
            node_name = SubElement(node_object, 'name')
            node_name.text = val
            node_pose = SubElement(node_object, 'pose')
            node_pose.text = 'Unspecified'
            node_truncated = SubElement(node_object, 'truncated')
            node_truncated.text = '0'
            node_difficult = SubElement(node_object, 'difficult')
            node_difficult.text = '0'
            node_bndbox = SubElement(node_object, 'bndbox')
            node_xmin = SubElement(node_bndbox, 'xmin')
            node_xmin.text = left
            node_ymin = SubElement(node_bndbox, 'ymin')
            node_ymin.text = top
            node_xmax = SubElement(node_bndbox, 'xmax')
            node_xmax.text = right
            node_ymax = SubElement(node_bndbox, 'ymax')
            node_ymax.text = bottom
        xml = tostring(node_root, pretty_print=True)
        dom = parseString(xml)
        with open(os.path.join(output_voc_dir, base_name + '.xml'), 'w', encoding="utf-8") as f:
            dom.writexml(f, indent='\t', addindent='\t', encoding="utf-8")

#def pascalVOC2icdar()

if __name__ == "__main__":
    img_dir = '/data20.04/data/aicr/korea_test_set/korea_English_test/images'
    icdar_anno_dir = '/home/cuongnd/PycharmProjects/aicr/aicr.core/aicr_core/outputs/predict_pytorch/korea_English_test_2020-08-26_22-37_0.9432_0.4675/pred_icdar'
    output_voc_dir = '/home/cuongnd/PycharmProjects/aicr/aicr.core/aicr_core/outputs/predict_pytorch/korea_English_test_2020-08-26_22-37_0.9432_0.4675/pred_voc'
    list_files=[]
    txtToXml(list_files, img_dir, icdar_anno_dir, output_voc_dir)
