# Converting a number to a list of integers.

# Source: https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers/

def numtointlist1(num):
    # using list comprehension
    
    # printing number 
    print ("The original number is " + str(num))

    # using list comprehension
    # to convert number to list of integers
    res = [int(x) for x in str(num)]
    
    # printing result 
    print ("The list from number is " + str(res))


def numtointlist2(num):

    # conversion of number to list of integers
    # using map()
    
    # printing number 
    print ("The original number is " + str(num))

    # using map()
    # to convert number to list of integers
    res = list(map(int, str(num)))
    
    # printing result 
    print ("The list from number is " + str(res))

def main():
    num = int(input("Input the number to be converted: "))
    choice = input("Choose between [1, 2] to execute different kinds of conversions: ")
    if choice == '1':
        return numtointlist1(num)
    elif choice == '2':
        return numtointlist2(num)
    else:
        return exit()



if __name__ == '__main__' :
    main()