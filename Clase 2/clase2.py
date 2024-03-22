# 2) 
# from matplotlib_venn import *
# from matplotlib import pyplot as plt
# U=600
# v = venn2(subsets = {'10': 1, '01': 1, '11': 1}, set_labels = ('A', 'B'))
# v.get_patch_by_id('10').set_alpha(0.5)
# v.get_patch_by_id('10').set_color('tomato')
# v.get_patch_by_id('01').set_alpha(0.5)
# v.get_patch_by_id('01').set_color('tomato')
# v.get_patch_by_id('11').set_alpha(0.5)
# v.get_patch_by_id('11').set_color('orange')
# v.get_label_by_id('10').set_text('50')
# v.get_label_by_id('01').set_text('400')
# v.get_label_by_id('11').set_text('50')
# plt.text(-0.70, 0.52,
#  s="Universo = " + str(f'{U}'),
#  size=10,ha="left",va="top",bbox=dict(boxstyle="square", # tipo de cuadro
#  ec=(1.0, 0.7, 0.5),
#  fc=(1.0, 0.9, 0.8),))
# plt.annotate('Estudian Ingles', xy = v.get_label_by_id('10').get_position(), xytext = (-50,-80),
#  size = 'medium', ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5',
#  fc = 'lime', alpha = 0.3), arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = 0.2',
#  color = 'gray'))
# plt.annotate('Estudian Frances', xy = v.get_label_by_id('01').get_position(), xytext = (50,-80),
#  size = 'medium', ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.5',
#  fc = 'lime', alpha = 0.3),arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = -0.2',
#  color = 'gray'))
# plt.annotate('Estudian Frances y Ingles', xy = v.get_label_by_id('11').get_position(),
#  xytext = (0,-70), size = 'medium', ha = 'center', textcoords = 'offset points',
#  bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'lime', alpha = 0.3),
#  arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad = 0',color = 'gray'))
# # Valor de los que quedan afuera
# plt.text(0.28, -0.65,
#  s="Fuera de\nlos conjuntos = " + str('Estudiantes Afuera =100'),
#  size=10)
# # plt.axis('on')
# plt.show()
################################################################
# 
# 1)
# 
# from matplotlib import pyplot as plt
# from matplotlib_venn import *
# from matplotlib.patches import Circle

# # dibujamos los diagramas
# diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
#  "Laptop", "Celular", "Ipod"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))
# # establecemos el tamaño de la fuente
# for subset in ("111", "110", "101", "100", "011", "010", "001"):
#  diagram.get_label_by_id(subset).set_fontsize(16)

# c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)
# # transferimos los resultados de las operaciones
# diagram.get_label_by_id('100').set_text('10')
# diagram.get_label_by_id('100').set_color('green')
# diagram.get_label_by_id('010').set_text('0')
# diagram.get_label_by_id('010').set_color('green')
# diagram.get_label_by_id('001').set_text('19')
# diagram.get_label_by_id('001').set_color('green')
# diagram.get_label_by_id('110').set_text('12')
# diagram.get_label_by_id('110').set_color('blue')
# diagram.get_label_by_id('011').set_text('48')
# diagram.get_label_by_id('011').set_color('blue')
# diagram.get_label_by_id('101').set_text('8')
# diagram.get_label_by_id('101').set_color('blue')
# diagram.get_label_by_id('111').set_text('50')
# diagram.get_label_by_id('111').set_color('red')
# plt.text(0.50, -0.65, s='3',size=14)
# plt.show()

################################################################################
#
# 2. En una encuesta de 80 dueños de casa, se descubrió que:
# • 30 tenían al menos un perro.
# • 42 tenían al menos un gato.
# • 21 tenían al menos una mascota "otra" (pez, tortuga, reptil, hámster, etc.).
# • 20 Tenían perro(s) y gato (s).
# • 10 tenían gato(s) y mascota(s) otra.
# • 8 tenían perro(s) y mascota(s) otra.
# • 5 tenían los tres tipos de mascotas.
# Haz un diagrama de Venn para ilustrar los resultados de la encuesta y responde:
# a. ¿Cuántos tenían perro(s) y gato(s) pero no mascota(s) "otra"? 15
# b. ¿Cuántos solo tenían perro(s)? 2
# c. ¿Cuántos no tenían mascotas? 4
# d. ¿Cuántos dueños de mascota(s) otra también tenían perro(s) o gato(s), pero no ambos? 18
#-Rta
# from matplotlib import pyplot as plt
# from matplotlib_venn import *
# from matplotlib.patches import Circle

# # dibujamos los diagramas
# diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
#  "Perro", "Gato", "Otro"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))
# # establecemos el tamaño de la fuente
# for subset in ("111", "110", "101", "100", "011", "010", "001"):
#  diagram.get_label_by_id(subset).set_fontsize(16)

# c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)
# # transferimos los resultados de las operaciones
# diagram.get_label_by_id('100').set_text('2')
# diagram.get_label_by_id('100').set_color('green')
# diagram.get_label_by_id('010').set_text('12')
# diagram.get_label_by_id('010').set_color('green')
# diagram.get_label_by_id('001').set_text('3')
# diagram.get_label_by_id('001').set_color('green')
# diagram.get_label_by_id('110').set_text('20')
# diagram.get_label_by_id('110').set_color('blue')
# diagram.get_label_by_id('011').set_text('10')
# diagram.get_label_by_id('011').set_color('blue')
# diagram.get_label_by_id('101').set_text('8')
# diagram.get_label_by_id('101').set_color('blue')
# diagram.get_label_by_id('111').set_text('5')
# diagram.get_label_by_id('111').set_color('red')
# plt.text(0.50, -0.65, s='4 sin mascotas',size=14)
# plt.show()

################################################################
# 3. En una encuesta realizada en la ciudad de Buenos Aires, acerca de los medios de transporte más utilizados
# entre colectivos, subte o moto, se obtuvieron los siguientes resultados: de los 3200 encuestados, 1950
# utilizan el subte, 400 se desplazan en moto, 1500 van en colectivo, 800 se desplazan en colectivo y
# subte, además ninguno de los que se transporta en moto utiliza colectivo o subte.
# a. El número de personas que solo utiliza el subte es…. 1150
# b. Las persona que solo utilizan máximo 2 medios de transporte son… 800

# from matplotlib import pyplot as plt
# from matplotlib_venn import *
# from matplotlib.patches import Circle

# # dibujamos los diagramas
# diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
#  "Subte", "Moto", "Colectivo"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))
# # establecemos el tamaño de la fuente
# for subset in ("111", "110", "101", "100", "011", "010", "001"):
#  diagram.get_label_by_id(subset).set_fontsize(16)

# c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)
# # transferimos los resultados de las operaciones
# diagram.get_label_by_id('100').set_text('1150')
# diagram.get_label_by_id('100').set_color('green')
# diagram.get_label_by_id('010').set_text('400')
# diagram.get_label_by_id('010').set_color('green')
# diagram.get_label_by_id('001').set_text('700')
# diagram.get_label_by_id('001').set_color('green')
# diagram.get_label_by_id('110').set_text('0')
# diagram.get_label_by_id('110').set_color('blue')
# diagram.get_label_by_id('011').set_text('0')
# diagram.get_label_by_id('011').set_color('blue')
# diagram.get_label_by_id('101').set_text('800')
# diagram.get_label_by_id('101').set_color('blue')
# diagram.get_label_by_id('111').set_text('0')
# diagram.get_label_by_id('111').set_color('red')
# plt.text(0.50, -0.65, s='150 no usan este tipo de Trasporte',size=7)
# plt.show()

################################################################
# 3. Se encuesta a 150 familias consultando por el nivel educacional actual de sus hijos.
# Los resultados obtenidos son:
# ▪ 10 familias tienen hijos en Enseñanza Básica, Enseñanza Media y Universitaria.
# ▪ 16 familias tienen hijos en Enseñanza Básica y Universitaria
# ▪ 30 familias tienen hijos en Enseñanza Media y Enseñanza Básica.
# ▪ 22 familias tienen hijos en Enseñanza Media y Universitaria.
# ▪ 72 familias tienen hijos en Enseñanza Media.
# ▪ 71 familias tienen hijos en Enseñanza Básica.
# ▪ 38 familias tienen hijos en Enseñanza Universitaria.
# Con la información anterior, deducir:
# a. El número de familias que solo tienen hijos universitarios. 0
# b. El número de familias que tienen hijos solo en dos niveles. 68
# c. El número de familias que tienen hijos que no estudian. 27

# from matplotlib import pyplot as plt
# from matplotlib_venn import *
# from matplotlib.patches import Circle

# # dibujamos los diagramas
# diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
#  "Basica", "Media", "Universitaria"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))
# # establecemos el tamaño de la fuente
# for subset in ("111", "110", "101", "100", "011", "010", "001"):
#  diagram.get_label_by_id(subset).set_fontsize(16)

# c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)
# # transferimos los resultados de las operaciones
# diagram.get_label_by_id('100').set_text('25')
# diagram.get_label_by_id('100').set_color('green')
# diagram.get_label_by_id('010').set_text('20')
# diagram.get_label_by_id('010').set_color('green')
# diagram.get_label_by_id('001').set_text('0')
# diagram.get_label_by_id('001').set_color('green')
# diagram.get_label_by_id('110').set_text('30')
# diagram.get_label_by_id('110').set_color('blue')
# diagram.get_label_by_id('011').set_text('22')
# diagram.get_label_by_id('011').set_color('blue')
# diagram.get_label_by_id('101').set_text('16')
# diagram.get_label_by_id('101').set_color('blue')
# diagram.get_label_by_id('111').set_text('10')
# diagram.get_label_by_id('111').set_color('red')
# plt.text(0.50, -0.65, s='27 No estudian',size=7)
# plt.show()

################################################################
# #4. Una encuesta sobre 500 estudiantes inscriptos en una o más asignaturas de Matemática, Física y Química
# durante un semestre, reveló los siguientes números de estudiantes en los cursos indicados: Matemática 329,
# Física 186, Química 295, Matemática y Física 83, Matemática y Química 217, Física y Química 63. Cuántos
# alumnos estarán inscriptos en:
# a) Los tres cursos
# b) Matemática pero no Química
# c) Física pero no matemática
# d) Química pero no Física
# e) Matemática o Química, pero no Física
# f) Matemática y Química, pero no Física
# g) Matemática pero no Física ni Química

from matplotlib import pyplot as plt
from matplotlib_venn import *
from matplotlib.patches import Circle

# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
 "Matematica", "Fisica", "Quimica"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))
# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
 diagram.get_label_by_id(subset).set_fontsize(16)

c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)
# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text('23')
diagram.get_label_by_id('100').set_color('green')
diagram.get_label_by_id('010').set_text('40')
diagram.get_label_by_id('010').set_color('green')
diagram.get_label_by_id('001').set_text('15')
diagram.get_label_by_id('001').set_color('green')
diagram.get_label_by_id('110').set_text('83')
diagram.get_label_by_id('110').set_color('blue')
diagram.get_label_by_id('011').set_text('63')
diagram.get_label_by_id('011').set_color('blue')
diagram.get_label_by_id('101').set_text('217')
diagram.get_label_by_id('101').set_color('blue')
diagram.get_label_by_id('111').set_text('59')
diagram.get_label_by_id('111').set_color('red')
plt.text(0.50, -0.65, s='59 estan inscriptos a las 3',size=7)
plt.show()












