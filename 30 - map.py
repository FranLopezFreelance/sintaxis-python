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
    Empleado("Juan", "Evaluador", 60000),
]

def calculo_comision(empleado):
    if empleado.salario > 120000:
        empleado.salario=empleado.salario*1.03
    else:
        empleado.salario=empleado.salario*1.06
        
    return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)

