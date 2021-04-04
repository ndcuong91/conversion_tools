import glob, os
from PIL import Image
from tqdm import tqdm
import json
import base64


def labelme2txt(img_dir, labelme_anno_dir, output_icdar_dir, ext=['jpg', 'JPG', 'PNG', 'png'], default_class='text'):
    for json_path in tqdm(glob.glob(labelme_anno_dir + '/*.json')):
        base_name = os.path.basename(json_path).replace('.json', '')
        print('labelme2txt. Convert', base_name)
        for ex in ext:
            if os.path.exists(os.path.join(img_dir, base_name + '.' + ex)):
                img_path = os.path.join(img_dir, base_name + '.' + ex)
                break

        icdar_txt = ''
        with open(json_path) as json_file:
            data = json.load(json_file)
            shapes = data["shapes"]
            for shape in shapes:
                point = shape["points"]
                label = shape["label"]
                line = ','.join([str(point[0][0]),
                                 str(point[0][1]),
                                 str(point[1][0]),
                                 str(point[1][1]),
                                 str(point[2][0]),
                                 str(point[2][1]),
                                 str(point[3][0]),
                                 str(point[3][1]),
                                 label])
                icdar_txt += line + '\n'

        with open(os.path.join(output_icdar_dir, base_name + '.txt'), mode = 'w', encoding='utf-8') as f:
            f.write(icdar_txt)


if __name__ == "__main__":
    img_dir = '/media/duycuong/Data/ocr_data/detector/invoices_SDV/textline_icdar_9May/test_images'
    labelme_anno_dir = '/media/duycuong/Data/ocr_data/detector/invoices_SDV/textline_icdar_9May/test_gts_labelme'
    output_icdar_dir = '/media/duycuong/Data/ocr_data/detector/invoices_SDV/textline_icdar_9May/test_gt2'

    labelme2txt(img_dir=img_dir,
                labelme_anno_dir=labelme_anno_dir,
                output_icdar_dir=output_icdar_dir)
