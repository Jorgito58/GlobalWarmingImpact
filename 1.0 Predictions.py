import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from Manager import DataAnalytics as da

def Temperature_Prediction():
        
    #Importando Datos
    temperature_df = pd.read_excel("TempFilter.xlsx")

    #Variables a entrenar
    x_train = temperature_df["Año"]
    y_train = temperature_df["Maxima Media"]


    #Creando Modelo
    model = tf.keras.Sequential()
    capa1 = model.add(tf.keras.layers.Dense(units = 1, input_shape = [1]))
    oculto1 = model.add(tf.keras.layers.Dense(units = 10))
    oculto2 = model.add(tf.keras.layers.Dense(units = 10))
    salida = model.add(tf.keras.layers.Dense(1))
    #Mostrando Modelo
    model.summary()

    #Compilado
    model.compile(optimizer = tf.keras.optimizers.Adam(0.9), loss = 'mean_absolute_error')

    #Entrenando el Modelo
    epochs_hist = model.fit(x_train, y_train, epochs = 15)
    model.save("\\Save Models\\Temperature Model")
    plt.plot(epochs_hist.history["loss"])
    plt.title('Progreso de Perdida durante Entrenamiento del Modelo')
    plt.xlabel('Epochs')
    plt.ylabel('Training Loss')
    plt.legend('Training Loss')
    plt.show()

        
    #Predicciones
    Year_list_before = [x for x in range(1900, 2010, 10)]
    Year_list_after = [x for x in range(2000, 2110, 10)]
    
    crop_years = [x for x in range(2030, 2080 , 10)]


    print(temperature_df)

    before = []
    after = []
    crop_temp_pred = []

    # for item in Year_list_before:
    #     Prediction = model.predict([item])
    #     Prediction = float(Prediction[0])
    #     before.append(Prediction)


    # for item in Year_list_after:
    #     Prediction = model.predict([item])
    #     Prediction = float(Prediction[0])
    #     after.append(Prediction)

    

    for item in crop_years:
        Prediction = model.predict([item])
        Prediction = float(Prediction[0])
        crop_temp_pred.append(Prediction)

    

    print(crop_temp_pred)

    #[30.850234985351562, 30.850234985351562, 30.850234985351562, 30.850234985351562, 30.850234985351562]
    


def RainFall_Prediction():
        
    #Importando Datos
    precipitacion_df = pd.read_excel("RainfallMean.xlsx")
    df = da.makePrecipitationDf() 
    print(df)
    #Variables a entrenar
    #x_train = precipitacion_df["Año"]
    x_train = df["Año"]
    y_train = df["Mean"]

   

    #Creando Modelo
    model = tf.keras.Sequential()
    capa1 = model.add(tf.keras.layers.Dense(units = 1, input_shape = [1]))
    oculto1 = model.add(tf.keras.layers.Dense(units = 10))
    oculto2 = model.add(tf.keras.layers.Dense(units = 10))
    salida = model.add(tf.keras.layers.Dense(12))
    #Mostrando Modelo
    model.summary()

    #Compilado
    model.compile(optimizer = tf.keras.optimizers.Adam(2), loss = 'mean_absolute_error')

    #Entrenando el Modelo
    epochs_hist = model.fit(x_train, y_train, epochs = 90)

    #Evaluando Modelo
    epochs_hist.history.keys()

    #Grafico
    plt.plot(epochs_hist.history['loss'])
    plt.title('Progreso de Perdida durante Entrenamiento del Modelo')
    plt.xlabel('Epochs')
    plt.ylabel('Training Loss')
    plt.legend('Training Loss')
    plt.show()
    model.get_weights()

    #Predicciones
    Year = 2025
    Prediction = model.predict([2025])
    import time
    time.sleep(2)
    lista = []

        
    print(lista)
    lista = list(Prediction[0])
    for item in lista:
        print(item)
    print(Prediction[0])

#[106.805626  99.9317   112.46863   93.77981  103.75721  113.06196 94.62138   95.10668  115.456375  91.47464  100.59279  105.46933 ]
# def Clasification():

#     #Importando Datos
#     temperature_df = pd.read_excel("D:\\Software Development\\PythonLearning\\Curso-Python\\21.Proyecto_Cientifico_Calentamiento_Global\\Proyecto\\RainfallMean.xlsx")

#     print(temperature_df)
#     #Variables a entrenar
#     x_train = temperature_df["Año"]
#     y_train = temperature_df["Enero"]


#     model = tf.keras.Sequential()
    
#     model.add(tf.keras.layers.Dense(32, activation = "relu", input_shape = [1]))   
#     model.add(tf.keras.layers.Dense(128, activation = "relu")) 
#     model.add(tf.keras.layers.Dense(32, activation = "relu"))
#     model.add(tf.keras.layers.Dense(1, activation = "softmax"))    
    
#     model.compile(loss = tf.keras.losses.categorical_crossentropy, optimizer = tf.keras.optimizers.Adam(0.001), metrics = ['accuracy'])

#     hist = model.fit(x_train, y_train, epochs = 100)
#     plt.plot(hist)
#     plt.show()

#     prediction = model.predict(2050)
#     print(prediction)
   

#  #Importando Datos
# temperature_df = pd.read_excel("D:\\Software Development\\PythonLearning\\Curso-Python\\21.Proyecto_Cientifico_Calentamiento_Global\\Proyecto\\TempFilter.xlsx")

#     #Variables a entrenar
# x_train = temperature_df["Año"]
# y_train = temperature_df["Maxima Media"]



# model = tf.keras.models.load_model("D:\\Software Development\\PythonLearning\\Curso-Python\\21.Proyecto_Cientifico_Calentamiento_Global\\Proyecto\\Save Models\\Temperature Model")
# model.fit(x_train, y_train, epochs = 2)
# pred = model.predict(2090)
# print(pred)

Temperature_Prediction()



