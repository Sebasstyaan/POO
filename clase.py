class Aprendiz:
    def __init__(self,identificacion,nombre,edad,correo,telefono):
        self.identificacion=identificacion
        self.nombre=nombre
        self.edad=edad
        self.correo=correo
        self.telefono=telefono
        
    def calcularEdad(self):
        if self.edad>=18:
            print('\nEl aprendiz es mayor de edad')
        elif self.edad<18:
            print('\nEl aprendiz es menor de edad ')
            
Aprendiz1=Aprendiz(111,'Brandon',27,'brandon@misena.edu.co',3202299978)
Aprendiz2=Aprendiz(222,'Sebastian',16,'scvargas40@misena.edu.co',3173305304)
print()
print(f'Identificacion del Aprendiz1:{Aprendiz1.identificacion}\nNombre: {Aprendiz1.nombre}\nEdad: {Aprendiz1.edad}\nCorreo: {Aprendiz1.correo}\nTelefono: {Aprendiz1.telefono}')
Aprendiz1.calcularEdad()
print()
print(f'Identificacion del Aprendiz2:{Aprendiz2.identificacion}\nNombre: {Aprendiz2.nombre}\nEdad: {Aprendiz2.edad}\nCorreo: {Aprendiz2.correo}\nTelefono: {Aprendiz2.telefono}')
