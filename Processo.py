import psutil
import time
global array_pids

array_pids = []

for proc in psutil.process_iter(['name', 'pid']):
    array_pids.append(proc.pid)

print(array_pids)
print(len(array_pids))


for proc in psutil.process_iter(['memory_percent','status', 'cpu_percent', 'name', 'pid']):
    c = proc.cpu_percent(interval=2)
    print(proc.info,c)

time.sleep(100)