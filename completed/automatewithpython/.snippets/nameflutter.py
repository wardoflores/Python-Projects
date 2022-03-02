#! python3
name = str(input("what is your name: "))

def process(name):
    print("Oh hey there,")
    for i in name:
        print("* * * " + i + " * * *")

process(name)