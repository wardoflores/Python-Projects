# https://stackoverflow.com/questions/2846653/how-can-i-use-threading-in-python

import time
from threading import Thread

def just_func():
    pass

def threaded_func():
    pass

Thread(target=threaded_func)

start = time.time()
threaded_func()
end = time.time()
print(end - start)

start = time.time()
just_func()
end = time.time()
print(end - start)