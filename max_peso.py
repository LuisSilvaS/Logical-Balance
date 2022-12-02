# imports
from ImprimaPeso import ImprimaMaxPeso

def peso(Group_1,Group_2,Group_3):
  
    if(Group_1 == Group_2): # comparando os pesos de dois grupos. 

        print(f'A bola com maior massa está no grupo 3. {Group_3}') # caso os pesos sejam iguais

        # Buscando a posição da bola com maior massa  

        ImprimaMaxPeso(Group_3) # função que imprimi a bola de maior massa

    if(Group_1 < Group_2): 

        print(f'A bola com maior massa está no grupo 2. {Group_2}') 

        ImprimaMaxPeso(Group_2)  

    if(Group_1 > Group_2):

        print(f'A bola com maior massa está no grupo 1. {Group_1}') 

        ImprimaMaxPeso(Group_1)


