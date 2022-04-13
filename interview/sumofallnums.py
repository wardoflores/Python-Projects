# Outputs the sum of the range of all numbers from 1 to n.

# Source: https://pynative.com/python-program-to-calculate-sum-and-average-of-numbers/

def main():
    print("\n")
    input_string = input('Enter numbers separated by space ')
    print("\n")
    # Take input numbers into list
    numbers = input_string.split()

    # convert each item to int type
    for i in range(len(numbers)):
        # convert each item to int type
        numbers[i] = int(numbers[i])

    # Calculating the sum and average
    print("Sum = ", sum(numbers))
    print("Average = ", sum(numbers) / len(numbers))   

if __name__ == '__main__' :
    main()