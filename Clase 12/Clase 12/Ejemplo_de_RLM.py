#!/usr/bin/env python
# coding: utf-8

# # Regresión lineal Múltiple

# Realizamos una regresión lineal que involucra dos variables. Casi todos los problemas del mundo real con los que nos vamos a encontrar tendrán más de dos variables. La regresión lineal que involucra múltiples variables se llama __"regresión lineal múltiple"__ o __"regresión lineal multivariable"__. 
# 
# Los pasos para realizar la regresión lineal múltiple son casi similares a los de la regresión lineal simple. La diferencia radica en la evaluación. Se puede utilizar para averiguar qué factor tiene el mayor impacto en el resultado previsto y cómo se relacionan las diferentes variables entre sí.

# Tenemos un dataset de la calidad del vino tinto. El dataset corresponde a las variantes rojas del vino portugués "Vinho Verde". Sólo se dispone de variables físico-químicas (los insumos) y sensoriales (el producto) (por ejemplo, no hay datos sobre los tipos de uva, la marca del vino, el precio de venta del vino, etc.).
# 
# Tendremos en cuenta varios atributos de entrada y basándonos en estos atributos haremos la __predicción sobre la calidad del vino__.

# #### Información de los datos
# 
# fixed acidity: :la mayoría de los ácidos involucrados con el vino o fijos o no volátiles (no se evaporan fácilmente).
# 
# volatile acidity: la cantidad de ácido acético en el vino, que a niveles demasiado altos puede conducir a un sabor desagradable a vinagre.
# 
# citric acid: se encuentra en pequeñas cantidades, el ácido cítrico puede agregar "frescura" y sabor a los vinos.
# 
# residual sugar: la cantidad de azúcar que queda después de que se detiene la fermentación, es raro encontrar vinos con menos de 1 gramo / litro y vinos con más de 45 gramos / litro se consideran dulces.
# 
# chlorides: la cantidad de sal en el vino.
# 
# free sulfur dioxide: la forma libre de SO2 existe en equilibrio entre el SO2 molecular (como gas disuelto) y el ion bisulfito; previene el crecimiento microbiano y la oxidación del vino.
# 
# total sulfur dioxide: cantidad de formas libres y unidas de S02; en bajas concentraciones, el SO2 es en su mayoría indetectable en el vino, pero a concentraciones libres de SO2 superiores a 50 ppm, el SO2 se hace evidente en la nariz y el sabor del vino.
# 
# density: la densidad del vino es cercana a la del agua dependiendo del porcentaje de alcohol y contenido de azúcar.
# 
# pH: describe qué tan ácido o básico es un vino en una escala de 0 (muy ácido) a 14 (muy básico); la mayoría de los vinos están entre 3-4 en la escala de pH.
# 
# sulphates: un aditivo del vino que puede contribuir a los niveles de gas de dióxido de azufre (S02), que actúa como antimicrobiano y antioxidante.
# 
# alcohol: el porcentaje de contenido alcohólico del vino.
# 
# quality: variable de salida (basada en datos sensoriales, puntuación entre 0 y 10).

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('archs/winequality.csv')
df.head()


# #### Exploración de datos

# In[3]:


df.shape


# #### Detalles estadísticos del conjunto de datos:

# In[4]:


df.describe()


# #### Comprobar valores faltantes

# In[5]:


df.isnull().any()


# _Todas las columnas deben dar False, en caso de que para cualquier columna se encuentre el resultado True, entonces se pueden eliminar todos los valores nulos de esa columna usando el código siguiente 'dataset=dataset.fillna(method='ffill')'_

# #### Matriz de correlación
# 
# Muestra el grado de correlaciones, de cada variable en el conjunto de datos, con cada otra variable en el conjunto de datos. Es una representación de todos estos coeficientes de correlación de cada variable individual en los datos con cada otra variable en los datos.
# 
# El grado de correlación entre dos variables cualesquiera se representa de dos maneras, el color del cuadro o caja y el número dentro. Cuanto más fuerte sea el color, mayor será la magnitud de la correlación.
# 
# Cuanto más cerca esté el número de 1, mayor será la correlación. Si el número es positivo, establece una correlación positiva. Si es negativo establece una correlación negativa. 
# 
# 1 y -1 establecen correlaciones perfectas entre las variables.

# In[6]:


corr = df.corr()
plt.subplots(figsize=(12,8))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, fmt='.0%',
            cmap=sns.diverging_palette(240, 10, as_cmap=True)) 


# In[7]:


corr['quality'].abs().sort_values(ascending=False)


# _El alcohol es la característica más correlacionada._ 

# In[8]:


X = df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 
             'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
             'pH', 'sulphates','alcohol']].values
y = df['quality'].values


# Comprobemos el valor medio de la columna "calidad".

# In[9]:


'''
Valor promedio de la calidad del vino
'''
fig, ax1 = plt.subplots(figsize=(8,6))
ax1.hist(df.quality,align='left',alpha=0.5)
ax1.set_xlabel('Calificación de calidad')


# 
#  
# Como podemos observar, la mayoría de las veces el valor es 5 o 6. A continuación, dividimos el 80% de los datos para el conjunto de entrenamiento y  el 20% de los datos al conjunto de pruebas usando el código de abajo.

# In[10]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# #### Entrenamiento
# 
# Ahora vamos a entrenar nuestro modelo

# In[11]:


regressor = LinearRegression() 
regressor.fit(X_train, y_train)


# In[12]:


df = df.drop(['quality'], axis=1)
df = df.T


# In[13]:


df = df.index
df


# Como se ha dicho antes, en el caso de la regresión lineal multivariable, el modelo de regresión tiene que encontrar los coeficientes más óptimos para todos los atributos. Para ver qué coeficientes ha elegido nuestro modelo de regresión, ejecutamos el siguiente código:

# In[14]:


coeff_df = pd.DataFrame(regressor.coef_, df, columns=['Coefficient']) 
coeff_df


# Significa que para un aumento de una unidad en la "densidad", hay una disminución de 31,51 unidades en la calidad del vino. Del mismo modo, la disminución en una unidad de los "cloruros" resulta en un aumento de 1,87 unidades en la calidad del vino. Podemos ver que el resto de los atributos tienen muy poco efecto en la calidad del vino.”
# 
# #### Predicción sobre los datos de la prueba

# In[15]:


y_pred = regressor.predict(X_test)


# Revisemos la diferencia entre el valor real y el valor previsto.

# In[16]:


df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)
df1.head()


# #### Comparación entre el valor real y el valor de la predicción
# 
# Ahora vamos a graficar la comparación de los valores reales y los valores de la predicción

# In[17]:


df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='darkgreen')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
'''
Gráfico de barras mostrando las diferencias entre los valores reales y los de la predicción.
'''


# El modelo ha dado resultados aproximados de predicción, aunque hay valores que evidencian una diferencia notable. 

# #### Métricas
# 
# El paso final es evaluar el rendimiento del algoritmo. Lo haremos encontrando los valores de MAE, MSE y RMSE. 

# In[18]:


print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred)) 
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred)) 
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# Se puede ver que el valor de la raíz del error cuadrático medio es de 0,62, que es ligeramente superior al 10% del valor de la media que es de 5,63. Esto significa que nuestro algoritmo no fue muy preciso pero aún así puede hacer predicciones razonablemente buenas.
# 
# Hay muchos factores que pueden haber contribuido a esta inexactitud, por ejemplo:
# 
# 1. Necesita más datos: Necesitamos una gran cantidad de datos para obtener la mejor predicción posible.
# 2. Malas suposiciones: Hicimos la suposición de que estos datos tienen una relación lineal, pero puede que no sea así. Visualizar los datos puede ayudar a determinar eso.
# 3. Atributos pobres: Los atributos  que usamos pueden no tener una correlación lo suficientemente alta con los valores que tratamos de predecir.

# #### Regresión aplicada a un grupo de características
# 
# A modo de ejemplo se realiza una estimación de calidad basada en solo un grupo de características. Para ello vamos a utilizar Regresión Lineal. También trazaremos los valores de predicción y calidad verdadera.

# In[19]:


df = pd.read_csv('archs/winequality.csv')
X = df.loc[:,['alcohol','sulphates','citric acid','volatile acidity']]
y = df.iloc[:,11]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[20]:


regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_prediction_lr = regressor.predict(X_test)
y_prediction_lr = np.round(y_prediction_lr)


# In[21]:


plt.scatter(y_test,y_prediction_lr)
plt.title("Predicción usando Regresión Lineal")
plt.xlabel("Calidad Real")
plt.ylabel("Predicción")
plt.show()


# In[ ]:




