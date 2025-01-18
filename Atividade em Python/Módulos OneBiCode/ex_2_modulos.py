import os
from time import sleep

def desligar():
    while True: 
        min = input('Em quento tempo deseja desligar o computador(em minutos): ')
        try:
            min = float(min)
            break
        except:
            print('Erro! Tempo invalido.')
    segundos = min * 60
    print(f'O computador será desligado em {min} minutos')
    sleep(segundos)
    os.system('shutdown /s /t 1')

def cancelarDesligamento():
    os.system('shutdown /a')
    print('Desligamento cancelado')

desligar()
cancelarDesligamento()