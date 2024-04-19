#
# Alumno: Lisandro Rios
# Email: rios.lisandro369@gmail.com
#
################################################################
#ENUNCIADO
#
# Se realizó una encuesta a 1000 personas sobre sus preferencias de viajes y se
# obtuvieron los siguientes datos:
# a)
#  400 viajan en avión y los datos se han recolectado en una tupla:
#  (57,35,11,3,41,23,6,22,10,5,7,67,9,4,58,42)

#  100 alquilan autos y los datos se han recolectado en una diccionario:
#  [7,9,4,10,2,8,41,11,3,5]

#  700 prefieren alojamiento de distintos tipos y los datos se han recolectado en un diccionario:
#  {"Hotel": 42, "Hostel": 9, "Motel": 67, "Apart-Hotel":58, "Apartment":4, "Boutique Hotel": 135,
#  "Resort": 119, "Bed and Breakfast": 68, "Guest House": 8, "Lodge":75, "Casa Rural":26, "Inn": 59,
#  "Pop-up Hotel": 7, "Business Hotel":23}
# b)
# Por otra parte se sabe que:
#  210 eligen alojamiento y avión.
#  28 eligen alojamiento y alquilan auto.
#  90 de los que alquilan autos también eligen avión.
#  20 de la población total eligen avión, alquilan auto y eligen alojamiento.
# c) Resolver y responder:
#  1. Cuántos entrevistados eligen alojamiento, avión y alquilan autos?
#  2. Cuántos entrevistados sólo eligen alojamiento y avión?
#  3. Cuántos entrevistados sólo eligen avión y alquilar autos?
#  4. Cuántos entrevistados sólo eligen alojamiento y alquilar autos?
#  5. Cuántos entrevistados sólo eligen alojamiento?
#  6. Cuántos entrevistados sólo eligen avión?
#  7. Cuántos entrevistados sólo eligen alquilar autos?
#  8. Cuántos entrevistados eligen 2 de las 3 propuestas?
#  9. Cuántos entrevistados no eligen alojamiento, ni avión, ni alquilar autos?
# d) Graficar con matplotlib_venn
# Nota: El ejercicio debe resolverse con variables, estructuras, operaciones de conjuntos, funciones propias y del lenguaje, etc. No
# se admiten valores literales, salvo en el caso de la asignación del valor universal y en las inicializaciones de variables. Una vez
# resuelto el ejercicio, sube la solución a la carpeta del campus con nombre y apellido como nombre de archivo.


########################################################################
#RESOLUCION
########################################################################

from matplotlib import pyplot as plt
from matplotlib_venn import *
from matplotlib.patches import Circle

universal = 1000

avion = (57,35,11,3,41,23,6,22,10,5,7,67,9,4,58,42)

autos = [7,9,4,10,2,8,41,11,3,5]

alogamiento = {"Hotel": 42, "Hostel": 9, "Motel": 67, "Apart-Hotel":58, "Apartment":4, "Boutique Hotel": 135,
 "Resort": 119, "Bed and Breakfast": 68, "Guest House": 8, "Lodge":75, "Casa Rural":26, "Inn": 59,
 "Pop-up Hotel": 7, "Business Hotel":23}

#----------------------------------------------------------------
# Funciones
def suma_diccionario(diccionario):
    suma = 0
    for elemento in diccionario.values():
        suma = suma + elemento
    return suma

def suma(estructuras):
    suma = 0
    for elem in estructuras:
        suma = suma + elem
    return suma

def set_dic(diccionario):
    aloga = set()
    for elemento in diccionario.values():
        aloga.add(elemento)
    return aloga

aloga = suma_diccionario(alogamiento)
avi = suma(avion)
aut = suma(autos)
set_aloja = set_dic(alogamiento)
set_avion = set(avion)
set_autos = set(autos)

print('alogamiento:',aloga)
print('avion: ',avi)
print('autos: ',aut) 
print(set_aloja)
print(set_avion)
print(set_autos)

#----------------------------------------------------------------
# Resuelvo
#  1. Cuántos entrevistados eligen alojamiento, avión y alquilan autos?
ven_todos = set_aloja & set_avion & set_autos
print(ven_todos, sum(ven_todos))  

# 2. Cuántos entrevistados sólo eligen alojamiento y avión?
ven_alojaYAvion = set_aloja & set_avion - (ven_todos)
print(ven_alojaYAvion, sum(ven_alojaYAvion)) 

# 3. Cuántos entrevistados sólo eligen avión y alquilar autos?
ven_avionYAutos = set_avion & set_autos - (ven_todos)
print(ven_avionYAutos, sum(ven_avionYAutos))

# 4. Cuántos entrevistados sólo eligen alojamiento y alquilar autos?
ven_alogyAutos = set_aloja & set_autos - (ven_todos)
print(ven_alogyAutos, sum(ven_alogyAutos))

# 5. Cuántos entrevistados sólo eligen alojamiento?
solo_alojamiento = set_aloja - (ven_todos | ven_alojaYAvion | ven_alogyAutos)
print(solo_alojamiento, sum(solo_alojamiento)) 

# 6. Cuántos entrevistados sólo eligen avión?
solo_avion = set_avion - (ven_todos | ven_alojaYAvion | ven_avionYAutos)
print(solo_avion, sum(solo_avion)) 

# 7. Cuántos entrevistados sólo eligen alquilar autos? 
solo_autos = set_autos - (ven_todos | ven_alogyAutos | ven_avionYAutos)
print(solo_autos, sum(solo_autos)) 

# 8. Cuántos entrevistados eligen 2 de las 3 propuestas?
entrevist2De3 = ven_alogyAutos | ven_avionYAutos | ven_alojaYAvion
print(entrevist2De3, sum(entrevist2De3)) 

# 9. Cuántos entrevistados no eligen alojamiento, ni avión, ni alquilar autos?
afuera = universal - (sum(ven_todos) + sum(ven_alojaYAvion) + sum(ven_avionYAutos) + sum(ven_alogyAutos) + sum(solo_alojamiento) + sum(solo_autos) + sum(solo_avion))
print(afuera)

#----------------------------------------------------------------
# Grafico con matplotlib_venn

plt.figure(figsize=(7,7))
plt.rcParams['text.color'] = 'k'

diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(f"Alogamientos={aloga}", f"Avión={avi}", f"Auto={aut}"))

for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(7)

diagram.get_label_by_id('100').set_text(sum(solo_alojamiento)) 
diagram.get_label_by_id('010').set_text(sum(solo_avion)) 
diagram.get_label_by_id('001').set_text(sum(solo_autos)) 
diagram.get_label_by_id('110').set_text(sum(ven_alojaYAvion)) 
diagram.get_label_by_id('011').set_text(sum(ven_avionYAutos)) 
diagram.get_label_by_id('101').set_text(sum(ven_alogyAutos))  
diagram.get_label_by_id('111').set_text(suma(ven_todos)) 

c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

plt.text(-0.15, 0.57,      
         f"Entrevistados = {universal}",
         size=14)

plt.text(0.40, -0.5,      
         f"Afuera = {afuera}",
         size=10)

plt.text(-1.10, -0.20,
         s=f"eligen alojamiento = {suma(solo_alojamiento)}",
         size=10,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,
         s=f"eligen avión = {suma(solo_avion)}",
         size=10,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,
         s=f"eligen alquilar autos = {suma(solo_autos)}",
         size=10,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s=f"eligen alojamiento y avión = {suma(ven_alogyAutos)}",
         size=10,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s=f"Ven 2 de las 3 categorías = {suma(ven_alogyAutos) + suma(ven_avionYAutos) + suma(ven_alojaYAvion)}",
         size=10,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.70,
         s=f"Ven las 3 categorías = {sum(ven_todos)}",
         size=10,
         ha="left",  
         va="bottom",  
         bbox=dict(boxstyle="square",  
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.show()




