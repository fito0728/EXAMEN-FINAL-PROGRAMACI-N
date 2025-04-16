from pymongo import MongoClient

# 1. Conectar a la base de datos
uri = 'mongodb://localhost:27017'
db_name = 'miBaseDatos'

def main():
    client = MongoClient(uri)

    try:
        print('✅ Conectando a MongoDB...')
        db = client[db_name]
        clientes = db['clientes']

        # 2. Insertar documentos
        clientes.insert_many([
            {
                "nombre": "Carlos Pérez",
                "ciudad": "Bogotá",
                "compras": ["Camisa", "Zapatos", "Pantalón"]
            },
            {
                "nombre": "Laura Gómez",
                "ciudad": "Medellín",
                "compras": ["Bolso", "Perfume"]
            },
            {
                "nombre": "Andrés Martínez",
                "ciudad": "Cali",
                "compras": ["Celular", "Audífonos", "Cargador", "Funda"]
            },
            {
                "nombre": "fito gonzalez",
                "ciudad": "barranquilla",
                "compras": ["moto", "casco", "calecho", "guantes"]
            
            },
            {
                "nombre": "luciano gonzalez franco",
                "ciudad": "barranquilla",
                "compras": ["carro de juguete", "balom", "mono patin", "bicicleta"]
            }
        ])
        print('✅ Documentos insertados')

        # 3. Buscar clientes con más de 2 compras
        resultado = clientes.find({
            "compras.2": {"$exists": True}
        })

        print('📋 Clientes con más de 2 compras:')
        for cliente in resultado:
            print(cliente)

    except Exception as e:
        print('❌ Error:', e)

    finally:
        client.close()
        print('🔒 Conexión cerrada')

if __name__ == '__main__':
    main()
