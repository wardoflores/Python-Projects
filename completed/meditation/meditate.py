#! python3
import time
'''
Guides you through the process of meditation.
'''

print("Good day to you my friend.")
time.sleep(1)


print("We'll go through the meditative process now, are you ready?")
questionone = input("Type Yes: ")
if questionone == "Yes":
    print("Great!")
else:
    print("Well I will still go on as needed, knowing that you came.")
    
time.sleep(2)

print("make yourself comfortable in a space without distractions.")      
time.sleep(5)


print("Let's reflect on these concepts.")
time.sleep(2)

def process():
    print("Who are you?")
    time.sleep(5)


    print("What mindset do you primarily have right now?")
    time.sleep(5)


    print("Recall your principles.")
    time.sleep(5)


    print("Reflect on your Spirituality.")
    time.sleep(5)


    print("What are your Responsibilities?")
    time.sleep(5)
process()

restart = input("Do you want to be reminded again? Type Yes to be reminded: ")
if restart == "Yes":
    restart ==  process()
else:
    print("Excellent, have a nice day!")
    exit()

