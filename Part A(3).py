#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mediapipe


# In[1]:


import cv2


# In[ ]:


cap=cv2.VideoCapture('http://192.168.1.3:8080/video')


# In[2]:


import math
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt


# In[3]:


mp_pose=mp.solutions.pose
pose=mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
mp_drawing=mp.solutions.drawing_utils


# In[4]:


def detectpose(image,pose,display=True):
    
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


# In[5]:


image=cv2.imread("pr.jpg")
detectpose(image,pose,display=True)


# In[6]:


pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)



video = cv2.VideoCapture(0)#'http://192.168.1.3:8080/video'



video.set(3,1280)
video.set(4,960)



while video.isOpened():
    
    ok, frame = video.read()
    
    if not ok:
        
        break
        
        
    frame = cv2.flip(frame,1)
    
    frame_height, frame_width, _ = frame.shape
    
    
    
    frame, _ = detectpose(frame, pose_video, display=False)
    
    time2 = time()
    
   
    cv2.imshow('Landmarks detection', frame)
        
    k=cv2.waitKey(1) & 0xFF
        
    if(k==27):
        
        break
            
            
video.release()

cv2.destroyAllWindows()


# In[7]:


def CalculateAngle(ld1,ld2,ld3):
    
    x1, y1, _ = ld1
    x2, y2, _ = ld2
    x3, y3, _ = ld3

    angle=math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))


    #if angle < 0:
        
        #angle+=360
    return angle


# In[7]:


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



    if left_knee_angle > 90 and left_knee_angle < 110 or right_knee_angle > 90 and right_knee_angle < 110:
        
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




# In[9]:


image=cv2.imread("amar.jpg")
output,landmarks=detectpose(image,pose,display=False)
if landmarks:
    
    PoseClassification(landmarks,output,display=True)
    


# In[10]:


image=cv2.imread("b.jpg")
output,landmarks=detectpose(image,pose,display=False)
if landmarks:
    
    PoseClassification(landmarks,output,display=True)


# In[33]:


image=cv2.imread("o2.jpg")
output,landmarks=detectpose(image,pose,display=False)
if landmarks:
    
    PoseClassification(landmarks,output,display=True)


# In[34]:


image=cv2.imread("o.jpg")
output,landmarks=detectpose(image,pose,display=False)
if landmarks:
    
    PoseClassification(landmarks,output,display=True)


# In[19]:


#image=cv2.imread("c2.jpg")
#output,landmarks=detectpose(image,pose,display=False)
#if landmarks:
    
    #PoseClassification(landmarks,output,display=True)


# In[ ]:


pose_video=mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

camera_video=cv2.VideoCapture(0)#'http://192.168.1.3:8080/video'

camera_video.set(3,1280)

camera_video.set(4,960)









while camera_video.isOpened():
    
    ok, frame = camera_video.read()
    
    if not ok:
        
        break
    
    frame=cv2.flip(frame,1)
    
    
    frame_height , frame_width, _ = frame.shape
     
    
    frame=cv2.resize(frame,(int(frame_width * (640 / frame_height)),640))
    
    
    frame, landmarks = detectpose(frame, pose_video, display=False)
    
    if landmarks:
        
        frame, _ = PoseClassification(landmarks, frame, display=False)
        
    cv2.imshow("Movement classification",frame)
    
    k = cv2.waitKey(1) & 0xFF
    
    
    if(k==27):
            
            break

camera_video.release()

cv2.destroyAllWindows()
    


# In[ ]:




