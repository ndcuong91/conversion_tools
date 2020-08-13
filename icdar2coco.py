import os, json, random

indir='.'
anno_dir = os.path.join(indir, 'anno_DB')
img_dir = os.path.join(indir, 'images')
cat = [{"form":0, "serial":1, "no":2, "date":3, "tax_code":4, "address":5, "buyer":6, "company_name":7, 
        "exchange_rate":8, "total": 9, "grand_total": 10, "amount_in_words": 11, "label": 12}]

def export2json(_in, _out):
    savejson = {}
    imgs = []
    anno = []
    idx = 0
    for i, img in enumerate(_in):
        imgs.append({"id":i, "file_name": os.path.join(img_dir, img)})
        for line in open(os.path.join(anno_dir, img.replace(".jpg","").replace(".png", "") + ".txt")).readlines():
            #print(img)
            left, top, right, top, right, bottom, left, bottom, val = line.split(',')
            anno.append({
                "id": idx,
                "image_id": i,
                "category_id": cat[0][val.strip()],
                "bbox": [int(left), int(top), int(right)-int(left), int(bottom)-int(top)],
                "area": (float(right)-int(left)) * (float(bottom)-int(top)),
                "iscrowd":0
                })
    savejson["image"] = imgs
    savejson["annotations"] = anno
    savejson["categories"] = cat
    #print(savejson)
    with open(os.path.join(indir, _out), 'w', encoding='utf-8') as fd:
        json.dump(savejson, fd, ensure_ascii=False)
    return

files=[f for f in os.listdir(img_dir)]
print(len(files))
val_size = int(len(files)*0.1)
train_size = len(files) - val_size
random.shuffle(files)
train = files[0:train_size]
val = files[train_size:train_size+val_size]
try:
    export2json(train, 'train.json')
    export2json(val, 'val.json')
except Exception as e:
    print(e)
