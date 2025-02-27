import mysql.connector

class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Cargo:
    def __init__(self, id, nombre, bono):
        self.id = id
        self.nombre = nombre
        self.bono = bono

class Empleado(Persona):
    def __init__(self, id, nombre, cargo, salario, fecha_ingreso):
        super().__init__(id, nombre)
        self.cargo = cargo
        self.salario = salario
        self.fecha_ingreso = fecha_ingreso
        self.subordinados = []
    
    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

def conectar_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="DOOLABS"
    )

def obtener_empleados():
    conn = conectar_db()
    cursor = conn.cursor()
    query = """
    SELECT e.id, p.name, c.id, c.name, c.bonus, e.salary, e.hire_date 
    FROM employees e
    JOIN persons p ON e.person_id = p.id
    JOIN positions c ON e.position_id = c.id
    """
    cursor.execute(query)
    empleados = {}
    for (emp_id, nombre, cargo_id, cargo_nombre, bono, salario, fecha_ingreso) in cursor.fetchall():
        cargo = Cargo(cargo_id, cargo_nombre, bono)
        empleados[emp_id] = Empleado(emp_id, nombre, cargo, salario, fecha_ingreso)
    
    query = "SELECT supervisor_id, employee_id FROM employee_supervision"
    cursor.execute(query)
    for supervisor_id, empleado_id in cursor.fetchall():
        if supervisor_id in empleados and empleado_id in empleados:
            empleados[supervisor_id].agregar_subordinado(empleados[empleado_id])
    
    cursor.close()
    conn.close()
    return empleados

def calcular_salario_neto(empleado):
    return {sub.nombre: sub.salario + sub.cargo.bono for sub in empleado.subordinados}

if __name__ == "__main__":
    empleados = obtener_empleados()

    
    for emp in empleados.values():
        if emp.subordinados:
            print(f"Salarios netos de los empleados a cargo de {emp.nombre}:")
            print(calcular_salario_neto(emp))
    
