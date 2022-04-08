# Fizzbuzz sentence in Python

# Source: https://blog.finxter.com/python-one-line-fizzbuzz/

# or from finxter

# 1

print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1,101)))

# 2

for i in range(1, 101): print('FizzBuzz'[i*i%3*4:8--i**4%5] or i)

# 3

print(list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i), range(1,101))))

# Source: https://www.w3resource.com/python-exercises/python-conditional-exercise-10.php

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



