Each json file correspond to a folder

The COCO dataset is formatted in JSON and is a collection of “info”, “licenses”, “images”, “annotations”, “categories” (in most cases), and “segment info” (in one case).

{
    "info": {...},
    "licenses": [...],
    "images": [...],
    "annotations": [...],
    "categories": [...], <-- Not in Captions annotations
    "segment_info": [...] <-- Only in Panoptic annotations
}
INFO
The “info” section contains high level information about the dataset. If you are creating your own dataset, you can fill in whatever is appropriate.

"info": {
    "description": "COCO 2017 Dataset",
    "url": "http://cocodataset.org",
    "version": "1.0",
    "year": 2017,
    "contributor": "COCO Consortium",
    "date_created": "2017/09/01"
}
LICENSES
The “licenses” section contains a list of image licenses that apply to images in the dataset. If you are sharing or selling your dataset, you should make sure your licenses are correctly specified and that you are not infringing on copyright.

"licenses": [
    {
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License"
    },
    {
        "url": "http://creativecommons.org/licenses/by-nc/2.0/",
        "id": 2,
        "name": "Attribution-NonCommercial License"
    },
    ...
]
IMAGES
The “images” section contains the complete list of images in your dataset. There are no labels, bounding boxes, or segmentations specified in this part, it's simply a list of images and information about each one.  Note that coco_url, flickr_url, and date_captured are just for reference. Your deep learning application probably will only need the file_name.

Note that image ids need to be unique (among other images), but they do not necessarily need to match the file name (unless the deep learning code you are using makes an assumption that they’ll be the same… developers are lazy, it wouldn’t surprise me).

"images": [
    {
        "license": 4,
        "file_name": "000000397133.jpg",
        "coco_url": "http://images.cocodataset.org/val2017/000000397133.jpg",
        "height": 427,
        "width": 640,
        "date_captured": "2013-11-14 17:02:52",
        "flickr_url": "http://farm7.staticflickr.com/6116/6255196340_da26cf2c9e_z.jpg",
        "id": 397133
    },
    {
        "license": 1,
        "file_name": "000000037777.jpg",
        "coco_url": "http://images.cocodataset.org/val2017/000000037777.jpg",
        "height": 230,
        "width": 352,
        "date_captured": "2013-11-14 20:55:31",
        "flickr_url": "http://farm9.staticflickr.com/8429/7839199426_f6d48aa585_z.jpg",
        "id": 37777
    },
    ...
]
FIVE COCO ANNOTATION TYPES
According to cocodataset.org/#format-data:

COCO has five annotation types: for object detection, keypoint detection, stuff segmentation, panoptic segmentation, and image captioning. The annotations are stored using JSON.

The documentation on the COCO annotation format isn’t crystal clear, so I’ll break them down as simply as I can. Each one is a little different.

OBJECT DETECTION (SEGMENTATION)
http://cocodataset.org/#detection-2018
http://cocodataset.org/#detection-2018

This is the most popular one; it draws shapes around objects in an image. It has a list of categories and annotations.

CATEGORIES
The “categories” object contains a list of categories (e.g. dog, boat) and each of those belongs to a supercategory (e.g. animal, vehicle). The original COCO dataset contains 90 categories. You can use the existing COCO categories or create an entirely new list of your own. Each category id must be unique (among the rest of the categories).

"categories": [
    {"supercategory": "person","id": 1,"name": "person"},
    {"supercategory": "vehicle","id": 2,"name": "bicycle"},
    {"supercategory": "vehicle","id": 3,"name": "car"},
    {"supercategory": "vehicle","id": 4,"name": "motorcycle"},
    {"supercategory": "vehicle","id": 5,"name": "airplane"},
    ...
    {"supercategory": "indoor","id": 89,"name": "hair drier"},
    {"supercategory": "indoor","id": 90,"name": "toothbrush"}
]
ANNOTATIONS
The “annotations” section is the trickiest to understand. It contains a list of every individual object annotation from every image in the dataset. For example, if there are 64 bicycles spread out across 100 images, there will be 64 bicycle annotations (along with a ton of annotations for other object categories). Often there will be multiple instances of an object in an image. Usually this results in a new annotation item for each one.

I say “usually” because regions of interest indicated by these annotations are specified by “segmentations”, which are usually a list of polygon vertices around the object, but can also be a run-length-encoded (RLE) bit mask. Typically, RLE is used for groups of objects (like a large stack of books). I’ll explain how this works later in the article.

Area is measured in pixels (e.g. a 10px by 20px box would have an area of 200).

Is Crowd specifies whether the segmentation is for a single object or for a group/cluster of objects.

The image id corresponds to a specific image in the dataset.

The COCO bounding box format is [top left x position, top left y position, width, height].

The category id corresponds to a single category specified in the categories section.

Each annotation also has an id (unique to all other annotations in the dataset).

The following JSON shows 2 different annotations.

The first annotation:

Has a segmentation list of vertices (x, y pixel positions)

Has an area of 702 pixels (pretty small) and a bounding box of [473.07,395.93,38.65,28.67]

Is not a crowd (meaning it’s a single object)

Is category id of 18 (which is a dog)

Corresponds with an image with id 289343 (which is a person on a strange bicycle and a tiny dog)

The second annotation:

Has a Run-Length-Encoding style segmentation

Has an area of 220834 pixels (much larger) and a bounding box of [0,34,639,388]

Is a crowd (meaning it’s a group of objects)

Is a category id of 1 (which is a person)

Corresponds with an image with id 250282 (which is a vintage class photo of about 50 school children)




"annotations": [
    {
        "segmentation": [[510.66,423.01,511.72,420.03,...,510.45,423.01]],
        "area": 702.1057499999998,
        "iscrowd": 0,
        "image_id": 289343,
        "bbox": [473.07,395.93,38.65,28.67],
        "category_id": 18,
        "id": 1768
    },
    ...
    {
        "segmentation": {
            "counts": [179,27,392,41,…,55,20],
            "size": [426,640]
        },
        "area": 220834,
        "iscrowd": 1,
        "image_id": 250282,
        "bbox": [0,34,639,388],
        "category_id": 1,
        "id": 900100250282
    }
]