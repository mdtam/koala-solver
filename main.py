import pyautogui
import time
import keyboard
import json

def get_position(prompt):
    time.sleep(0.5)
    print(prompt)
    while True:
        if keyboard.is_pressed('enter'):
            return pyautogui.position()

def save_positions(top_left, bottom_right, filename="positions.json"):
    data = {"top_left": top_left, "bottom_right": bottom_right}
    with open(filename, "w") as file:
        json.dump(data, file)

def load_positions(filename="positions.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def scan_area(top_left, bottom_right, repetitions=8):
    width = bottom_right[0] - top_left[0]
    height = bottom_right[1] - top_left[1]
    
    for _ in range(repetitions):
        for y in range(top_left[1], bottom_right[1] + 1, 5):  # Move in steps of 5 pixels
            pyautogui.moveTo(top_left[0], y)
            pyautogui.moveTo(bottom_right[0], y)
            # for x in range(top_left[0], bottom_right[0] + 1, 5):
        time.sleep(0.5)  # Pause briefly between repetitions

def main():
    positions = load_positions()
    
    if positions:
        print("Loaded positions from file.")
        top_left = tuple(positions["top_left"])
        bottom_right = tuple(positions["bottom_right"])
    else:
        print("Move mouse to the top-left corner and press Enter...")
        top_left = get_position("Captured top-left corner.")
        
        print("Move mouse to the bottom-right corner and press Enter...")
        bottom_right = get_position("Captured bottom-right corner.")
        
        save_positions(top_left, bottom_right)
        print("Positions saved to file.")
    
    print("Starting scan in 2 seconds...")
    time.sleep(2)
    scan_area(top_left, bottom_right)
    print("Scanning complete. Exiting...")

if __name__ == "__main__":
    main()
