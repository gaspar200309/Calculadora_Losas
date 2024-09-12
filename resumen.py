
#_CÁLCULO Y DIMENSIONADO DE LOSAS UNIDIRECCIONALES
# INTRODUCCION DE DATOS

h= 0.25 #(m)
b= 0.10 #(m)
Asøprincipal= 0.0010 #(m)
rec= 0.025 #(m)
fc= 21 #(MPa)
fy= 420 #(MPa)
Mu= 21.93 #(Kn)
Vu= 26.36 #(Kn)
λ= 1
ø=0.9 # factor resistente a esfuerzo de flexion

#BÚSQUEDA 1. DETERMINACIÓN DE LA ALTURA UTIL
d=h-rec-(Asøprincipal/2)
print('d=',d)

#BÚSQUEDA 2. TRANSFORMACION DEL MOMENTO UTLIMO
Mu=(Mu/1000)
print('Mu=',Mu)


#*BÚSQUEDA 3. CUANTÍA O PORCENTAJE DE ACERO REQUERIDO (ρ)
ρ=(0.85*fc/fy)*(1-(1-2*Mu/(ø*0.85*fc*b*d**2))**0.5)
print('ρ=',ρ)

#VERIFICACIÓN. VIGA RECTANGULAR O VIGA T
a=ρ*fy*d/(0.85*fc)
print('a=',a)

# VALORES β1 PARA LA DISTRIBUCIÓN DE ESFUERZO
if fc<28:
    β1 = 0.85 
elif fc<55:
    β1 = 0.65
else:   
    β1 = 0.85-(0.05*(fc-28)/7)
print('β1=',β1)   

#BÚSQUEDA 3.2. DISTANCIA AL EJE NEUTRO
c=a/β1
print('c=',c)

#BÚSQUEDA 3.3 Et A TRAVÉS DE LA RELACIÓN DE TRIÁNGULOS
єt=d-c*0.003/(c)
print('єt=', єt)

#BÚSQUEDA 3.4 AREA REQUERIDO DE ACERO
As=ρ*(b*100)*(d*100) #esta expresion esta en cm
print('As=',As)

#BÚSQUEDA 3.5 REFUERZO MÍNIMO A FLEXIÓN EN LOSAS NO PREESFORZADAS
ρmin_a= (0.0018*420/fy)*0.045
ρmin_b= 0.0014*0.045
ρmin= max(ρmin_a,ρmin_b)
print('ρmin=',ρmin)

#NÚMERO DE BARRAS
Nb= ρmin/1.13
print('Nb=', Nb)

#BÚSQUEDA 3.6. REFUERZO CORRUGADO DE RETRACCIÓN Y TEMPERATURA
ρmintemp_a= (0.0018*420/fy)*1*d
ρmintemp_b= 1.4*1*d
ρmintemp= max(ρmintemp_a,ρmintemp_b)
print('ρmintemp=',ρmintemp)

#BÚSQUEDA 3.7 DETERMINANDO EL MOMENTO NOMINAL 
øMn= ø*ρmin*fy*(d-(a/2))*(1000/1) #conversión a Kn.m
print('øMn=',øMn)

#Verificación
if øMn>Mu:
    print('CUMPLE')
else:
    print('NO CUMPLE')
 
#VERIFICACIÓN AL CORTANTE
if 1/2*(ø)*(0.17)*(λ)*(fc**0.5)*(100)*b*d>Vu:
   print('cortante no requiere estribos') 
else:
    print('cortante requiere estribos')

#Cuantia minima, real y max
#Ro minima, real y max
#Algo más de nosotros
