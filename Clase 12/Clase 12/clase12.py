# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df= pd.read_csv('C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Clase 12/Clase 12/archs/detalles_autos2.csv')
# df = df.drop(['name','year','fuel','seller_type','transmission','owner'], axis=1)

# print(df)

# Q1 = df['km_driven'].quantile(0.25)
# Q3 = df['km_driven'].quantile(0.75)
# IQR = Q3 - Q1 
# # Definir límites para identificar valores atípicos
# limite_inferior = Q1 - 1.5 * IQR
# limite_superior = Q3 + 1.5 * IQR

# # Identificar valores atípicos
# valores_atipicos = df[(df['km_driven'] < limite_inferior) | (df['km_driven'] > limite_superior)] 

# print("El valor del IRQ es: ", IQR)
# print("El valor del límite inferior es :", limite_inferior)
# print("El valor del límite superior es :", limite_superior)
# print("Valores Atípicos Detectados :", valores_atipicos)

# np.sort(df['km_driven'])

# g = sns.boxplot(data = df, x = 'selling_price')
# g.set_title('KM Driven')
# g.set_xlabel('Costo')

# plt.show()

# import numpy as np
# import pandas as pd
# from sklearn import metrics
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# df = pd.read_csv('C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Clase 12/Clase 12/archs/detalles_autos2.csv')

# y = df['selling_price']
# y_pred = df['km_driven']

# print('Error cuadrático medio (MSE):', metrics.mean_squared_error(y, y_pred))

# print('Raíz cuadrada del error cuadrático medio (RMSE) :', np.sqrt(metrics.mean_squared_error(y, y_pred)))

# print('Error Medio Absoluto (MAE):', metrics.mean_absolute_error(y, y_pred))

# print('Error absoluto mediano = ', metrics.median_absolute_error(y, y_pred))

# print('R^2', metrics.r2_score(y, y_pred))

# r2 = metrics.r2_score(y, y_pred)
# r2_adj = r2 - (y.shape[0] - 1)/(y.shape[0] - 2 - 1) * (1 - r2)
# print('R^2 ajustado', r2_adj)

