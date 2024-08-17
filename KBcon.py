from djitellopy import tello
from time import sleep, strftime
import cv2
import keyboardM


def getInput():
    left_right, front_back, up_down, clock_counter = 0, 0, 0, 0

    if keyboardM.getKey("a"): left_right = -150
    if keyboardM.getKey("d"): left_right = 150
    if keyboardM.getKey("w"): front_back = 150
    if keyboardM.getKey("s"): front_back = -150

    if keyboardM.getKey("i"): up_down = 150
    if keyboardM.getKey("k"): up_down = -150
    if keyboardM.getKey("j"): clock_counter = -150
    if keyboardM.getKey("l"): clock_counter = 150

    if keyboardM.getKey("UP"): drone.takeoff()
    if keyboardM.getKey("DOWN"): drone.land()

    if keyboardM.getKey("c"):
        filename = strftime("%Y년%m월%d일-%H시%M분%S초") + ".png"
        cv2.imwrite('TelloCaptures' + "/" + filename, drone.get_frame_read().frame)
        print("Image saved as", filename)
    if keyboardM.getKey("g"): drone.streamoff()

    return [left_right, front_back, up_down, clock_counter]


def video_stream():
    image = drone.get_frame_read().frame
    image = cv2.resize(image, (1280, 720))
    cv2.imshow("image", image)
    cv2.waitKey(1)

drone = tello.Tello()
drone.connect()
drone.streamon()
print('Battery:', drone.get_battery())
keyboardM.init()

while True:
    video_stream()
    results = getInput()
    drone.send_rc_control(results[0], results[1], results[2], results[3])

    print('Speed:', drone.get_speed_x(), 'km/h')

if drone.streamoff():
    drone.end(), cv2.destroyAllWindows()
