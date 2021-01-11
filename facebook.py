import pyautogui
import time

message=2
while message>0:
    time.sleep(4)
    pyautogui.typewrite("hi,hello,welcome!!!")
    time.sleep(2)
    pyautogui.press('enter')
    message=message-1


