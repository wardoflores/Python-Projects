#! python3
import time
'''
Guides you through the process of meditation.
'''

print("\n")
print("Good day to you my friend.")
print("\n")
time.sleep(1)


print("We'll go through the meditative process now, are you ready?")
questionone = input("Type Yes: ")
if questionone == "Yes":
    print("\n")
    print("Great!")
else:
    print("Well I will still go on as needed, knowing that you came.")
    
time.sleep(2)
print("\n")

print("make yourself comfortable in a space without distractions.")      
time.sleep(5)
print("\n")


print("Let's reflect on these concepts:")
print("\n")
time.sleep(2)

def process():
    print("Who are you?")
    print("\n")
    time.sleep(5)


    print("What mindset do you primarily have right now?")
    print("\n")
    time.sleep(5)


    print("Recall your principles.")
    print("\n")
    time.sleep(5)


    print("Reflect on your Spirituality.")
    print("\n")
    time.sleep(5)


    print("What are your Responsibilities?")
    print("\n")
    time.sleep(5)

process()

restart = input("Do you want to be reminded once again? Type Yes to be reminded: ")
if restart == "Yes":
    print("\n")
    restart ==  process()
else:
    print('\n')
    print("Excellent, have a nice day!")
    exit()


