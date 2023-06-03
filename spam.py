import pyautogui
import time
import keyboard
from art import *

tprint("Use with Caution",font="random")
tprint("Using this script may lead to account ban in some platforums,because they would assume a bot is using the account. So atleast use 2 Seconds of pause \n", font="rnd-small")
msg = input("Enter the massage \n")

n = int(input("How many times ?: "))

t = int(input("Pause between each massage,in Seconds ? \n"))

time.sleep(8)

print("Wait for 8 Seconds \n ")
print("Press 'X' to escape at anypoint")


for i in range(n):
        pyautogui.typewrite(msg + '\n')
        time.sleep(t)
        if keyboard.is_pressed('x'):
                print("code is exiting because exit key has been pressed")
                exit()
