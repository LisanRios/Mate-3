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
#****************************************************************
#tarea 
#
#1. ¿Qué se emitirá cuando se ejecute el siguiente código?
# def test(a, b = 5):
#  print(a, b)
# test(-3)
# A. a, b
# B. -3, b
# C. a, 5
# D. -3, 5 (*)
# E. -3 5
#
# # 2 2. ¿Qué valor se emite cuando se ejecuta el siguiente código?
# name = "Jane Doe"
# def myFunction(parameter):
#  value = "First"
#  value = parameter
#  print (value)
# myFunction("Second")
# A. value
# B. Second (*)
# C. parameter
# E. Jane Doe
#
# 3. ¿Qué emite el siguiente código?
# def pow(b, p):
#  y = b ** p
#  return y
# def square(x):
#  a = pow(x, 2)
#  return a
# n = 5
# result = square(n)
# print(result)
# A. 5
# B. 10
# C. 25 (*)
# D. 32
# E. 3125
#
# 4. Considere el siguiente código. ¿Qué emite?
# def rem(a, b):
#  return a % b
# print(rem(3,7))
# A. 0
# B. 3 (*)
# C. 7
# D. 1
#
# 5. ¿Qué se devolverá después de llamar?
# def modulus(num1, num2):
#  answer = num1 % num2
#  return answer
# A. 5 y 5.2 y 1
# B. 5 y 95.3 y 0 (*)
# C. 100 y 95.3 y 12
# D. 95 y 100.5 y 0
# E. 5 y 100.5 y 1
#
# 6. ¿Qué se emitirá después de llamar a divide(100, 95), divide(5, 7), divide(7, 5)?
# def divide(num1, num2):
#  single_div_answer = num1 / num2
#  print(round(single_div_answer, 2))
#  double_div_answer = num1 // num2
#  print(round(double_div_answer, 2))
# A. 1, 1.05, 0, 0.71, 1, 1.4
# B. 1.05, 5, 0.71, 5, 1.4, 2
# C. 1.05, 2, 0.71, 1, 1.4, 2
# D. 1.05, 1, 0.71, 1, 1.4, 1
# E. 1.05, 1, 0.71, 0, 1.4, 1 (*)
#
# 7. Después de ejecutar el siguiente código, ¿cuál será el resultado?
# def addition(num1, num2):
#  return(num1 + num2)
# def subtraction(num1, num2):
#  print(num1 - num2)
# def main():
#  add_answer = addition(2, 4)
#  new_add_answer = addition(add_answer, 105)
#  print(subtraction(new_add_answer, 200))
# main()
# A. None y -89
# B. None
# C. -89
# D. -89 y None (*)
#
# 8. Dado el siguiente código, ¿qué emitirá la función?
# def countodd(lst):
#  num_of_odd = 0
#  for item in lst:
#  if item % 2 == 1:
#  num_of_odd += 1
#  return num_of_odd
# print(countodd([1,2,3,4,5]))
# A. 1
# B. 2
# C. 3 (*)
# D. 4
# E. 5
#
# 9. ¿Después de cuántas iteraciones se ejecuta el break?
# def divide_by_two_until_one(num):
#  count = 0
#  while (True):
#  num = num/2
#  count = count + 1
#  if (num <= 1):
#  break
#  return count
# print(divide_by_two_until_one(50))
# A. 50
# B. 25
# C. 5
# D. 6 (*)
# E. 2
#
# 10. ¿Cuál de los siguientes valores para x,y,z daría como resultado que la función devolviera "True"?
# def addition(x,y,z):
#  if (x + y) == z:
#  return "True"
#  else:
#  return "False"
# A. x = 5, y = 6, z = 11 (*)
# B. x = 1, y = 5, z = 6 (*)
# C. x = 1, y = 3, z = 10
# D. x = -2, y = 1, z = -1 (*)
# E. x = 50, y = 41, z = 94 
#
# 11. Qué devuelve list_transformation([0, -2, 5.2, 1])?
# def list_transformation(lst):
#  lst.sort()
#  sum_of_lst = sum(lst)
#  lst.append(sum_of_lst)
#  return lst
# A. [-2, 0, 1, 4.2, 5.2]
# B. [-2, 0, 1, 5.2, 4.2] (*)
# C. [4.2, -2, 0, 1, 5.2]
# D. [0, -2, 5.2, 1, 4.2]
# E. [5.2, 1, 0, -2, 4.2]
#
# 12. ¿Qué imprimirá el siguiente código?
# def mystery(str):
#  out = ""
#  for char in str:
#  if char == "i":
#  break
#  if char == 'a':
#  continue
#  out += char
#  return out
# print(mystery("walking"))
# A. walking
# B. wlking
# C. wlk (*)
# D. wlkng
#
# 13. ¿Cuál sería la salida cuando se llama: tup_and_list_transform((16, 7, 100, 0, 27),(84, 99, 78, 200, -7))
# def tup_and_list_transform(tup1, tup2):
#  list_tup1 = list(tup1)
#  list_tup2 = list(tup2)
#  list_tup1.reverse()
#  return tuple(zip(list_tup1, list_tup2))
# A. (0, 7, 16, 27, 100, 84, 99, 78, 200, -7)
# B. (27, 0, 100, 7, 16, 84, 99, 78, 200, -7)
# C. ((0, 84), (7, 99), (16, 78), (27, 200), (100, -7))
# D. ((27, 84), (0, 99), (100, 78), (7, 200), (16, -7)) (*)
#
# 14. ¿Qué devuelve la siguiente función?
# def slice_exercise():
#  alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
#  print(alist[2:4])
# A. [ [ ], 3.14, False]
# B. ["cat", [56, 57, "dog"]] (*)
# C. [ [56, 57, "dog"], [ ], 3.14, False]
# D. [27, "cat"]
################################################################
# Resolver:
# 1. Qué salida tiene el siguiente código?
# def display_person(*args):
#  for i in args:
#  print(i)
# display_person(name="Emma", age="25")
# A. TypeError (*)
# B. Emma
#  25
# C. name
#  age
#
# 2. ¿ Cuál es el resultado de la siguiente llamada a función ?
# def display(**kwargs):
#  for i in kwargs:
#  print(i)
# display(emp="Kelly", salary=9000)
# A. TypeError
# B. Kelly
#  9000
# C. ('emp', 'Kelly')
#  ('salary', 9000)
# D. emp (*)
#  salary
#
# 3. Elija la declaración de función correcta para que podamos ejecutar la siguiente llamada con éxito:
# fun1(25, 75, 55)
# fun1(10, 20)
# A. def fun1(**kwargs)
# B. No es posible en Python
# C. def fun1(args*)
# D. def fun1(*data)
########################################################################
# Resolver:
# 1. Completa el código con la función lambda:
# radio_cm = int(input("Ingresa el radio del círculo en cm.\n"))
# PI = 3.14159265359
# calcula_area = ______________________________
# area = round(calcula_area(radio_cm),2)
# print(f"El área del círculo es de {area} cm.")
# 
#RTA=
# radio_cm = int(input("Ingresa el radio del círculo en cm.\n"))
# PI = 3.14159265359
# calcula_area = lambda r: r**2 * PI
# area = round(calcula_area(radio_cm), 2)
# print(f"El área del círculo es de {area} cm².")
#
# 2. Qué salida tiene el siguiente código?
# (lambda *args: sum(args))(1, 2, 3)
#
#RTA= 
#print((lambda *args: sum(args))(1, 2, 3)) # 6 
#
# 3. Desarrolla la función cuadrado usando lambda.
#
#RTA= 
#print((lambda num: num * 2 )(2))
