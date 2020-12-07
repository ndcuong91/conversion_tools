Collection of tools to convert detection, segmentation dataset
## I. Detection
### icdar format (.txt)
```
72,25,326,25,326,64,72,64,TAN WOON YANN
50,82,440,82,440,121,50,121,BOOK TA .K(TAMAN DAYA) SDN BND
205,121,285,121,285,139,205,139,789417-W
110,144,383,144,383,163,110,163,NO.53 55,57 & 59, JALAN SAGU 18,
192,169,299,169,299,187,192,187,TAMAN DAYA,
```

### yolo format (.txt)
```
0 45 55 29 67
1 99 83 28 44
```

### voc format (.xml)

```
<annotation>
	<folder>images</folder>
	<filename>SCAN_20191128_145142994_001.jpg</filename>
	<path>abc</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>2481</width>
		<height>3507</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>học</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>983</xmin>
			<ymin>415</ymin>
			<xmax>1118</xmax>
			<ymax>489</ymax>
		</bndbox>
	</object>
	<object>
		<name>sacramento</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1238</xmin>
			<ymin>411</ymin>
			<xmax>1581</xmax>
			<ymax>488</ymax>
		</bndbox>
	</object>
</annotation>
```

### coco format (.xml)
```
annotation{
"id" : int,
"image_id": int,
"category_id": int,
"segmentation": RLE or [polygon],
"area": float,
"bbox": [x,y,width,height],
"iscrowd": 0 or 1,
}
categories[{
"id": int,
"name": str,
"supercategory": str,
}]
```

## II. Segmentation

| |  **COCO to** |  **normal to** |  **PascalVOC to** |   **labelme to**|
| -------------------- | --------- | -------- | -------- | ------- |
| **COCO**   | x   | -    | -  | o        |
| **normal**    |  | x | o |  |
| **PascalVOC**    |  |  | x | o |
| **labelme**    | o |  |  | x |