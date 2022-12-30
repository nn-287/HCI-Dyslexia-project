import cv2
import mediapipe as mp
import pyautogui as pyautogui

video = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

while True:

    _, frame = video.read()

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = face_mesh.process(rgb)

    landmark_points = output.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    print(landmark_points)

    if landmark_points:

        landmarks = landmark_points[0].landmark

        for id, landmark in enumerate(landmarks[474:478]):

            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

            if id == 1:
                pyautogui.moveTo(x, y)

            # print(x,y)

    cv2.imshow('test', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()