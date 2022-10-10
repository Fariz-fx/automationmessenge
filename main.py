import pyautogui
#for naturalway of typing importing time
import time
#For infinite running the loop
while True:
    # for waiting 3 sec
    time.sleep(3)
    # This code will type a line
    pyautogui.typewrite('Testing automation')
    # This will press enter
    pyautogui.press('enter')

# Keep your cursor on mentioned screen