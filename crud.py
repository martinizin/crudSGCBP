import pyodbc;

# Declarar variables de Conexión
name_server = 'UPOAULA10423'  # Nombre del servidor SQL
database = 'SGCBP'  # Nombre de la base de datos
username = 'Administrador'  # Usuario para la conexión
password = 'sgc2024a'  # Contraseña del usuario
controlador_odbc = 'ODBC Driver 17 for SQL Server'  # Controlador ODBC para SQL Server.

# Crear Cadena de Conexion
connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'



# Función para insertar un registro en la tabla Clientes
# Función para insertar un registro en la tabla Clientes
def insertar_cliente(conexion):
    try:
        cursor = conexion.cursor()
        print("\n\tInserción de un nuevo cliente:")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        cedula_ruc = input("Ingrese el número de cédula o RUC: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")
        email = input("Ingrese el correo electrónico: ")
        tipo_cliente = input("Ingrese el tipo de cliente: ")  # Suponiendo que es un campo obligatorio.
        
        query = """
        INSERT INTO BancoDelPacifico.Clientes (nombre_cliente, cedula_ruc, telefono, email, direccion, tipo_cliente)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (nombre_cliente, cedula_ruc, telefono, email, direccion, tipo_cliente))
        conexion.commit()
        print("\nCliente insertado exitosamente.")
    except Exception as e:
        print("\nOcurrió un error al insertar el cliente: ", e)

# Función para consultar registros de la tabla Clientes
def consultar_clientes(conexion):
    try:
        cursor = conexion.cursor()
        print("\n\tConsulta de clientes:\n")
        query = "SELECT * FROM BancoDelPacifico.Clientes"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(f"ID Cliente: {row.id_cliente}, Nombre: {row.nombre_cliente}, Cédula/RUC: {row.cedula_ruc}, Dirección: {row.direccion}, "
                f"Teléfono: {row.telefono}, Correo: {row.email}, Tipo de Cliente: {row.tipo_cliente}")
    except Exception as e:
        print("\nOcurrió un error al consultar los clientes: ", e)


# Función para actualizar un registro en la tabla Clientes
def actualizar_cliente(conexion):
    try:
        cursor = conexion.cursor()
        print("\n\tActualización de un cliente:")
        id_cliente = int(input("Ingrese el ID del cliente a actualizar: "))
        nombre_cliente = input("Ingrese el nuevo nombre: ")
        cedula_ruc = input("Ingrese el nuevo número de cédula o RUC: ")
        direccion = input("Ingrese la nueva dirección: ")
        telefono = input("Ingrese el nuevo teléfono: ")
        email = input("Ingrese el nuevo correo electrónico: ")
        tipo_cliente = input("Ingrese el nuevo tipo de cliente: ")

        query = """
        UPDATE BancoDelPacifico.Clientes
        SET nombre_cliente = ?, cedula_ruc = ?, direccion = ?, telefono = ?, email = ?, tipo_cliente = ?
        WHERE id_cliente = ?
        """
        cursor.execute(query, (nombre_cliente, cedula_ruc, direccion, telefono, email, tipo_cliente, id_cliente))
        conexion.commit()
        print("\nCliente actualizado exitosamente.")
    except Exception as e:
        print("\nOcurrió un error al actualizar el cliente: ", e)

# Función para eliminar un registro de la tabla Clientes
def eliminar_cliente(conexion):
    try:
        cursor = conexion.cursor()
        print("\n\tEliminación de un cliente:")
        id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
        query = "DELETE FROM BancoDelPacifico.Clientes WHERE id_cliente = ?"
        cursor.execute(query, (id_cliente,))
        conexion.commit()

        if cursor.rowcount > 0:
            print("\nCliente eliminado exitosamente.")
        else:
            print("\nNo se encontró un cliente con ese ID.")
    except Exception as e:
        print("\nOcurrió un error al eliminar el cliente: ", e)


# Función para mostrar el menú CRUD
def mostrar_opciones_crud():
    print("\n\t** SISTEMA CRUD - CLIENTES **\n")
    print("\t1. Añadir cliente")
    print("\t2. Consultar clientes")
    print("\t3. Actualizar cliente")
    print("\t4. Eliminar cliente")
    print("\t5. Salir\n")


try:
    conexion = pyodbc.connect(connection_string)
    print("Conexión exitosa.\n")
    while True:
        mostrar_opciones_crud()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            insertar_cliente(conexion)
        elif opcion == '2':
            consultar_clientes(conexion)
        elif opcion == '3':
            actualizar_cliente(conexion)
        elif opcion == '4':
            eliminar_cliente(conexion)
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
except Exception as e:
    print("\nError al conectar con la base de datos: ", e)
finally:
    if 'conexion' in locals() and conexion:
        conexion.close()
        print("Conexión cerrada.")
