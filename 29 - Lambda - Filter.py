class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
    Empleado("Juan", "Director", 180000),
    Empleado("José", "Gerente", 140000),
    Empleado("Luis", "Supervisor", 100000),
    Empleado("Roberto", "Evaluador", 60000),
]

salarios_altos=filter(lambda empleado:empleado.salario>100000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)