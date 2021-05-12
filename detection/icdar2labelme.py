import glob, os
from PIL import Image
from tqdm import tqdm
import json
import base64


def txt2labelme(img_dir, icdar_anno_dir, output_labelme_dir, ext=['jpg', 'JPG', 'PNG', 'png'], default_class ='other'):
    for txt_file in tqdm(glob.glob(icdar_anno_dir + '/*.txt')):
        base_name = os.path.basename(txt_file).replace('.txt', '')
        print('txt2labelme. Convert', base_name)
        for ex in ext:
            if os.path.exists(os.path.join(img_dir, base_name + '.' + ex)):
                img_path = os.path.join(img_dir, base_name + '.' + ex)
                break
        im = Image.open(img_path)

        with open(img_path, mode='rb') as file:
            img_data = base64.encodebytes(file.read()).decode("utf-8")


        tree = open(txt_file, 'r', encoding='UTF-8')
        root = tree.readlines()
        bboxes =[]
        for i, line in enumerate(root):
            line_str = line.split('\t')[0].replace('\n', '')
            # separate coordinate with value
            idx = -1
            for i in range(0, 8):
                idx = line_str.find(',', idx + 1)

            coordinates = line_str[:idx]
            val = line_str[idx + 1:]
            if default_class is not None:
                val = default_class
            locs= [float(f) for f in coordinates.split(",")]

            bbox= {'label':val,
                   'points':[[locs[0],locs[1]],[locs[2],locs[3]],[locs[4],locs[5]],[locs[6],locs[7]]],
                   'group_id':None,
                   'shape_type':'polygon',
                   'flags':{}}
            bboxes.append(bbox)

        json_dict = {'version': '4.4.0',
                     'flags': {},
                     'shapes': bboxes,
                     'imagePath': os.path.basename(img_path),
                     'imageData': img_data,
                     'imageHeight': im.size[1],
                     'imageWidth': im.size[0]}

        with open(os.path.join(output_labelme_dir,base_name+'.json'), 'w') as outfile:
            json.dump(json_dict, outfile)


if __name__ == "__main__":
    img_dir = '/data_backup/cuongnd/Viettel_freeform/sale_contract/crawl_data_internet/imgs'
    icdar_anno_dir = '/data_backup/cuongnd/Viettel_freeform/sale_contract/crawl_data_internet/icdar'
    output_labelme_dir = '/data_backup/cuongnd/Viettel_freeform/sale_contract/crawl_data_internet/json_entity'

    txt2labelme(img_dir=img_dir,
                icdar_anno_dir=icdar_anno_dir,
                output_labelme_dir=output_labelme_dir,
                default_class=None)
