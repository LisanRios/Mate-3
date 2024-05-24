import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from itertools import cycle
import plotly.graph_objects as go 
import plotly.express as px 
from plotly.subplots import make_subplots 

# Cargar los datos
Monero = pd.read_csv("C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Segundo Trabajo Práctico Integrador de Matemática III Lisandro Rios/archive/coin_Monero.csv")
Ethereum = pd.read_csv("C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Segundo Trabajo Práctico Integrador de Matemática III Lisandro Rios/archive/coin_Ethereum.csv")
WrappedBitcoin = pd.read_csv("C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Segundo Trabajo Práctico Integrador de Matemática III Lisandro Rios/archive/coin_WrappedBitcoin.csv")
Bitcoin = pd.read_csv("C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Segundo Trabajo Práctico Integrador de Matemática III Lisandro Rios/archive/coin_Bitcoin.csv")

################################################### Monero #############################################################
# Creación de una variable para predecir '5' días en el futuro
projection_Monero = 5
# Creación de una nueva columna con el nombre prediction
Monero['Prediction'] = Monero[['Close']].shift(-projection_Monero)

################################################### Ethereum #############################################################
# Creación de una variable para predecir '5' días en el futuro
projection_Ethereum = 5
# Creación de una nueva columna con el nombre prediction
Ethereum['Prediction'] = Ethereum[['Close']].shift(-projection_Ethereum)

################################################### WrappedBitcoin #############################################################
# Creación de una variable para predecir '5' días en el futuro
projection_WrappedBitcoin = 5
# Creación de una nueva columna con el nombre prediction
WrappedBitcoin['Prediction'] = WrappedBitcoin[['Close']].shift(-projection_WrappedBitcoin)

################################################### Bitcoin #############################################################
# Creación de una variable para predecir '5' días en el futuro
projection_Bitcoin = 5
# Creación de una nueva columna con el nombre prediction
Bitcoin['Prediction'] = Bitcoin[['Close']].shift(-projection_Bitcoin)

################################################### Monero #############################################################
# Visualización de los datos de Monero
visualize_Monero = cycle(['Open', 'Close', 'High', 'Low', 'Prediction'])

fig = px.line(Monero, x=Monero.Date, y=[Monero['Open'], Monero['Close'], 
        Monero['High'], Monero['Low'], Monero['Prediction']],
        labels={'Date': 'Date', 'value': 'Price'})
fig.update_layout(title_text='Monero', font_size=15, font_color='black', legend_title_text='Parameters')
fig.for_each_trace(lambda t: t.update(name=next(visualize_Monero)))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

fig.show()

################################################### Ethereum #############################################################
# Visualización de los datos de Ethereum
visualize_Ethereum = cycle(['Open', 'Close', 'High', 'Low', 'Prediction'])

fig = px.line(Ethereum, x=Ethereum.Date, y=[Ethereum['Open'], Ethereum['Close'], 
                                          Ethereum['High'], Ethereum['Low'], Ethereum['Prediction']],
             labels={'Date': 'Date', 'value': 'Price'})
fig.update_layout(title_text='Ethereum', font_size=15, font_color='black', legend_title_text='Parameters')
fig.for_each_trace(lambda t: t.update(name=next(visualize_Ethereum)))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

fig.show()

################################################### WrappedBitcoin #############################################################
# Visualización de los datos de WrappedBitcoin
visualize_WrappedBitcoin = cycle(['Open', 'Close', 'High', 'Low', 'Prediction'])

fig = px.line(WrappedBitcoin, x=WrappedBitcoin.Date, y=[WrappedBitcoin['Open'], WrappedBitcoin['Close'], 
                                          WrappedBitcoin['High'], WrappedBitcoin['Low'], WrappedBitcoin['Prediction']],
             labels={'Date': 'Date', 'value': 'Price'})
fig.update_layout(title_text='WrappedBitcoin', font_size=15, font_color='black', legend_title_text='Parameters')
fig.for_each_trace(lambda t: t.update(name=next(visualize_WrappedBitcoin)))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

fig.show()

################################################### Bitcoin #############################################################
# Visualización de los datos de Bitcoin
visualize_Bitcoin = cycle(['Open', 'Close', 'High', 'Low', 'Prediction'])

fig = px.line(Bitcoin, x=Bitcoin.Date, y=[Bitcoin['Open'], Bitcoin['Close'], 
                                          Bitcoin['High'], Bitcoin['Low'], Bitcoin['Prediction']],
             labels={'Date': 'Date', 'value': 'Price'})
fig.update_layout(title_text='Bitcoin', font_size=15, font_color='black', legend_title_text='Parameters')
fig.for_each_trace(lambda t: t.update(name=next(visualize_Bitcoin)))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

fig.show()

################################################### Monero #############################################################
# Creación del conjunto de datos independiente (X)
X_Monero = np.array(Monero[['Close']])
X_Monero = X_Monero[:-projection_Monero]
# Creación del conjunto de datos dependiente (y)
y_Monero = Monero['Prediction'].values
y_Monero = y_Monero[:-projection_Monero]

################################################### Ethereum #############################################################
# Creación del conjunto de datos independiente (X)
X_Ethereum = np.array(Ethereum[['Close']])
X_Ethereum = X_Ethereum[:-projection_Ethereum]
# Creación del conjunto de datos dependiente (y)
y_Ethereum = Ethereum['Prediction'].values
y_Ethereum = y_Ethereum[:-projection_Ethereum]

################################################### WrappedBitcoin ########################################################
# Creación del conjunto de datos independiente (X)
X_WrappedBitcoin = np.array(WrappedBitcoin[['Close']])
X_WrappedBitcoin = X_WrappedBitcoin[:-projection_WrappedBitcoin]
# Creación del conjunto de datos dependiente (y)
y_WrappedBitcoin = WrappedBitcoin['Prediction'].values
y_WrappedBitcoin = y_WrappedBitcoin[:-projection_WrappedBitcoin]

################################################### Bitcoin #############################################################
# Creación del conjunto de datos independiente (X)
X_Bitcoin = np.array(Bitcoin[['Close']])
X_Bitcoin = X_Bitcoin[:-projection_Bitcoin]
# Creación del conjunto de datos dependiente (y)
y_Bitcoin = Bitcoin['Prediction'].values
y_Bitcoin = y_Bitcoin[:-projection_Bitcoin]

# Función para entrenar el modelo y hacer predicciones
def train_and_predict(X, y, projection):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    X_forecast = X[-projection:]
    predictions = model.predict(X_forecast)
    return predictions

# Hacer predicciones
pred_Monero = train_and_predict(X_Monero, y_Monero, projection_Monero)
pred_Ethereum = train_and_predict(X_Ethereum, y_Ethereum, projection_Ethereum)
pred_WrappedBitcoin = train_and_predict(X_WrappedBitcoin, y_WrappedBitcoin, projection_WrappedBitcoin)
pred_Bitcoin = train_and_predict(X_Bitcoin, y_Bitcoin, projection_Bitcoin)

# Redondear predicciones
pred_Monero_rounded = np.round(pred_Monero, 2)
pred_Ethereum_rounded = np.round(pred_Ethereum, 2)
pred_WrappedBitcoin_rounded = np.round(pred_WrappedBitcoin, 2)
pred_Bitcoin_rounded = np.round(pred_Bitcoin, 2)

# Imprimir predicciones
print("CONCLUSIÓN\n")
print(f"Las predicciones del modelo de regresión lineal para los próximos 5 días a partir de los datos de Monero son {pred_Monero_rounded}\n")
print(f"Las predicciones del modelo de regresión lineal para los próximos 5 días a partir de los datos de Ethereum son {pred_Ethereum_rounded}\n")
print(f"Las predicciones del modelo de regresión lineal para los próximos 5 días a partir de los datos de WrappedBitcoin son {pred_WrappedBitcoin_rounded}\n")
print(f"Las predicciones del modelo de regresión lineal para los próximos 5 días a partir de los datos de Bitcoin son {pred_Bitcoin_rounded}\n")
