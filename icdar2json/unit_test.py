import unittest
from voc2icdar import *
import glob
import os
class TestFunctions(unittest.TestCase):

    def test_reader(self):
        pt_labels=read_json("labels/609042.json")
        final_label = pt_labels_to_string(pt_labels)
        print(final_label)
    def test_translate_foldr(self):
        sources = glob.glob("labels/*.json")
        for path in sources:
            pt_labels = read_json(path)
            json_name = (path.split("/")[-1]).split(".")[0]+".txt"
            final_label = pt_labels_to_string(pt_labels)
            destination_path = os.path.join("icdar_label",json_name)
            file = open(destination_path,"w")
            file.write(final_label)
            file.close()

        print(sources)