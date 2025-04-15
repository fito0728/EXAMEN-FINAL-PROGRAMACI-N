// index.js
const { MongoClient } = require('mongodb');

// URL de conexión (usa tu propia si es Atlas)
const uri = 'mongodb://localhost:27017';

// Nombre de la base de datos
const dbName = 'miBaseDatos';

async function main() {
  const client = new MongoClient(uri);

  try {
    await client.connect();
    console.log('✅ Conectado a MongoDB');

    const db = client.db(dbName);
    const clientes = db.collection('clientes');

    // 1. Insertar documentos
    await clientes.insertMany([
      {
        nombre: "Carlos Pérez",
        ciudad: "Bogotá",
        compras: ["Camisa", "Zapatos", "Pantalón"]
      },
      {
        nombre: "Laura Gómez",
        ciudad: "Medellín",
        compras: ["Bolso", "Perfume"]
      },
      {
        nombre: "Andrés Martínez",
        ciudad: "Cali",
        compras: ["Celular", "Audífonos", "Cargador", "Funda"]
      }
    ]);
    console.log('✅ Documentos insertados');

    // 2. Consulta: clientes con más de 2 compras
    const resultado = await clientes.find({
      "compras.2": { $exists: true }
    }).toArray();

    console.log('📋 Clientes con más de 2 compras:');
    console.log(resultado);

  } catch (error) {
    console.error('❌ Error:', error);
  } finally {
    await client.close();
    console.log('🔒 Conexión cerrada');
  }
}

main();
