#imports
from max_peso import peso 
import random 


pesos_list = [1.0, 1.0, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0]
random.shuffle(pesos_list) # Embaralhando as posição da lista de pesos.


Group_1 = [pesos_list[0],pesos_list[1],pesos_list[2]]
Group_2 = [pesos_list[3],pesos_list[4],pesos_list[5]]
Group_3 = [pesos_list[6],pesos_list[7],pesos_list[8]]


peso(Group_1,Group_2,Group_3)

print('Lógica')
print('1) Divida as bolas em 3 grupos;')
print('2) Escolha dois grupos para pesar e reserve o grupo extra;')
print('3) Coloque-os cada um em um lado da balança;')
print('4) Se os pesos forem iguais, descarte ambos os grupos;')
print('5) Senão, descarte o grupo mais pesado e o grupo extra;')
print('6) A bola que restou é a mais pesada;')