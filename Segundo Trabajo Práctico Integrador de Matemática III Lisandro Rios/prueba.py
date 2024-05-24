import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from itertools import cycle
import plotly.graph_objects as go 
import plotly.express as px 
from plotly.subplots import make_subplots 

Monero = pd.read_csv("C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Segundo Trabajo Práctico Integrador de Matemática III Lisandro Rios/archive/coin_Monero.csv")
Ethereum = pd.read_csv("C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Segundo Trabajo Práctico Integrador de Matemática III Lisandro Rios/archive/coin_Ethereum.csv")
WrappedBitcoin = pd.read_csv("C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Segundo Trabajo Práctico Integrador de Matemática III Lisandro Rios/archive/coin_WrappedBitcoin.csv")
Bitcoin = pd.read_csv("C:/Users/ivaga/OneDrive/Documentos/GitHub/Mate-3/Segundo Trabajo Práctico Integrador de Matemática III Lisandro Rios/archive/coin_Bitcoin.csv")

def prepare_and_predict(data, projection_days):
    data['Prediction'] = data[['Close']].shift(-projection_days)
    
    X = np.array(data[['Close']])
    X = X[:-projection_days]
    
    y = data['Prediction'].values
    y = y[:-projection_days]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    X_forecast = np.array(data[['Close']])[-projection_days:]
    prediction = model.predict(X_forecast)
    
    return prediction

projection_days = 5

pred_Monero = prepare_and_predict(Monero, projection_days)
pred_Ethereum = prepare_and_predict(Ethereum, projection_days)
pred_WrappedBitcoin = prepare_and_predict(WrappedBitcoin, projection_days)
pred_Bitcoin = prepare_and_predict(Bitcoin, projection_days)

print("CONCLUSIÓN\n")
print(f"Las predicciones del modelo de regresión lineal para los próximos 5 días a partir de los datos de Monero son {pred_Monero}\n")
print(f"Las predicciones del modelo de regresión lineal para los próximos 5 días a partir de los datos de Ethereum son {pred_Ethereum}\n")
print(f"Las predicciones del modelo de regresión lineal para los próximos 5 días a partir de los datos de WrappedBitcoin son {pred_WrappedBitcoin}\n")
print(f"Las predicciones del modelo de regresión lineal para los próximos 5 días a partir de los datos de Bitcoin son {pred_Bitcoin}\n")
