# 🧠 Proyecto de Reconocimiento de Dígitos con Machine Learning

Este proyecto permite reconocer números escritos a mano en una pizarra digital. Al dibujar un número del 0 al 9, un algoritmo de Machine Learning entrenado con un modelo de **Random Forest** intentará identificarlo correctamente.

---

## 🎨 ¿Cómo funciona?

1. El usuario **dibuja un número** (del 0 al 9) en una cuadrícula de píxeles tipo pizarra.
2. Al hacer clic en **"ENVIAR"**, la imagen dibujada se convierte en una matriz de datos.
3. Esta matriz se transforma y se pasa a un **modelo de Random Forest**, previamente entrenado.
4. El modelo predice el número más probable basado en lo que aprendió durante el entrenamiento.
5. La predicción se muestra en pantalla.

---

## 📊 Modelo entrenado

- **Algoritmo**: Random Forest Classifier
- **Cantidad de imágenes de entrenamiento**: 70,000
- **Fuente de datos**: Dataset de imágenes de dígitos manuscritos (probablemente MNIST)
- **Precisión esperada**: Moderada. Dado el tamaño limitado del dataset, se recomienda dibujar los números de forma **clara y gruesa** para mejorar la precisión del modelo.

---

## ⚠️ Recomendaciones para un mejor reconocimiento

- Usa trazos **gruesos y definidos**.
- Intenta **centrar el número** en la pizarra.
- Evita escribir números muy pequeños o con líneas cortadas.

---

## 🧰 Tecnologías utilizadas

- Python 🐍
- Scikit-learn
- HTML, CSS y JavaScript para la interfaz
- Librerías de visualización y preprocesamiento de imágenes

---

## 🚀 Posibles mejoras futuras

- Entrenar con un dataset más grande y diverso
- Implementar redes neuronales convolucionales (CNN) para mayor precisión
- Aumentar la tolerancia a estilos de escritura diversos
- Permitir borrar y redibujar fácilmente

---

## 📷 Ejemplo

![image](https://github.com/user-attachments/assets/05516799-3648-4a9e-9309-3f57a1d80abd)

---

## 📩 Contribuciones

¿Te gustaría mejorar el modelo o la interfaz? ¡Eres bienvenido a colaborar! Abre un issue o envía un pull request con tus sugerencias.

---

## Licencia

Este proyecto es de uso libre para fines educativos y experimentales. ¡Diviértete aprendiendo!
