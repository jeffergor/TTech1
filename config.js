const mongoose = require('mongoose');
const Web3 = require('web3');

// Conexión a MongoDB
mongoose.connect('mongodb://localhost/gestion_permisos', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Conectado a MongoDB'))
    .catch(err => console.error('No se pudo conectar a MongoDB', err));

// Conexión a la blockchain de Ganache
const web3 = new Web3('http://localhost:7545'); // Aquí eliminamos el uso de HttpProvider

module.exports = mongoose;
module.exports.web3 = web3;
