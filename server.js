// server.js

const express = require('express');
const app = express();
const mongoose = require('./config');  // Importamos la configuración de MongoDB
const permisoRoutes = require('./routes/permisos'); // Importamos las rutas de permisos
const axios = require('axios'); // Librería para hacer peticiones HTTP

const PORT = process.env.PORT || 3000;

// Middleware para parsear JSON
app.use(express.json());

// Rutas para los permisos
app.use('/api/permisos', permisoRoutes);

// Nueva ruta para analizar datos usando IA (servidor Flask)
app.post('/analyze', async (req, res) => {
    const inputData = req.body.data;  // Datos enviados por el cliente
    try {
        // Hacer la petición al servidor Flask para obtener predicciones de IA
        const response = await axios.post('http://localhost:5000/predict', {
            data: inputData
        });
        // Devolver la predicción al cliente
        res.json(response.data);
    } catch (error) {
        console.error('Error llamando al servidor de IA', error);
        res.status(500).send('Error procesando los datos de IA');
    }
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
