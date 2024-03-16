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
from matplotlib import pyplot as plt
from matplotlib_venn import venn3
plt.figure(figsize=(7,7))
dv = venn3(subsets=(1,2,3,4,5,6,7), set_labels = ('A', 'B', 'C'))
from matplotlib.patches import Circle
# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
 "Laptop", "Celular", "Ipod"), set_colors=("#FFFFFF", "#FFFFFF", "#FFFFFF"))
# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
 diagram.get_label_by_id(subset).set_fontsize(16)

c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), color="#000000", alpha=0.5, linewidth=3)
# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text('10')
diagram.get_label_by_id('100').set_color('green')
diagram.get_label_by_id('010').set_text('0')
diagram.get_label_by_id('010').set_color('green')
diagram.get_label_by_id('001').set_text('19')
diagram.get_label_by_id('001').set_color('green')
diagram.get_label_by_id('110').set_text('12')
diagram.get_label_by_id('110').set_color('blue')
diagram.get_label_by_id('011').set_text('48')
diagram.get_label_by_id('011').set_color('blue')
diagram.get_label_by_id('101').set_text('8')
diagram.get_label_by_id('101').set_color('blue')
diagram.get_label_by_id('111').set_text('50')
diagram.get_label_by_id('111').set_color('red')
plt.text(0.50, -0.65, s='3',size=14)
plt.show()
