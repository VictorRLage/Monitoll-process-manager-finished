import psutil
import time
import colorama

# POGGERS BAR
def progress_bar(progresso, total, color=colorama.Fore.YELLOW):
    porcentagem = 100 * (progresso/float(total))
    barra = '█' * int(porcentagem) + '-' *(100 - int(porcentagem))
    print(color + f"\r|{barra}| {porcentagem:.2f}%", end="\r")
    if progresso == total:
        print(colorama.Fore.GREEN + f"\r|{barra}| {porcentagem:.2f}%", end="\r")







global array_pids
array_pids = []
global array_cpu
array_cpu = []


for proc in psutil.process_iter(['name', 'pid']):
    array_pids.append(proc.pid)

# print(array_pids)
# print(len(array_pids))

progress_bar(0, len(array_pids))
for i, proc in enumerate(psutil.process_iter(['memory_percent','status', 'cpu_percent', 'name', 'pid'])):
    c = proc.cpu_percent(interval=1)
    array_cpu.append(c)
    progress_bar(i+1, len(array_pids))

# print(array_cpu)
# print(len(array_cpu))
print(colorama.Fore.RESET)
print(f"\r")
print(len(array_pids))

time.sleep(100)