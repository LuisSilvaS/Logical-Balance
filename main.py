#imports
from max_peso import peso 
import random 


pesos_list = [1.0, 1.0, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0]
random.shuffle(pesos_list) # Embaralhando as posição da lista de pesos.


Group_1 = [pesos_list[0],pesos_list[1],pesos_list[2]]
Group_2 = [pesos_list[3],pesos_list[4],pesos_list[5]]
Group_3 = [pesos_list[6],pesos_list[7],pesos_list[8]]


peso(Group_1,Group_2,Group_3)
