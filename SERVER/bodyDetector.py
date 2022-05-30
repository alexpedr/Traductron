# -*- coding: utf-8 -*-
"""
Created on Sat May 28 11:23:28 2022

@author: PC
"""

import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# For static images:
IMAGE_FILES = []
BG_COLOR = (192, 192, 192) # gray
with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5) as pose:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image_height, image_width, _ = image.shape
    # Convert the BGR image to RGB before processing.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.pose_landmarks:
      continue
    print(
        f'Nose coordinates: ('
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
    )
    print(results.pose_landmarks)
    annotated_image = image.copy()
    # Draw segmentation on the image.
    # To improve segmentation around boundaries, consider applying a joint
    # bilateral filter to "results.segmentation_mask" with "image".
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
    bg_image = np.zeros(image.shape, dtype=np.uint8)
    bg_image[:] = BG_COLOR
    annotated_image = np.where(condition, annotated_image, bg_image)
    # Draw pose landmarks on the image.
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
    # Plot pose world landmarks.
    mp_drawing.plot_landmarks(
        results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    lm = results.pose_landmarks
    lmPose = mp_pose.PoseLandmark
    
    h, w = image.shape[:2]
    
    if lm is not None:
        l_shldr_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
        l_shldr_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
        
        r_shldr_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * w)
        r_shldr_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * h)
    
        r_hand_x =  int(lm.landmark[lmPose.RIGHT_WRIST].x * w)
        r_hand_y =  int(lm.landmark[lmPose.RIGHT_WRIST].y * h)
        
        l_hand_x =  int(lm.landmark[lmPose.LEFT_WRIST].x * w)
        l_hand_y =  int(lm.landmark[lmPose.LEFT_WRIST].y * h)
    #print(r_hand_y)
        if(r_hand_y > h and r_hand_x < w/5):
            print("Bajar camara a la derecha")
        elif(r_hand_y > h and r_hand_x > 4*w/5):
            print("Bajar camara a la izquierda")
        elif(r_hand_y < h/3 and r_hand_x < w/5):
            print("Subir camara a la derecha")
        elif(r_hand_x > 4*w/5 and r_hand_y < h/3):
            print("Subir camara a la izquierda")
        elif(r_hand_y < h/3):
            print("Subir camara")
        elif(r_hand_y > h):
            print("Bajar camara")
        elif(r_hand_x < w/5):
            print("Girar camara a la derecha")
        elif(r_hand_x > 4*w/5):
            print("Girar camara a la izquierda")
        elif(r_hand_x > w/5 and r_hand_x < 4*w/5 and r_hand_y < h and r_hand_y > h/3):
            print("Quieto")
    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()