import time
import pyautogui

def Sendmessages():
    time.sleep(4)
    text = open('messages.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")


if __name__ == '__main__':
    Sendmessages()

with open(r"messages.txt","w") as f:
    for i in range(100):
        f.write("Hi\n")
