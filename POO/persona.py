class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    
    def saluda(self,otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'



edwin = Persona('Edwin', 20)
maria = Persona('Marijo', 21)

print(edwin.saluda(maria))