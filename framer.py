import cv2
 
capture = cv2.VideoCapture('vdo.mp4')
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
    if success:
        cv2.imwrite(f'C:/Edrive/projects/SimpleProjects/Framer/Frames/frame_{frameNr}.jpg', frame)
 
    else:
        break
    frameNr = frameNr+1
 
capture.release()