import psutil
import time
import colorama

# POGGERS BAR


def progress_bar(progresso, total, color=colorama.Fore.YELLOW):
    porcentagem = 100 * (progresso/float(total))
    barra = '█' * int(porcentagem) + '-' * (100 - int(porcentagem))
    print(color + f"\r|{barra}| {porcentagem:.2f}%", end="\r")
    if progresso == total:
        print(colorama.Fore.GREEN + f"\r|{barra}| {porcentagem:.2f}%", end="\r")


array_dados = []
array_pids = []
for proc in psutil.process_iter(['pid']):
    array_pids.append(proc.pid)


# print(array_pids)
# print(len(array_pids))

print('Iniciando Leitura!')
nucleos = psutil.cpu_count()

# print("NOME | PID | STATUS | USO CPU | USO RAM")
for i, proc in enumerate(psutil.process_iter()):
    n = proc.name()
    p = proc.ppid()
    s = proc.status()
    c = float(proc.cpu_percent(interval=1)/nucleos)
    m = proc.memory_percent()
    array_dados.append(
        '{"name":c, "pid":p, "status":s, "uso_cpu":c, "uso_ram":m}')

    # print(f"{n} | {p} | {s} | {c:.2f}% | {m:.2f}%")
    progress_bar(i+1, len(array_pids))
progress_bar(1, 1)

print(colorama.Fore.RESET)
print(f"\r")
print(array_dados)
print(len(array_dados))

time.sleep(100)
