import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

def load_data():
    # Cargar el dataset
    data = pd.read_csv('data.csv')
    
    # Convertir las columnas de fechas en formato datetime
    data['Fecha Inicio'] = pd.to_datetime(data['Fecha Inicio'], format='%Y-%m-%d')
    data['Fecha Fin'] = pd.to_datetime(data['Fecha Fin'], format='%Y-%m-%d')
    
    # Calcular la diferencia en días entre Fecha Inicio y Fecha Fin
    data['Dias Duracion'] = (data['Fecha Fin'] - data['Fecha Inicio']).dt.days
    
    # Codificar las columnas de texto en valores numéricos
    le_trabajador = LabelEncoder()
    le_supervisor = LabelEncoder()
    le_estado = LabelEncoder()
    le_motivo = LabelEncoder()
    
    data['Nombre Trabajador'] = le_trabajador.fit_transform(data['Nombre Trabajador'])
    data['Supervisor'] = le_supervisor.fit_transform(data['Supervisor'])
    data['Estado'] = le_estado.fit_transform(data['Estado'])  # Columna objetivo
    data['Motivo'] = le_motivo.fit_transform(data['Motivo'])
    
    # Separar características (features) y la columna objetivo (label)
    X = data[['Nombre Trabajador', 'Dias Duracion', 'Supervisor', 'Motivo']]  # Características
    y = data['Estado']  # Lo que queremos predecir (columna objetivo)
    
    return X, y

def train_model():
    X, y = load_data()
    
    # Separar los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Crear y entrenar el modelo de RandomForest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Guardar el modelo entrenado en un archivo .pkl
    with open('trained_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Modelo entrenado y guardado como 'trained_model.pkl'")

# Entrenar el modelo
train_model()
