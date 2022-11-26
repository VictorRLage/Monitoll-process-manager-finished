import math
import time
import colorama


def progress_bar(progresso, total, color=colorama.Fore.YELLOW):
    porcentagem = 100 * (progresso/float(total))
    barra = '█' * int(porcentagem) + '-' *(100 - int(porcentagem))
    print(color + f"\r|{barra}| {porcentagem:.2f}%", end="\r")
    if progresso == total:
        print(colorama.Fore.GREEN + f"\r|{barra}| {porcentagem:.2f}%", end="\r")


numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i+1, len(numbers))

print('\r')
print('aaa')
print('aaa')
time.sleep(100)
