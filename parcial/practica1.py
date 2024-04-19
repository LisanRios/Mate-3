# De 1000 televidentes encuestados se obtiene la siguiente información:
# 
# a)
#     391 ven programas deportivos y los datos se han recolectado en un diccionario: 
#         {"Voleybol": 10, "Hockey": 87,  "Equitacion":23, "Ciclismo":81, "Esqui":11, "Futbol": 45, "Tenis": 37,
#         "Rugby": 9, "Basquetbol": 7, "Boxeo": 6, "Natacion":75}
#     
#     230 ven programas cómicos y los datos se han recolectado en una tupla:
#         (41,29,58,4,45,37,9,7)
#     
#     545 ven programas sobre mundo animal y los datos se han recolectado en una lista:
#         [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]
# 
# b) 
# Por otra parte, se sabe que:
#     98 ven programas cómicos y deportivos
#     152 ven programas cómicos y de mundo animal
#     88 ven programas deportivos y de mundo animal
#     90 no ven ninguno de esos programas
# 
# c)
# Resolver y responder:
#     1. Cuántos entrevistados ven los 3 tipos de programas?
#     2. Cuántos entrevistados sólo lo ven deportivos y cómicos?
#     3. Cuántos entrevistados ven sólo cómicos y mundo animal?
#     4. Cuántos entrevistados ven sólo deportivos y mundo animal?
#     5. Cuántos entrevistados ven sólo deportes?
#     6. Cuántos entrevistados ven sólo cómicos?
#     7. Cuántos entrevistados ven sólo mundo animal? 
#     8. Cuántos entrevistados ven 2 de las 3 categorías?
# 
# d) Graficar con matplotlib_venn
# 
# Nota: 
# 
# El ejercicio debe resolverse con variables, estructuras, operaciones de conjuntos, funciones propias y del lenguaje, etc. No se admiten valores literales, salvo en el caso de la asignación del valor universal y en las inicializaciones de variables.
from matplotlib import pyplot as plt
from matplotlib_venn import *
from matplotlib.patches import Circle

universal = 1000
# ninguno = 90
# resto = universal - ninguno

# 391 (diccionario)
deportivo = {"Voleybol": 10, "Hockey": 87, "Equitacion":23, "Ciclismo":81, "Esqui":11,
             "Futbol": 45, "Tenis": 37, "Rugby": 9, "Basquetbol": 7, "Boxeo": 6,
             "Natacion":75} 

# 230 (tupla)
comico = (41,29,58,4,45,37,9,7)

# 545 (lista)
mundo_animal = [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]

#----------------------------------------------------------------
# # Funciones
# defino función que suma los elementos de las estructuras
def suma_dic(diccio):
    suma = 0
    for elemento in diccio.values():
        suma = suma + elemento
    return suma
dep = suma_dic(deportivo)
print('deportivo:',dep)

def suma(estructuras):
    suma = 0
    for elem in estructuras:
        suma = suma + elem
    return suma

com = suma(comico)
print('comico: ',com)
ani = suma(mundo_animal)
print('mundo_animal: ',ani) 

# convierto en set el dicc, la lista y la tupla
def set_dic(diccio):
    dep = set()
    for elemento in diccio.values():
        dep.add(elemento)
    return dep

set_d = set_dic(deportivo)
print(set_d)

set_c = set(comico)
print(set_c)

set_a = set(mundo_animal)
print(set_a)

#----------------------------------------------------------------
# # Resuelvo
# 1. Cuántos entrevistados ven los 3 tipos de programas?
ven_dca = set_d & set_c & set_a
print(ven_dca, sum(ven_dca))  # 82

# 2. Cuántos entrevistados sólo lo ven deportivos y cómicos?
ven_dc = set_d & set_c - (ven_dca)
print(ven_dc, sum(ven_dc))  # 16 ven sólo deportivos y cómicos

# 3. Cuántos entrevistados ven sólo cómicos y mundo animal?
ven_ca = set_c & set_a - (ven_dca)
print(ven_ca, sum(ven_ca)) # # 170 ven cómicos y mundo animal

# 4. Cuántos ven sólo deportivos y mundo animal
ven_da = set_d & set_a - (ven_dca)
print(ven_da, sum(ven_da)) # 6

# 5. Cuántos ven sólo deportes?
solo_d = set_d - (ven_dca | ven_dc | ven_da)
print(solo_d, sum(solo_d)) # 287

# 6. Cuántos ven sólo cómicos?
solo_c = set_c - (ven_dca | ven_dc | ven_ca)
print(solo_c, sum(solo_c)) # 62

# 7. cuántos ven sólo mundo animal? 
solo_a = set_a - (ven_dca | ven_da | ven_ca)
print(solo_a, sum(solo_a)) # 387

# 8. cuántos ven 2 de las 3 categorías?
opina_2_de_3 = ven_da | ven_ca | ven_dc
print(opina_2_de_3, sum(opina_2_de_3)) # 92

# quiere no ven ninguno?
ninguno = universal - (sum(ven_dca) + sum(ven_dc) + sum(ven_ca) + sum(ven_da) + sum(solo_d) + sum(solo_a) + sum(solo_c))
print(ninguno)

#----------------------------------------------------------------
# # Gráficos Pero con conjuntos.

# preparamos la ventana del gráfico
plt.figure(figsize=(9,15))
plt.rcParams['text.color'] = 'k'

# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(f"Deportivos={dep}", f"Cómicos={com}", f"Mundo Animal={ani}"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(8)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(solo_d) #287
diagram.get_label_by_id('010').set_text(solo_c) #62
diagram.get_label_by_id('001').set_text(solo_a) #387
diagram.get_label_by_id('110').set_text(ven_dc) #16
diagram.get_label_by_id('011').set_text(ven_ca) #70
diagram.get_label_by_id('101').set_text(ven_da)  #6
diagram.get_label_by_id('111').set_text(ven_dca) #82

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.15, 0.57,      # Texto y cantidad universal
         f"Universal = {universal}",
         size=12)

plt.text(0.40, -0.5,      # Texto fuera del conjunto
         f"Fuera\nde los\nconjuntos = {ninguno}",
         size=10)

# Respondemos las preguntas
plt.text(-1.10, -0.20,
         s="Respuestas solicitadas: ",
         size=10,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,
         s=f"Ven sólo deportes = {suma(solo_d)}",
         size=10,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,
         s=f"Ven sólo cómicos = {suma(solo_c)}",
         size=10,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s=f"Ven sólo mundo animal = {suma(solo_a)}",
         size=10,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s=f"Ven sólo deportes y mundo animal = {suma(ven_da)}",
         size=10,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.70,
         s=f"Ven 2 de las 3 categorías = {suma(ven_da) + suma(ven_ca) + suma(ven_dc)}",
         size=10,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.80,
         s=f"Ven las 3 categorías = {sum(ven_dca)}",
         size=10,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.axis('on')  # Recuadro
plt.title("Encuesta a televidentes")
plt.show()


#----------------------------------------------------------------
# Gráfico con los resultados.

# preparamos la ventana del gráfico
plt.figure(figsize=(9,7))
plt.rcParams['text.color'] = 'k'

# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(f"Deportivos={dep}", f"Cómicos={com}", f"Mundo Animal={ani}"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(sum(solo_d)) #287
diagram.get_label_by_id('010').set_text(sum(solo_c)) #62
diagram.get_label_by_id('001').set_text(sum(solo_a)) #387
diagram.get_label_by_id('110').set_text(sum(ven_dc)) #16
diagram.get_label_by_id('011').set_text(sum(ven_ca)) #70
diagram.get_label_by_id('101').set_text(sum(ven_da))  #6
diagram.get_label_by_id('111').set_text(suma(ven_dca)) #82

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.15, 0.57,      # Texto y cantidad universal
         f"Universal = {universal}",
         size=14)

plt.text(0.40, -0.5,      # Texto fuera del conjunto
         f"Fuera\nde los\nconjuntos = {ninguno}",
         size=12)

# Respondemos las preguntas
plt.text(-1.10, -0.20,
         s="Respuestas solicitadas: ",
         size=12,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,
         s=f"Ven sólo deportes = {suma(solo_d)}",
         size=12,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,
         s=f"Ven sólo cómicos = {suma(solo_c)}",
         size=12,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s=f"Ven sólo mundo animal = {suma(solo_a)}",
         size=12,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s=f"Ven sólo deportes y mundo animal = {suma(ven_da)}",
         size=12,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.70,
         s=f"Ven 2 de las 3 categorías = {suma(ven_da) + suma(ven_ca) + suma(ven_dc)}",
         size=12,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.80,
         s=f"Ven las 3 categorías = {sum(ven_dca)}",
         size=12,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.axis('on')  # Recuadro
plt.title("Encuesta a televidentes")
plt.show()




