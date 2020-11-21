
import cv2
import numpy as np
from tensorflow_yolov3.carla.config import cfg
from tensorflow_yolov3.carla.utils import read_class_names
import os
import time


class Sign:
    state = None
    classes = None
    bbx = []
    scores = []
    def __init__(self):
        self.classes = read_class_names(cfg.YOLO.CLASSES)
    
    def __del__(self):
        pass
    
    def getScore_Label(self, bboxes):
        if len(bboxes) == 0:
            return
        else:
            bbox = bboxes[0]
            self.bbx.append([int(bbox[1]), int(bbox[3]), int(bbox[0]) , int(bbox[2])])
            self.scores.append(bbox[4])
    
    def process_traffic_sign(self, frame, bboxes):
        if len(bboxes) != 0:
            self.getScore_Label(bboxes)
            signs = np.zeros_like(frame)
            for i in self.bbx:
                signs = frame[i[0]:i[1], i[2]:i[3]]

            if(signs.shape[0] > 0 and signs.shape[1] > 0):
                cv2.imshow("Traffic Sign", signs)
                qtd = len(os.listdir('./data/'))
                for i in range(10): 
                    cv2.imwrite('data/traffic_sign_{}_{}.jpg'.format(qtd ,i+1), signs)
                cv2.waitKey(1)# & 0xFF

    def filter_traffic_sign(self, bboxes):
        for i, bbox in enumerate(bboxes):
            if(self.classes[bbox[5]] == "stop sign"):
                return [bbox]
        return []
