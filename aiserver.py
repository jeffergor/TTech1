# ai_server.py
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Ejemplo: un modelo de IA simple (puedes usar un modelo entrenado)
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1, activation='linear')
])

# Ruta para hacer predicciones
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']  # Obtener los datos de la petición
    input_data = np.array(data).reshape(1, -1)  # Ajustar el input
    prediction = model.predict(input_data)[0]  # Realizar la predicción
    return jsonify({'prediction': float(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
