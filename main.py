from time import sleep
from termcolor import colored
import pyautogui
import random
import multiprocessing

print(colored("Welcome to AlwaysOn bot made by NullaSec!", "blue"))
sleep(1)

def move_mouse():
    for i in range(1, 600):
        y = random.randint(0, 600)
        x = random.randint(0, 600)
        pyautogui.moveTo(x, y)
        sleep(2)

timer_question = (input("Do you want to set a timer? (Y/N): ")).lower()
if timer_question == "y":
    timer = float(input(colored("Please enter the time in minutes: ", "green")))
    move_mouse()
    timer_p = multiprocessing.Process(target=move_mouse, name="move_mouse", args=(timer,))
    timer_p.start()
    sleep(timer)
    timer_p.terminate()
    timer_p.join()
elif timer_question == "n":
    print(colored("Starting the bot...", "green"))
    sleep(1)
    move_mouse()
else:
    print("You can only answer with ""Y"" (yes) or ""N"" (no), please try again.")
