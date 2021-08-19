import time
import pyautogui

def Sendmessages():
    time.sleep(4)
    text = open('messages.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")

def generate_message(text,total):
    
    with open(r"messages.txt","w") as f:
        for i in range(total):
            f.write(text+"\n")

if __name__ == '__main__':
    text = str(input("Enter the text you want to Spam : "))
    total = int(input("Enter how many time you want to spam : "))
    generate_message(text,total)
    Sendmessages()

