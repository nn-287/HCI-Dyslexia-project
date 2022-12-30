import numpy as np
import cv2
import socket
import pickle

ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}



socket = socket.socket()
hostname = '127.0.0.1'
port = 65434
socket.bind((hostname, port))

serverAddress = ((hostname, port))

socket.listen(5)

conn, addr = socket.accept()
print("device connected")






def Dispaly_ARUCO(corners, ids, rejected, image):
    if len(corners) > 0:  # Lama Yela2y el corners .

        for (markerCorner, markerID) in zip(corners, ids):  # Ha n loop over the ArUCo corners detected

            corners = markerCorner.reshape((4, 2))  # Extract the marker corners (TL,TR,BL,BR)
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            topRight = (int(topRight[0]), int(topRight[1]))  # convert each of the (x, y) to integers
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))



            # Center for each

            a = int((topLeft[0] + bottomRight[0]) / 2.0)
            b = int((topLeft[1] + bottomRight[1]) / 2.0)
            (cv2.circle(image, (a, b), 4, (0, 0, 255), -1))
            #print(a,b)
            # Data1 = str.encode(str(a))
            list = [a, b]

            print(list)
            list = str.encode(str(list))
            conn.send(list)






            cv2.putText(image, str(markerID), (topLeft[0], topLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                        2)
           #print("Marker ID: {}".format(markerID))



    return image


aruco_type = "DICT_5X5_50"

size = 200

aruco_dict = cv2.aruco.Dictionary_get(ARUCO_DICT[aruco_type])

aruco_param = cv2.aruco.DetectorParameters_create()

vid = cv2.VideoCapture(0)

while vid.isOpened():

    ret, img = vid.read()

    height, width, _ = img.shape

    # width=1000
    height = int(width * (height / width))

    corners, ids, rejected = cv2.aruco.detectMarkers(img, aruco_dict, parameters=aruco_param)

    detected_markers = Dispaly_ARUCO(corners, ids, rejected, img)

    cv2.imshow("Image", detected_markers)

    k = cv2.waitKey(1) & 0xFF

    if (k == 27):
        break

vid.release()

cv2.destroyAllWindows()



