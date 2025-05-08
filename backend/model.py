import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
import joblib
import matplotlib.pyplot as plt
import pandas as pd

#descargar dataset
mnist = fetch_openml('mnist_784', version=1)

# Dividir dataset en atributos y etiquetas
x = mnist['data']
y = mnist['target'].astype(np.uint8)

#reemplazar topdos los pixeles grises por negros si el pixel > 1 entonces poner en 255
x_all_black = x.replace([range(1,255)], 255)

#declarar el randomforest para entrenar el modelo
rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1) #obliga a trabajar todos los nucleos del pc para entrenarlo
rnd_clf.fit(x_all_black.values, y)

#guardar el modelo en .plk para usarlo en otras partes
joblib.dump(rnd_clf, 'rnd_clf_model.pkl')
print('Entrenamiento terminado')
