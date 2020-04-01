import random
#Simulaciondepoisson
#se generara una variable aleatoria binomial usando los siguientes datos. 
#Numero de intentos: 20 intentos.
#probabilidad de exito: 30% 
#se desea calcular la probabilidad:  de 5 exitos en los 20 intentos
#variables: 
#n numero de intentos. 
#ne numero de exitos.
#i es un contador.
#p probabilidad de exito. 
#q probabilidad de fracaso.
#s de suma
#probabilidad que sea mayor a 5
s = 0
j = 0
n = 20
p = 0.30
q = 1.0 - p

while(j<1000000):
    i = 0
    ne = 0
    while(i<20):
        r = random.random()
        if(r<p):
            ne = ne + 1
        i = i + 1
    if (ne==5):
        s = s + 1
    j = j + 1
print ("P[NE=5]=" +str(float(s)/1000000))
