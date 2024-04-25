from Biblioteca import Biblioteca
from Libro import Libro

class FuncionalidadesBiblioteca:

    def __init__(self, librosParaAlquiler: Biblioteca, biblioteca: Biblioteca):
        self.librosParaAlquilar = librosParaAlquiler
        self.biblioteca = biblioteca

    def agregarLibro(self):
        numeroLibro: str = input("Ingresa el número del libro: ")
        genero: str = input("Ingresa el género del libro: ")
        autor: str = input("Ingresa el autor del libro: ")
        titulo: str = input("Ingresa el título del libro: ")
        añoPublicacion: int = int(input("Ingresa el año de publicación del libro: "))
        tarifaAlquiler: int = int(input("Ingresa la tarifa del alquiler del libro: "))
        
        if self.biblioteca.head == None:
            libro = Libro(numeroLibro, genero, autor, titulo, añoPublicacion, tarifaAlquiler)
            self.librosParaAlquilar.append(libro)
            print(self.biblioteca.append(libro))
        elif self.biblioteca.head != None:
            iteracionesBiblioteca = 0
            for elementoBiblioteca in self.biblioteca:
                iteracionesBiblioteca += 1
                if  elementoBiblioteca.value.numeroLibro == numeroLibro:
                    print("\nEl número del libro ya existe en la biblioteca.")
                    print("\nIngrese un número diferente para el libro.\n")
                    self.agregarLibro()
                    break
                elif elementoBiblioteca.value.numeroLibro != numeroLibro and self.biblioteca.length > iteracionesBiblioteca:
                    pass
                elif elementoBiblioteca.value.numeroLibro != numeroLibro and self.biblioteca.length == iteracionesBiblioteca:
                    libro = Libro(numeroLibro, genero, autor, titulo, añoPublicacion, tarifaAlquiler)
                    self.librosParaAlquilar.append(libro)
                    print(self.biblioteca.append(libro))
                    break
                
                
    def eliminarLibro(self, numeroLibro):
        iteracionesBiblioteca = 0
        for elementoBiblioteca in self.biblioteca:

            iteracionesBiblioteca += 1
            if elementoBiblioteca.value.numeroLibro == numeroLibro:

                if self.librosParaAlquilar.length > 0:

                    iteracionesParaAlquilar = 0
                    for elementoParaAlquilar in self.librosParaAlquilar:

                        iteracionesParaAlquilar += 1
                        if elementoParaAlquilar.value.numeroLibro == numeroLibro:
                            print(self.biblioteca.remove(iteracionesBiblioteca - 1))
                            self.librosParaAlquilar.remove(iteracionesParaAlquilar - 1)
                            break #PUEDE QUE ACÁ NO SE ME ELMINE EL OTRO LIBRO POR GÉNERO

                        elif elementoParaAlquilar.value.numeroLibro != numeroLibro and self.librosParaAlquilar.length > iteracionesParaAlquilar:
                            pass

                        elif  elementoParaAlquilar.value.numeroLibro != numeroLibro and self.librosParaAlquilar.length == iteracionesParaAlquilar:
                            print(f"\nEl libro con número {numeroLibro} se encuentra alquilado, debe devolverse para poderse eliminar.")

                else:
                    print(f"\nEl libro con número {numeroLibro} se encuentra alquilado, debe devolverse para poderse eliminar.")
                break 

            elif elementoBiblioteca.value.numeroLibro != numeroLibro and self.biblioteca.length > iteracionesBiblioteca:
                pass

            elif elementoBiblioteca.value.numeroLibro != numeroLibro and self.biblioteca.length == iteracionesBiblioteca:
                print("\nEse libro no existe en la biblioteca.\n")
                break