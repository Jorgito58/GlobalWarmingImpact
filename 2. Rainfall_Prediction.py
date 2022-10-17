import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



x_train = [x for x in range(2006, 2023, 1)]
y_train = [100, 200, 10, 36, 26, 34, 98, 65, 76, 100, 87, 98, 87, 98, 103, 110, 140 ]
print(len(x_train), len(y_train))

#Visualizacion
sns.scatterplot(x = x_train ,y = y_train)

#Creando Modelo
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units = 1, input_shape = [1]))

#Mostrando Modelo
model.summary()

#Compilado
model.compile(optimizer = tf.keras.optimizers.Adam(1), loss = 'mean_squared_error')

#Entrenando el Modelo
epochs_hist = model.fit(x_train, y_train, epochs = 30)

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
Prediction = model.predict([Year])
import time
time.sleep(2)
lista = []

    
print(lista)
lista = list(Prediction[0])
for item in lista:
    print(item)
print(Prediction[0])


