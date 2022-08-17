# Cada apostador deve escolher no mínimo seis números entre os 60 disponíveis na cartela

from random import randint
from time import sleep
lista=[]
jogos=[]  #cada vez que for sorteado, é adicionado a respectiva lista
cont=0 #contador
print('#'*100)
print(f'{"Simulador MEGA SENA":^75}')
print('#'*100)

jogadas=int(input("Usuário, quantas sorteios você deseja ? "))

tot=1
# Total de jogos que serão sorteados

while tot<=jogadas:
    cont=0
    while True:
        numero= randint(1,61)
        if numero not in lista:
            lista.append(numero)
            cont+=1
            if cont>=6:
                break
    lista.sort()
    jogos.append(lista[:])  #criado uma copia da lista, toda vez que é sorteada uma lista, para que se gere
    lista.clear()           #uma nova, chamada jogos e assim a anterior é apagada
    tot+=1
sleep(0.75)
print("\033[1mAGUARDE ENQUANTO O COMPUTADOR PROCESSA OS DADOS\033[m")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")
sleep(0.5)
print(".",end="")

for i,l in enumerate(jogos):
    print(f"\n\033[1;31mJogo {i+1}: {l}\033[m")
print("\033[1;36m#"*10,'\033[4;36mBOM JOGO E BOA SORTE\033[m',"\033[1;36m#\033[m"*13)


