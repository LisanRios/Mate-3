# Importar las librerías necesarias
import os
import csv
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta
from itertools import cycle

# Función para convertir el formato de fecha
def convert_date(date):
    return datetime.strptime(date, "%d.%m.%Y").strftime("%Y-%m-%d %H:%M:%S")

# Función para leer el archivo CSV de entrada y escribir en el archivo CSV de salida
def transform_csv(input_file, output_file, cripto):
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Saltar la primera fila (encabezados)
        data = list(csv_reader)
        data.reverse()  # Invertir el orden de las filas
        
        with open(output_file, mode='w', encoding='utf-8', newline='') as output_csv:
            csv_writer = csv.writer(output_csv)
            csv_writer.writerow(["SNo", "Name", "Symbol", "Date", "High", "Low", "Open", "Close", "Volume", "Marketcap"])
            for idx, row in enumerate(data, start=1):
                fecha = convert_date(row[0])  # Convertir la fecha al nuevo formato
                # Reemplazar las comas y convertir números al formato adecuado
                ultimo = float(row[1].replace('.', '').replace(',', '.'))
                apertura = float(row[2].replace('.', '').replace(',', '.'))
                maximo = float(row[3].replace('.', '').replace(',', '.'))
                minimo = float(row[4].replace('.', '').replace(',', '.'))
                vol = row[5].replace('K', '000').replace('.', '').replace(',', '.')
                var = row[6].replace('%', '').replace(',', '.')
                # Escribir la fila en el nuevo formato
                csv_writer.writerow([idx, cripto, "", fecha, maximo, minimo, apertura, ultimo, vol, 0.0])
    print("Transformación completada.")

# Función para cargar y preprocesar los datos
def load_and_preprocess_data(output_file, projection_Table):
    # Cargar los datos
    Table = pd.read_csv(output_file)
    # Nos aseguramos de que la columna 'Date' sea del tipo datetime
    Table['Date'] = pd.to_datetime(Table['Date'])
    # Creación de una nueva columna con el nombre 'Prediction'
    Table['Prediction'] = Table[['Close']].shift(-int(projection_Table))
    return Table

# Función para crear los conjuntos de datos independientes (X) y dependientes (y)
def create_datasets(Table, projection_Table):
    # Crear el conjunto de datos independiente (X)
    X_Table = np.array(Table[['Close']])
    X_Table = X_Table[:-int(projection_Table)]
    # Crear el conjunto de datos dependiente (y)
    y_Table = Table['Prediction'].values
    y_Table = y_Table[:-int(projection_Table)]
    return X_Table, y_Table

# Función para entrenar el modelo y hacer las predicciones
def train_and_predict(X, y, projection_Table):   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    # Calcular el puntaje R^2 del modelo
    score = model.score(X_train, y_train)
    X_forecast = X[-int(projection_Table):]
    predictions = model.predict(X_forecast)
    return predictions, score

# Función para crear un DataFrame de predicciones futuras
def create_future_dataframe(Table, pred_Table, projection_Table):
    # Calcula las fechas futuras
    future_dates = [Table['Date'].max() + timedelta(days=x) for x in range(1, int(projection_Table) + 1)]
    future_df = pd.DataFrame({'Date': future_dates, 'Prediction': pred_Table})
    return future_df

# Función para visualizar los datos
def visualize_data(Table, future_df, cripto):
    # Concatenar el DataFrame original con el DataFrame de las predicciones
    Table = pd.concat([Table, future_df])
    # Visualización de los datos de la criptomoneda
    visualize_Table = cycle(['Apertura', 'Último', 'Máximo', 'Mínimo', 'Predicción'])
    fig = px.line(Table, x=Table.Date, y=[Table['Open'], Table['Close'], Table['High'], Table['Low'], Table['Prediction']],
                  labels={'Date': 'Fecha', 'Close': 'Precio'})
    fig.update_layout(title_text=cripto, font_size=15, font_color='black', legend_title_text='Parámetros')
    fig.for_each_trace(lambda t: t.update(name=next(visualize_Table)))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.show()

# Función para validar la entrada del usuario
def validate_input(prompt, type_func, condition_func=lambda x: True, error_message="Entrada inválida. Por favor, inténtelo de nuevo."):
    while True:
        try:
            value = type_func(input(prompt))
            if condition_func(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)


# Fuinción para retornar la conclución 
def conclusion(score, pred_Table):
            print("CONCLUSIÓN\n")
            print(f"Regresión lineal del dólar blue: {score} ({score*100}%)")
            print(f"Las predicciones del modelo de regresión lineal para los próximos días son {pred_Table}\n")

# Función principal para ejecutar el análisis
def main():
    while True:
        #Motrar el menú
        print("Menú:")
        print("1. Criptomonedas")
        print("2. Mercado de valores (ingresar URL)")
        print("3. Valor dólar a peso argentino")
        print("4. Salir")

        #Controlar el error    
        option = validate_input("Seleccione una opción: ", int, lambda x: 1 <= x <= 4, "Opción inválida. Por favor, inténtelo de nuevo.")

        if option == 1:
            #El usuario ingresa la criptomoneda a analizar
            cripto = input("Ingrese el nombre de la criptomoneda que desea analizar: ")
            
            # Definición de variables de archivo
            input_file = f"archive/Datos históricos del {cripto}.csv"
            output_file = f"archive/datosActualizados_{cripto}.csv"
            
            #Comprobar si existe en archive
            if not os.path.isfile(input_file):
                print("La criptomoneda especificada no se encontró. Por favor, inténtelo de nuevo.")
                continue
            
            #Validar los dias a proyectar
            projection_days = validate_input("Proyección a días en el futuro: ", int, lambda x: x > 0, "No se puede proyectar menos de 1 día en el futuro. Por favor, inténtelo de nuevo.")
            
            #Transformar el archivo CSV           
            transform_csv(input_file, output_file, cripto)
            
            # Procesamiento de datos y predicciones
            Table = load_and_preprocess_data(output_file, projection_days)
            X_Table, y_Table = create_datasets(Table, projection_days)
            pred_Table, score = train_and_predict(X_Table, y_Table, projection_days)
            future_df = create_future_dataframe(Table, pred_Table, projection_days)

            # Visualización y conclusión
            visualize_data(Table, future_df, cripto)
            conclusion(score, pred_Table)
        
        elif option == 2:
            # Definición de variables de archivo
            cripto = "Bolsa de Valores"
            output_file = f"archive/datosActualizados_{cripto}.csv"
            archivo_csv = f"archive/archivo.csv"
            
            custom_url = input("Ingrese la URL personalizada (dicha url debe ser de esta pagina investing.com/equities/NOMBRE-caracterEspecial-historical-data): ")
            request = requests.get(custom_url)
            soup = BeautifulSoup(request.text) 
            
            # Extracción de datos de la tabla HTML
            tabla_html = soup.find_all("table")[1]
            datos_tabla = pd.read_html(str(tabla_html))[0]
            
            # Exportar los datos de la tabla a un archivo CSV
            datos_tabla.to_csv(archivo_csv, index=None, header=True)   
            # Leer los datos del archivo CSV
            datos_csv = pd.read_csv(archivo_csv)   
            print(datos_csv.head())    
            
            projection_days = validate_input("Proyección a días en el futuro: ", int, lambda x: x > 0, "No se puede proyectar menos de 1 día en el futuro. Por favor, inténtelo de nuevo.")
            
            #Transformar el archivo CSV           
            transform_csv(archivo_csv, output_file, cripto)
            
            # Procesamiento de datos y predicciones
            Table = load_and_preprocess_data(output_file, projection_days)
            X_Table, y_Table = create_datasets(Table, projection_days)
            pred_Table, score = train_and_predict(X_Table, y_Table, projection_days)
            future_df = create_future_dataframe(Table, pred_Table, projection_days)

            # Visualización y conclusión
            visualize_data(Table, future_df, "Mercado de Valores")
            conclusion(score, pred_Table)
        
        elif option == 3:
            # Definición de variables de archivo
            cripto = "Dolar a peso argentino"
            output_file = f"archive/datosActualizados_{cripto}.csv"
            archivo_csv = f"archive/archivo.csv"

            # Mostrar opciones al usuario
            print("Opciones")
            print("1. Dolar Blue a peso argentino")
            print("2. Dolar a peso argentino")

            # Solicitar la opción del usuario
            while True:
                try:
                    tipoDolar = int(input("Elegir el tipo de dolar a saber: "))
                    if tipoDolar in [1, 2]:
                        break
                    else:
                        print("Por favor, elija una opción válida (1 o 2).")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número (1 o 2).")

            # Seleccionar la URL basada en la opción del usuario
            if tipoDolar == 1:
                url = "https://es.investing.com/currencies/usd-arsb-historical-data"
                tabla = 1
            else:
                url = "https://es.investing.com/currencies/usd-ars-historical-data"
                tabla = 2

            # Realizar la solicitud HTTP
            request = requests.get(url)
            soup = BeautifulSoup(request.text, 'html.parser')

            # Extracción de datos de la tabla HTML
            tabla_html = soup.find_all("table")[tabla]
            datos_tabla = pd.read_html(str(tabla_html))[0]

            # Exportar los datos de la tabla a un archivo CSV
            datos_tabla.to_csv(archivo_csv, index=None, header=True)

            # Leer los datos del archivo CSV
            datos_csv = pd.read_csv(archivo_csv)
            print(datos_csv.head())

            # Solicitar la proyección a días en el futuro
            projection_days = validate_input(
                "Proyección a días en el futuro: ",
                int,
                lambda x: x > 0,
                "No se puede proyectar menos de 1 día en el futuro. Por favor, inténtelo de nuevo."
            )
            
            #Transformar el archivo CSV           
            transform_csv(archivo_csv, output_file, cripto)

            # Procesamiento de datos y predicciones
            Table = load_and_preprocess_data(output_file, projection_days)
            X_Table, y_Table = create_datasets(Table, projection_days)
            pred_Table, score = train_and_predict(X_Table, y_Table, projection_days)
            future_df = create_future_dataframe(Table, pred_Table, projection_days)

            # Visualización y conclusión
            visualize_data(Table, future_df, "Proyección Dolar")
            conclusion(score, pred_Table)
        
        elif option == 4:
            #En caso de finalizar cerrar el programa
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()