# Fizzbuzz sentence in Python


# or from finxter

# 1

print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1,101)))

# 2

for i in range(1, 101): print('FizzBuzz'[i*i%3*4:8--i**4%5] or i)

# 3

print(list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i), range(1,101))))

#



