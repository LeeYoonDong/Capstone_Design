# Import necessary libraries
from djitellopy import tello
from keras.models import load_model
from time import sleep, strftime
import cv2
import keyboardM
import numpy as np

# Initialize Drone
drone = tello.Tello()
drone.connect()
drone.streamon()
print('Battery:', drone.get_battery())

# Load Model
np.set_printoptions(suppress=True)
class_names = open("/home/dev/Capstone/labels.txt", "r").readlines()
model = load_model("/home/dev/Capstone/keras_model.h5", compile=False)
face_cascade = cv2.CascadeClassifier('/home/dev/Capstone/haarcascade_frontalface_default.xml')
keyboardM.init()

def getInput():
    left_right, front_back, up_down, clock_counter = 0, 0, 0, 0

    if keyboardM.getKey("a"): left_right = -50
    if keyboardM.getKey("d"): left_right = 50
    if keyboardM.getKey("w"): front_back = 50
    if keyboardM.getKey("s"): front_back = -50

    if keyboardM.getKey("i"): up_down = 50
    if keyboardM.getKey("k"): up_down = -50
    if keyboardM.getKey("j"): clock_counter = -50
    if keyboardM.getKey("l"): clock_counter = 50

    if keyboardM.getKey("UP"): drone.takeoff()
    if keyboardM.getKey("DOWN"): drone.land()

    if keyboardM.getKey("c"):
        filename = strftime("%Y년%m월%d일-%H시%M분%S초") + ".png"
        cv2.imwrite('/home/dev/Capstone/LP_OCR' + "/" + filename, drone.get_frame_read().frame)
        cv2.imwrite('/home/dev/Capstone/LP_IMG' + "/" + filename, drone.get_frame_read().frame)
        print("Image saved as", filename)

    return [left_right, front_back, up_down, clock_counter]

while True:
    frame = drone.get_frame_read().frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_img = gray[y:y + w, x:x + w]
        face_img = cv2.resize(face_img, (224, 224), interpolation=cv2.INTER_AREA)
        face_img = np.asarray(face_img, dtype=np.float32)
        face_img = np.expand_dims(face_img, axis=2)  # add a new axis along axis=2
        face_img = np.repeat(face_img, 3, axis=2)  # repeat along the new axis
        face_img = np.expand_dims(face_img, axis=0)  # add a batch dimension
        face_img = (face_img / 127.5) - 1

        prediction = model.predict(face_img)
        index = np.argmax(prediction)
        class_name = class_names[index].strip()
        confidence_score = prediction[0][index]
        if confidence_score >= 0.90:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, class_name[2:] + " " + str(np.round(confidence_score * 100))[:-2] + "%", (x, y - 10), \
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            print('Find Target')
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Display frame and handle keyboard control
    cv2.imshow("Drone Image", frame)
    results = getInput()
    drone.send_rc_control(results[0], results[1], results[2], results[3])

    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

drone.streamoff()
drone.end()
cv2.destroyAllWindows()
