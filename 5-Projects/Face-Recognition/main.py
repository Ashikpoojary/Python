#dependencies
'''
pip install cmake
pip install face_recognition
pip install opencv-python
pip install numpy
'''

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load Known Faces