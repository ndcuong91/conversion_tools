import os, cv2
import PIL
import numpy as np
def convert_voc_label_to_normal_format(src_anno_dir, dst_anno_dir):
    print('convert_voc_label_to_normal_format')
    print('src_anno_dir',src_anno_dir)
    print('dst_anno_dir',dst_anno_dir)


    list_images = get_list_file_in_folder(src_anno_dir)
    list_images = sorted(list_images)
    for idx, file in enumerate(list_images):
        print(idx, file)
        src_img_path=os.path.join(src_anno_dir,file)
        dst_img_path=os.path.join(dst_anno_dir,file)
        lbl = np.asarray(PIL.Image.open(src_img_path))
        cv2.imwrite(dst_img_path, lbl)

