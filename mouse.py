import pyautogui
import time

print("Move your mouse to the desired position. You have 5 seconds...")
time.sleep(5)  # Gives you time to move the cursor

x, y = pyautogui.position()  # Get current mouse position
print(f"Mouse Position: {x}, {y}")
