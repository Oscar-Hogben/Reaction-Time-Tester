from TimeV2 import time2
import random, threading, subprocess

words = ["dinosaur", "banana", "chicken", "dynamics", "yoyo", "lizard", "parrot", "helicopter"]

print("Welcome to the reaction speed tester!")
time2.wait(3)
print("Press enter as soon as you see the word 'dinosaur' on your screen!")
time2.wait(4)
print("Press enter to start!")
input()
print()
print()

finish = False
loose = False

word = ""

def inputTester():
  input()
  if not finish:
    global loose
    loose=True

# t = threading.Thread(target=inputTester)
# t.start()
# subprocess.call(['inputTester.py'])

while word != "dinosaur":
  timeToWait = random.randint(9, 15) / 10
  time2.wait(timeToWait)
  if loose:
    exit("You loose! You pressed enter too early!")
  word = random.choice(words)
  print(word)

finish = True

time2.stopwatch_start()
input()
timeTaken = time2.stopwatch_stop()

file = open("WorldRecord", "r")
worldRecord = file.read()
file.close()

if float(worldRecord) > float(timeTaken):
  print(f"Congratulations! You beat a world record with: {timeTaken} seconds!")
  file = open("WorldRecord", "w")
  file.write(str(timeTaken))
  file.close()
else:
  print(f"You got {timeTaken}. Well done!")