import psutil
import time
import colorama

# POGGERS BAR
def progress_bar(progresso, total, color=colorama.Fore.YELLOW):
    porcentagem = 100 * (progresso/float(total))
    barra = '█' * int(porcentagem) + '-' *(100 - int(porcentagem))
    print(color + f"\r|{barra}| {porcentagem:.2f}%", end="\r")
    if progresso > total-2:
        total = 100.00
        print(colorama.Fore.GREEN + f"\r|{barra}| {porcentagem:.2f}%", end="\r")


global array_pids
array_pids = []
global array_cpu
array_cpu = []


for proc in psutil.process_iter(['pid']):
    array_pids.append(proc.pid)

# print(array_pids)
# print(len(array_pids))

print('Iniciando Leitura!')
nucleos = psutil.cpu_count()
print(nucleos)
# progress_bar(0, len(array_pids))
for i, proc in enumerate(psutil.process_iter(['memory_percent','status', 'name', 'pid'])):
    c = float(proc.cpu_percent(interval=1)/nucleos)
    array_cpu.append(c)
    print(proc,c)
    # progress_bar(i+1, len(array_pids))

# print(array_cpu)
# print(len(array_cpu))
print(colorama.Fore.RESET)
print(f"\r")
print(len(array_pids))
print(array_cpu)

time.sleep(100)