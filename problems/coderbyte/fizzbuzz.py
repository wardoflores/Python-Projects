# Fizzbuzz sentence in Python

# Source: https://blog.finxter.com/python-one-line-fizzbuzz/
# Source: https://www.w3resource.com/python-exercises/python-conditional-exercise-10.php

def fizz1():

    print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1,101)))

def fizz2():

    for i in range(1, 101): print('FizzBuzz'[i*i%3*4:8--i**4%5] or i)

def fizz3():

    print(list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i), range(1,101))))

def fizz4():

    for fizzbuzz in range(51):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)

def main():
    choice = input("Choose which fizzbuzz code to run (choose between 1, 2, 3, 4): ")
    if choice == '1':
        return fizz1()
    elif choice == '2':
        return fizz2()
    elif choice == '3':
        return fizz3()
    elif choice == '4':
        return fizz4()
    else:
        return exit()

if __name__ == '__main__' :
    main()
