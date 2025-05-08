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

## ⚠️ Recomendaciones para un mejor reconocimiento

- Usa trazos **gruesos y definidos**.
- Intenta **centrar el número** en la pizarra.
- Evita escribir números muy pequeños o con líneas cortadas.

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


