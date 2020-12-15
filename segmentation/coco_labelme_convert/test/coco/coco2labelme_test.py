from annotation_utils.coco.structs import COCO_Dataset
import os

coco_data_dir='/data20.04/data/doc_structure/AICRv1_1_Test_subset_label_data_ori_preprocessed/solution_test_img_preprocessed'

dataset = COCO_Dataset.load_from_path(
    json_path=coco_data_dir+'.json',
    img_dir=coco_data_dir
)

for coco_ann in dataset.annotations:
    coco_image = dataset.images.get_images_from_imgIds([coco_ann.image_id])[0]
    coco_ann.bbox = coco_ann.bbox.scale_about_center(
        scale_factor=1.0,
        frame_shape=[coco_image.height, coco_image.width]
    )
# dataset.display_preview()
labelme_handler = dataset.to_labelme(priority='seg')

dst_dir = os.path.join(coco_data_dir,'labelme')
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

labelme_handler.save_to_dir(
    json_save_dir=dst_dir,
    src_img_dir=coco_data_dir,
    dst_img_dir=dst_dir
)