import math
import time
import colorama


def progress_bar(progresso, total, color=colorama.Fore.YELLOW):
    porcentagem = 100 * (progresso/float(total))
    barra = 'x' * int(porcentagem) + '-' *(100 - int(porcentagem))
    print(color + f"\r|{barra}| {porcentagem:.2f}%", end="\r")
    if progresso == total:
        print(colorama.Fore.GREEN + f"\r|{barra}| {porcentagem:.2f}%", end="\r")


numbers = [x * 5 for x in range(2000, 3000)]
results = []

print("Sistema de verificação")
v = input("Quem deseja verificar? ")
progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i+1, len(numbers))

print(colorama.Fore.RESET)
print('\r')
print('Confirmado!')
print()
time.sleep(5)
print("O "+v+" é gay")
time.sleep(100)
