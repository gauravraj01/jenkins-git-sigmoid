import psutil
import sched
import time

print("Hello World")
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    cpu = psutil.cpu_percent(1)
    mem = psutil.virtual_memory()
    print(f'CPU :{cpu}')
    print(f'Memory :{mem}')
    s.enter(2, 1, do_something, (sc,))
s.enter(2, 1, do_something, (s,))
s.run()
