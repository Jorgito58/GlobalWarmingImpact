# from os import stat
# import tensorflow as tf
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt


# class Prediction(object):


#     def __init__(self) -> None:
            
#         #Importando Datos
#         self.temperature_df = pd.read_excel("D:\\Software Development\\PythonLearning\\Curso-Python\\21.Proyecto_Cientifico_Calentamiento_Global\\Proyecto\\TempFilter.xlsx")
#         #Datos de Entrenamiento
#         self.x_train = self.temperature_df["Año"]
#         self.y_train = self.temperature_df["Maxima Media"]
#         #Creando Modelos 
#         self.model = self.Create_Model()

    
#     def Create_Model(self):
#         #Creando Modelo
#         model = tf.keras.Sequential()
#         model.add(tf.keras.layers.Dense(units = 10, input_shape = [1]))
#         #Compilado
#         model.compile(optimizer = tf.keras.optimizers.Adam(0.012), loss = 'mean_absolute_error')
#         history = model.fit(self.x_train, self.y_train, epochs = 30)
#         return history

#     def Show_Model(self):
#         #Mostrando Modelo
#         self.model.summary()

#     def Compile_and_Train(self):
#         pass
    

#     # def Model_Graphic():
#     #     #Grafico
#     #     plt.plot(epochs_hist.history['loss'])
#     #     plt.title('Progreso de Perdida durante Entrenamiento del Modelo')
#     #     plt.xlabel('Epochs')
#     #     plt.ylabel('Training Loss')
#     #     plt.legend('Training Loss')
#     #     plt.show()
    
#     def Predict(self):
#         #Predicciones
#         Year = 2020
#         Prediction = self.model.predict([Year])
#         import time
#         time.sleep(0.5)
#         lista = []
#         lista = list(Prediction[0])
#         print(Prediction[0])

#         return lista

# p = Prediction()
# p.Create_Model()
# p.Show_Model()
p.Predict()
