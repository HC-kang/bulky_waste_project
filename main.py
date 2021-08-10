import cv2
import mediapipe as mp
import time

import os
os.chdir('/Users/heechankang/projects/pythonworkspace/pushupcounter/testVideo')

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


#cap = cv2.VideoCapture('testVideo01.mp4')
# cap = cv2.VideoCapture('testVideo02.mp4')
cap = cv2.VideoCapture('/Users/heechankang/Downloads/SENORITA.mp4')
# cap = cv2.VideoCapture(1)
pTime = 0
out = cv2.VideoWriter('SENORITA_mediapipe.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (854, 480))
while cap.isOpened():
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    img_height, img_width, _ = img.shape
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        # for id, lm in enumerate(img, results.pose_landmarks.landmark):
        #     h, w, c = img.shape
        #     print(id, lm)
        #     cx, cy = int(lm.x * w), int(lm.y * h)
        #     cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow('Image', img)
    out.write(img)
    cv2.waitKey(10)
    cv2.destroyAllWindows()
cap.release()
out.release()