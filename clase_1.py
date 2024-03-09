# 1) De que tipo de balores son: "19" y "4.56"
#
#       a. Float
# 
# 2) que salida tiene la instruccion : print("1,000,000")
#
#       A. 1,000,000
#
# 3)como asignar la variable nombre la cadena martina?
#
#       B. nombre = "martina"
#
# 4) cual es el valor de var3 despues de ejecutar el siguiete codigo?
#
#       C. var3 = perro
#
# 5) cual de las siguietes lineas de codigo es una expresion?
#
#       D.todas las anteriores
#
# 6) que emite el siguiente codigo?
#
#   result= 4 + -2 * 3
#   print(result)
#
#   -2
#
# 7) que emite el siguiente codigo?
#
#   result= (4 + -2) * 3
#   print(result)
#
#   6
#
# 8) que emite 
#
#   result= 18%5
#   print(result)
#   
#   3
#
# 9) que emite
#
#   result= 2%3
#   print(result)
#   
#   2
#
# 10) que emite en el orden correcto 
#
#   Ninguna xd
#
# 11) que emite 
#
#   a = "vamos ar"
#   es = "!"
#   print(a+es*2)
#
# 12) tipo de error al escribir mal
#
# sintaxerror
#
# 13)
#
# x = -10
# if x < 0:
#     print("Numero negativo ", x, " No es valido")
# else:
#     if x > 0:
#         print(x, "es valido")
#     else:
#         print("es 0")
# if x < 0:
#     print("Numero negativo ", x, " No es valido")
# elif x > 0:
#     print(x, "es valido")
# else:
#         print("es 0")
# if x < 0:
#     print("Numero negativo ", x, " No es valido")
# if x > 0:
#     print(x, "es valido")
# else:
#     print("es 0")
#
# 14)
# c. 
# x = 3
# if(x > 2):
#     x = x * 2
# if(x < 4):
#     x = 0
# print(x)
#
# 15) D.
#
# 16) Falso
# a = 3
# b = (a != 3)
# print(b)
#
# 17) C.
#
# 18) Se repite indefinidamente.
#
# 19) D. 16
#
# 23) 
#
# for i in range (0,5):
#     print("*" * 5)
# 1. ¿Qué emitirá el siguiente programa Python?
# def fred():
#  print("Zap")
# In [1]:
# def mensajes():
#  print("Este es el primer ejemplo")
# mensajes()
# print("Programa terminado.")
# In [2]: mens()
# print("Programa terminado.")
# def mens():
#  print("Este es el primer ejemplo")
# def jane():
#  print("ABC")
# jane()
# fred()
# jane()
# A. Zap ABC jane fred jane
# B. Zap ABC Zap
# C. ABC Zap jane (#)
# D. ABC Zap ABC
# E. Zap Zap Zap
#
# 2. Dada la variable item, ¿cómo tomaría las letras "tebo"?
# def notebook():
#  item = "notebook"
#  # ¿Qué pasa aquí?
# notebook()
# A. print(item[2:7])
# ()B. print(item[2:6])
# ()C. print(item[-6:-2])
# D. print(item[3] + item[4] + item[5] + item[6])
# E. print(item[3:7])

# 1. Qué variables contiene el bloque de código?
# from datetime import datetime
# def get_name():
#  first = input("Ingresa tu nombre")
#  print("Hola " + first)
#  age_str = input("Ingresa tu edad")
#  today = datetime.today()
#  age = int(age_str)
#  birth_year = today.year - age
#  print("Naciste en " + str(birth_year) + " o " + str(birth_year - 1))
# get_name()

# Resolver:
# 1. Qué diferencia hay en las salidas de los siguientes códigos:
# a)
# contador = 0
# funcion4()
# print(d)
# In [7]: x = 0 # Es global por estar fuera de las funciones
# def funcion5():
#  print(x)

# funcion5()
# In [8]: x = 0
# def funcion6():
#  x = 1
#  print(x)

# funcion6()
# print(x)
# In [9]: x = 0
# def funcion7():
#  print(x)
#  x = 1

# funcion7()
# In [10]: x = 0
# print('x antes de test()',x)
# def test():
#  global x
#  print('x dentro de test()',x)
#  x = 1
# test()
# print('x luego de test()',x)
# def aumentar_contador():
#  contador += 1
#  print(contador)
# aumentar_contador()
# aumentar_contador()
# b)
# contador = 0
# def aumentar_contador():
#  global contador
#  contador += 1
#  print(contador)
# aumentar_contador()
# aumentar_contador()

def argsConClaveValor(**clave_valor_args):
 print(type(clave_valor_args))
 for nombre, valor in clave_valor_args.items():
    print(nombre + ': ' + valor)

print("Ejemplo con **kwargs\n")
argsConClaveValor(edad='32', profesion="Ingeniero", nacionalidad="Argentino")
