# conversion_tools
Collection of tools to convert dataset

### icdar format
1.txt
72,25,326,25,326,64,72,64,TAN WOON YANN
50,82,440,82,440,121,50,121,BOOK TA .K(TAMAN DAYA) SDN BND
205,121,285,121,285,139,205,139,789417-W
110,144,383,144,383,163,110,163,NO.53 55,57 & 59, JALAN SAGU 18,
192,169,299,169,299,187,192,187,TAMAN DAYA,

### yolo format

### voc format
1.xml
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


## Detection
### Yolo2Pascal-Annotation-Conversion

Perform conversion between YOLO annotation format and Pascal VOC format. Code based on [LabelImage](https://github.com/tzutalin/labelImg) repo. Images must be in .jpg format.

### Usage:
- Convert from YOLO to Pascal annotation format: The script will search for all .txt files in the folder and perform the conversion. 
Converted Pascal annotation files will have the same name and in the same directory.
  - ```python3 yolo2voc.py \path\to\folder\containing\images\and\yolo\label\files```
- Convert from Pascal to Yolo annotation format: The script will search for all .xml files in the folder and perform the conversion. 
The script requires to have the file class.txt describing all classes (this file is generated autonomously if using the LabelImage tool above for annotating images).
  - ```python3 voc2yolo.py \path\to\folder\containing\images\and\pascal\label\files```
  - Example of class.txt file:
    - bottle
    - can
    - cup
    - glass

### TODO:
- [ ] Remove Qt dependency
- [ ] Add more on Readme
- [ ] Add support for different image formats
- [ ] Add example images

