
import numpy as np
from PIL import ImageGrab, Image
import pydirectinput
import time
import pickle


with open("weights.pkl", "rb") as f:
    w, b = pickle.load(f)

def predict(x, w, b):
    return np.dot(x, w) + b


def control_vehicle(pred):
    steer, throttle, brake = pred
    if steer < -0.2:
        print('left')
        pydirectinput.keyDown('left')
        time.sleep(1)
        pydirectinput.keyUp('left')
    elif steer > 0.2:
        print('right')
        pydirectinput.keyDown('right')
        time.sleep(1)
        pydirectinput.keyUp('right')
    
    if throttle > 0.5:
        pydirectinput.keyDown('up')
        time.sleep(2)
        pydirectinput.keyUp('up')
    
    if brake > 0.5:
        pydirectinput.press('down')


while True:
    img = ImageGrab.grab().convert('L').resize((64, 48))
    img_array = np.array(img).flatten() / 255.0
    img_array = img_array.reshape(1, -1)

    pred = predict(img_array, w, b)[0]
    control_vehicle(pred)

    time.sleep(1)  
