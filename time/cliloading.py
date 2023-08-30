# https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running

import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.daemon=True
t.start()

#long process here
time.sleep(10)
done = True
