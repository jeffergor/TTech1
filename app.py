from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado al iniciar el servidor Flask
with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Ruta para la página de inicio
@app.route('/')
def index():
    return "¡Bienvenido a mi API!"

# Ruta para realizar predicciones
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['data']
        df = pd.DataFrame(data)
        
        # Convertir las columnas de fechas a datetime
        df['Fecha Inicio'] = pd.to_datetime(df['Fecha Inicio'])
        df['Fecha Fin'] = pd.to_datetime(df['Fecha Fin'])
        
        # Aquí puedes convertir otras columnas si es necesario

        predictions = model.predict(df)
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        print(f"Error: {e}")  # Esto mostrará el error en la consola de Flask
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
