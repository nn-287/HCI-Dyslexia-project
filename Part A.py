#!/usr/bin/env python
# coding: utf-8

# In[30]:


pip install mediapipe


# In[51]:


import cv2


# In[52]:


import math
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt


# In[53]:


mp_pose=mp.solutions.pose
pose=mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
mp_drawing=mp.solutions.drawing_utils


# In[54]:


def detectpose(source,pose,display=True):
    out_put=image.copy()
    
    RGB=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    
    results=pose.process(RGB)
    
    height,width,_ = image.shape
    
    landmarks=[]
    
    if results.pose_landmarks:
        
        mp_drawing.draw_landmarks(image=out_put, landmark_list=results.pose_landmarks, connections=mp_pose.POSE_CONNECTIONS)
        
        for landmark in results.pose_landmarks.landmark:
            
            landmarks.append((int(landmark.x*width), int(landmark.y*height), (landmark.z*width)))
    
    if display:
        
        plt.figure(figsize=[22,22])
       
        
        plt.subplot(122);plt.imshow(out_put[:,:,::-1]);plt.title("Output image");plt.axis('off');
    
    else:
        
        return out_put,landmarks 
  


# In[35]:


image=cv2.imread("pr.jpg")
detectpose(image,pose,display=True)


# In[55]:


def CalculateAngle(ld1,ld2,ld3):
    
    x1, y1, _ = ld1
    x2, y2, _ = ld2
    x3, y3, _ = ld3

    angle=math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))


    #if angle < 0:
        
        #angle+=360
    return angle


# In[102]:


def PoseClassification(landmarks,output_img,display=False):
    
    
    label = 'Unknown'
    color = (0,0,250) #red label classification
    
    
    left_elbow_angle=CalculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value], landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value], landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])
    right_elbow_angle=CalculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value], landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value], landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])

    left_knee_angle=CalculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value], landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value], landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])
    right_knee_angle=CalculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value], landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value], landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    
    
    if left_elbow_angle > 10 and left_elbow_angle < 90 or right_elbow_angle > 10 and right_elbow_angle < 90:
        
        
        label="Bored"
    
    
    
    

    #



    if left_knee_angle > 90 and left_knee_angle < 120 or right_knee_angle > 90 and right_knee_angle < 120:
        
        label="Focused!" 



  #


    if left_knee_angle > 165 and left_knee_angle <195 or right_knee_angle > 165 and right_knee_angle < 195:
        
            
            label="Lost attention"




    if label !="Not Classified":
        
        color=(0,255,0)

    cv2.putText(output_img, label, (10,30), cv2.FONT_HERSHEY_PLAIN, 2, color,2)
    
    if display:
        
        plt.figure(figsize=[10,10])
        plt.imshow(output_img[:,:,::-1]);plt.title("output image");plt.axis('off');

    else:
        return output_img, label




# In[103]:


image=cv2.imread("amar.jpg")
output,landmarks=detectpose(image,pose,display=False)
if landmarks:
    
    PoseClassification(landmarks,output,display=True)
    


# In[104]:


image=cv2.imread("b.jpg")
output,landmarks=detectpose(image,pose,display=False)
if landmarks:
    
    PoseClassification(landmarks,output,display=True)


# In[105]:


image=cv2.imread("o2.jpg")
output,landmarks=detectpose(image,pose,display=False)
if landmarks:
    
    PoseClassification(landmarks,output,display=True)


# In[106]:


image=cv2.imread("o.jpg")
output,landmarks=detectpose(image,pose,display=False)
if landmarks:
    
    PoseClassification(landmarks,output,display=True)


# In[ ]:




