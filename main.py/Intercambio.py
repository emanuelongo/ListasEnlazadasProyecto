from Biblioteca import Biblioteca
from Libro import Libro

class Intercambio:

    def __init__(self, librosParaAlquilar: Biblioteca, librosAlquilados: Biblioteca, biblioteca: Biblioteca):
        self.librosParaAlquilar = librosParaAlquilar
        self.librosAlquilados = librosAlquilados
        self.biblioteca = biblioteca
    
    def saberLibroDeteriorado(self, numeroLibro: str):
        
        if self.librosAlquilados.head != None:
            
            iteracionesParaAlquilados = 0
            for elemento in self.librosAlquilados:
                
                iteracionesParaAlquilados += 1
                if elemento.value.numeroLibro == numeroLibro:
                    print(f"\nEl libro con número de libro {numeroLibro} está alquilado.")
                    print(f"\nSe debe devolver el libro para poder intercambiarlo.")
                    break

                elif elemento.value.numeroLibro != numeroLibro and self.librosAlquilados.length > iteracionesParaAlquilados:
                    pass
                
                elif elemento.value.numeroLibro != numeroLibro and self.librosAlquilados.length == iteracionesParaAlquilados:
                    self.intercambioDeLibroDeteriorado(numeroLibro)

        elif self.librosAlquilados.head == None:
            
            iteracionesParaAlquilar = 0
            for elemento in self.librosParaAlquilar:
                
                iteracionesParaAlquilar += 1
                if elemento.value.numeroLibro == numeroLibro:
                    self.intercambioDeLibroDeteriorado(numeroLibro)
                    break

                elif elemento.value.numeroLibro != numeroLibro and self.librosAlquilados.length > iteracionesParaAlquilar:
                    pass
                
                elif elemento.value.numeroLibro != numeroLibro and self.librosAlquilados.length == iteracionesParaAlquilar:
                    print(f"\nEl libro con número de libro {numeroLibro} no existe en la biblioteca")


    def intercambioDeLibroDeteriorado(self, numeroLibro):
        
        iteracionesBiblioteca = 0
        for elemento in self.biblioteca:

            iteracionesBiblioteca += 1
            if elemento.value.numeroLibro == numeroLibro:
                libro = Libro(elemento.value.numeroLibro, elemento.value.genero, elemento.value.autor, elemento.value.titulo, elemento.value.añoPublicacion, elemento.value.tarifaAlquiler)
                self.biblioteca.remove(iteracionesBiblioteca - 1)
                self.biblioteca.insert(libro, iteracionesBiblioteca - 1)
                print("\nLibro intercambiado.")
                break

            elif elemento.value.numeroLibro != numeroLibro and self.biblioteca.length > iteracionesBiblioteca:
                pass

            elif elemento.value.numeroLibro != numeroLibro and self.biblioteca.length == iteracionesBiblioteca:
                print(f"\nEl libro con número de libro {numeroLibro} no existe en la biblioteca.")