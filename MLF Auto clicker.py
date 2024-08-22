import pyautogui as ai
from os import system
import time
system(" cls ")
print("Loading...")
time.sleep(5)
system(" cls ")
print("Your mouse crouser postion is:",ai.position())
print("")
sleep = float(input("What time you want to sleep? "))
amount = int(input("How many clicks did you want? "))
time.sleep(1)
system(" cls ")
print("attack is going to start \U0001F600")
time.sleep(2)
i = 1
while i < amount+1:
  ai.click(ai.position())
  time.sleep(sleep)
  i += 1
