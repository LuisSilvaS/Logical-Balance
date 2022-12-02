def ImprimaMaxPeso(Group):
    
    if(Group[0]==Group[1]): # comparando bolas do mesmo grupo

          print(f'Peso: {Group[2]}')

    else:

         print(f'Peso: {max(Group[0],Group[1])}')