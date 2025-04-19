import pyautogui
import time
from pynput import keyboard
import csv
import os
import threading
import numpy as np
from PIL import Image


os.makedirs('dataset', exist_ok=True)
csv_file = open('key_log2.csv', mode='a', newline='')
csv_writer = csv.writer(csv_file)

keys_held = set()
screenshot_count = 0
running = True

def on_press(key):
    keys_held.add(key)

def on_release(key):
    if key in keys_held:
        keys_held.remove(key)
    if key == keyboard.Key.esc:
        global running
        running = False
        return False

def capture_loop():
    global screenshot_count
    while running:
        time.sleep(1)
        path = f'dataset_new2/my_screenshot_{screenshot_count}.png'
        screenshot = pyautogui.screenshot(path,region=(797,808, 900, 700))
        
        
        
        img_array = np.array(screenshot) / 255.0  
        img_array = img_array.flatten()  

        if keys_held:
            key = list(keys_held)[0]
            if hasattr(key, 'char'):
                key_str = key.char
            else:
                key_str = str(key)
            
            if key_str == 'w':
                steer = 0.0
                throttle = 1.0
                brake = 0.0
            elif key_str == 'a':
                steer = -1.0
                throttle = 1.0
                brake = 0.0
            elif key_str == 'd':
                steer = 1.0
                throttle = 1.0
                brake = 0.0
            elif key_str == 's':
                steer = 0.0
                throttle = 0.0
                brake = 1.0
            else:
                steer = 0.0
                throttle = 0.0
                brake = 0.0
        else:
            steer = 0.0
            throttle = 0.0
            brake = 0.0
        

        csv_writer.writerow([path, steer, throttle, brake])
        csv_file.flush()
        print(f"Captured {path} with steer={steer}, throttle={throttle}, brake={brake}")
        screenshot_count += 1


threading.Thread(target=capture_loop, daemon=True).start()


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

csv_file.close()
