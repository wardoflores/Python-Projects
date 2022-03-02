#! python3
catnames = []

while True:
    print("Enter name of the cat" + str(len(catnames) + 1) + " (Or enter nothing to stop.):")
    name = input()
    if name == '':
        break
    catnames = catnames + [name]
    print("The cat names are:")
    for name in catnames:
        print(' ' + name)