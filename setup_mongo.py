from pymongo import MongoClient

def inicializar_base_datos():
    # Conectar a MongoDB (local o en servidor remoto)
    client = MongoClient('mongodb://localhost:27017/')  # Si tu Mongo está en un servidor remoto, pon su URL
    db = client['empresa_audiovisual']  # Base de datos que vas a usar o crear

    # Crear colecciones (si no existen)
    clientes = db['clientes']
    proyectos = db['proyectos']
    empleados = db['empleados']
    contratos = db['contratos']

    # Datos de ejemplo
    cliente = {"nombre": "Cliente X", "contacto": "contacto@cliente.com"}
    cliente_id = clientes.insert_one(cliente).inserted_id

    proyecto = {"nombre": "Proyecto A", "cliente_id": cliente_id, "estado": "En progreso"}
    proyectos.insert_one(proyecto)

    print("Base de datos inicializada con colecciones y datos de ejemplo.")

if __name__ == '__main__':
    inicializar_base_datos()
    