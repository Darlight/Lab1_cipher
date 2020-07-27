"""
Universidad del Valle de Guatemala
Cifrado de Informacion
Seccion 10
Lic. Luis Alberto Suriano
Grupo 4

main.py
Proposito: Crear una linea dentro del framebuffer con las posibles optimizaciones
"""
#Imnportar pylfsr en pip install
# Manual https://pypi.org/project/pylfsr/ 

# En este programa se puede explicar el método de Linear-feedback shift register (LFSR)
import numpy as np
from pylfsr import LFSR

#La primera forma es utilizar una libreria externa que permite hacer simular este tipo de algoritmo
L = LFSR()
#Esta funcion nos muestra en la terminal un LFSR de 5-bits con una semilla de [1,1,1,1,1] y contiene 
#los bits bit 5, bit 2 y el bit inicial como estado para determinar el output, con el %2 entre la suma de estos
# 3 bits
# Este estado es el "feedback" para generar un numero random
L.info()
L.runFullCycle()

#Tambien se puede modificar el estado y el feedback deseado para cambiar el proceso de determiner el output

state = [0,0,0,1,0] # 5-bits
fstate = [5,4,3,2] # (bit 5 + bit 4 + bit 3 + bit 2 + (bit 0 == 1, ya que xsub0 ^ 2 = 1)) % 2
L2 = LFSR(fpoly=fstate, initstate= state, verbose=True)
#Tenemos un espacio muestal de 5 bits {0,1}^5
L2.info()
#Le damos 10 ciclos de correr el programa y vemos que el resultado del feedback va cambiando en
#la primera columna, moviendo los otros resultados a la derecha
#hasta encontrar un patron
timeseq= L2.runKCycle(10)
print(timeseq)
L2.info()
#L.info()

#L
#import time
#def group_LFSR(seed, taps):
#    import time
 #   sr, xor = seed, 0
  #  while 1:
   #     for t in taps:
    #        xor += int(sr[t-1])
     #       if xor%2 == 0.0:
      #          xor = 0
       #     else:
        #        xor = 1
         #   print(xor)
          #  print('')
           # time.sleep(0.75)
            #sr, xor = str(xor) + sr[:-1], 0
            #print(sr)
            #if sr == seed:
             #   break
#def group2_LFSR(seed, taps):
 #   while True:
  #      nxt = sum([ seed[x] for x in taps]) % 2
   #     yield nxt
    #    seed = ([nxt] + seed)[:max(taps)+1]
#group_LFSR('11001001',(8,7,6,1))

#for x in group2_LFSR([1,0,1,1,1,0,1,0,0],[1,5,6]):
#    time.sleep(0.75)
#    print(x)