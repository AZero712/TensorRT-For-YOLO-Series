from yolo_trt.yolo_trt import preproc, vis
from yolo_trt.yolo_trt import BaseEngine
import numpy as np
import cv2
import time
import os
import argparse
# import yolo_trt 

class Predictor(BaseEngine):
    def __init__(self, engine_path):
        super(Predictor, self).__init__(engine_path)
        self.n_classes = 1  # your model classes
        self.class_names = ['test'] # your model class names

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--engine", help="TRT engine Path")
    parser.add_argument("-i", "--image", help="image path")
    parser.add_argument("-o", "--output", help="image output path")
    parser.add_argument("-v", "--video",  help="video path or camera index ")
    parser.add_argument("--end2end", default=False, action="store_true",
                        help="use end2end engine")

    args = parser.parse_args()
    print(args)

    pred = Predictor(engine_path=args.engine)
    pred.get_fps()
    img_path = args.image
    video = args.video
    if img_path:
      origin_img = cv2.imread(img_path)
      result, origin_img = pred.inference(origin_img, conf=0.1, end2end=args.end2end, is_return_img=True)
      print(result)
      # result = pred.inference(img_path, conf=0.1, end2end=args.end2end)
      cv2.imwrite("%s" %args.output , origin_img)
    if video:
      pred.detect_video(video, conf=0.1, end2end=args.end2end) # set 0 use a webcam
