from djitellopy import tello
from keras.models import load_model
import numpy as np
import cv2

drone = tello.Tello()
drone.connect()
drone.streamon()
np.set_printoptions(suppress=True)
class_names = open("labels.txt", "r").readlines()
model = load_model("keras_Model.h5", compile=False)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    frame = drone.get_frame_read().frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        face_img = gray[y:y+w, x:x+w]
        face_img = cv2.resize(face_img, (224, 224), interpolation=cv2.INTER_AREA)
        face_img = np.asarray(face_img, dtype=np.float32)
        face_img = np.expand_dims(face_img, axis=2)  # add a new axis along axis=2
        face_img = np.repeat(face_img, 3, axis=2)   # repeat along the new axis
        face_img = np.expand_dims(face_img, axis=0)  # add a batch dimension
        face_img = (face_img / 127.5) - 1

        prediction = model.predict(face_img)
        index = np.argmax(prediction)
        class_name = class_names[index].strip()
        confidence_score = prediction[0][index]
        if confidence_score >= 0.90:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, class_name[2:] + " " + str(np.round(confidence_score * 100))[:-2] + "%", (x, y-10),\
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            print('Find Taget')
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        else:
            None



    cv2.imshow("Drone Image", frame)
    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

drone.streamoff()
drone.end()
cv2.destroyAllWindows()
