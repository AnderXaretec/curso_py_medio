from re import I
import random
from tracemalloc import stop
from unittest import result
import time
import os


def read():
    # words = []
    with open("./archivos/DATA.txt", "r", encoding="utf-8") as f:
        
        
        # for word in f:
        #     words.append(word)
        # i="Word"

        # words = {"Word": word for word in f}#dict comprenhensions - pendiente continuar
    
        words = [word for word in f]#list compr.- crea lista con todas las palabras
        # randnum = random.randint(1, len(words))#elige un num al azar entre 1 y la cantidad de palabras que haya
        selword = words[int(random.randint(1, len(words)))]#selecciona la palabra en la posicion del num aleatorio elegido antes
        # return selword

#funcion principal del juego
    charlist = ["_" for z in range(1, len(selword))]#crea lista llena de tantos _ como caract tiene la palabra elegida    
    acepts = 1
    for z in range(1, 11):
        print("Te quedan ", 11 - z, " vidas")
        selchar = input("Inserta una letra: ")
        
#metodo1 - listas y for con slices:
        i = 1
        for char in selword[::i]:
            if selchar == char:
                # print(char)
                charlist[i - 1] = char
                acepts += 1
            i += 1
        if acepts == len(selword):
            print("Has ganado!! la palabra es: ", selword)
            exit()
                # print("_")        
        # time.sleep(3)
        os.system("cls")
        print(charlist)
    print("Fallaste. La palabra es: ", selword)
    exit()

#metodo2(list compr):



def game():
    pass



#select a word
def select():
     pass

#clean items without \n
def cleaner():
    pass


#Menu principal:
# print("""Bienvenido al juego del ahorcado.
# Acierta la palabra:""")
# input(print("Ingresa una letra: "))




def run():

    read()
    # game()




if __name__ == "__main__":
    run()