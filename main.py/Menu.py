from Biblioteca import Biblioteca
from Libro import Libro
from Buscador import Buscador
from Enlistar import Listados
from Alquiler import Alquiler

class Menu:
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.librosParaAlquilar = Biblioteca()
        self.librosAlquilados = Biblioteca()
        self.mostrarMenu()
        self.cantidadDeLibrosAlquilados = 0 #LE ASIGNARÉ EL VALOR QUE SE DEVUELVA EN LA TUPLA QUE RETORNA alquiler

    def mostrarMenu(self):
        print("\n====================================================")
        print("BIENVENIDO AL MENÚ DE LA BIBLIOTECA")
        print("====================================================\n")
        if self.biblioteca.length == 0:
            self.mostrarOpcionesBibliotecaVacia()
        elif self.biblioteca.length > 0:
            self.mostrarOpcionesBibliotecaIniciada()
        self.mostrarMenu()

    def mostrarOpcionesBibliotecaVacia(self):    
        print("1. Agregar un libro.")
        seleccionarOpcion: int = int(input("Ingresa tu opción: "))
    
        if seleccionarOpcion == 1:
            self.opcionSeleccionada1()
        else:
            print("\nIngresa una opción válida.\n")
            self.mostrarOpcionesBibliotecaVacia()
    
    def mostrarOpcionesBibliotecaIniciada(self):
        print("1. Agregar un libro.")
        print("2. Eliminar un libro.")
        print("3. Buscar un libro por su género.")
        print("4. Buscar un libro por su título.")
        print("5. Buscar un libro por su autor.")
        print("6. Buscar un libro por su año de publicación.")
        print("7. Mirar libros disponibles para alquilar.")
        print("8. Mirar libros alquilados.")
        print("9. Mirar libros disponibles para alquilar por género.")
        print("10. Mirar libros alquilados por género.")
        print("11. Alquilar libro por su género.")
        print("12. Alquilar libro.")
        print("13. Devolver libro.")
        seleccionarOpcion: int = int(input("\nIngresa tu opción: "))

        if seleccionarOpcion == 1:
            self.opcionSeleccionada1()
        elif seleccionarOpcion == 2:
            self.opcionSeleccionada2()
        elif seleccionarOpcion == 3:
            self.opcionSeleccionada3()
        elif seleccionarOpcion == 4:
            self.opcionSeleccionada4()
        elif seleccionarOpcion == 5:
            self.opcionSeleccionada5()
        elif seleccionarOpcion == 6:
            self.opcionSeleccionada6()
        elif seleccionarOpcion == 7:
            self.opcionSeleccionada7()
        elif seleccionarOpcion == 8:
            self.opcionSeleccionada8()
        elif seleccionarOpcion == 9:
            self.opcionSeleccionada9()
        elif seleccionarOpcion == 10:
            self.opcionSeleccionada10()
        elif seleccionarOpcion == 11:
            self.opcionSeleccionada11()
        elif seleccionarOpcion == 12:
            self.opcionSeleccionada12()
        elif seleccionarOpcion == 13:
            self.opcionSeleccionada13()
        else:
            print("\nIngresa una opción válida\n")
            self.mostrarOpcionesBibliotecaIniciada()

    def opcionSeleccionada1(self):
        print("\n================= Ingresemos el libro =================")
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
                    print("Ingrese un número diferente para el libro.")
                    self.opcionSeleccionada1()
                    break
                elif elementoBiblioteca.value.numeroLibro != numeroLibro and self.biblioteca.length > iteracionesBiblioteca:
                    pass
                elif elementoBiblioteca.value.numeroLibro != numeroLibro and self.biblioteca.length == iteracionesBiblioteca:
                    libro = Libro(numeroLibro, genero, autor, titulo, añoPublicacion, tarifaAlquiler)
                    self.librosParaAlquilar.append(libro)
                    print(self.biblioteca.append(libro))
                    break

    def opcionSeleccionada2(self):
        print("\n================= Eliminemos el libro =================")
        numeroLibro: str = input("Ingresa el número del libro que quieres eliminar: ")
        
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
    
    def opcionSeleccionada3(self):
        print("\n================= Busquemos el libro =================")
        generoLibro: str = input("Ingesa el género del libro: ")

        buscadorDeLibros = Buscador(self.biblioteca, self.librosParaAlquilar)
        buscadorDeLibros.buscarLibroPorGenero(generoLibro)

    def opcionSeleccionada4(self):
        print("\n================= Busquemos el libro =================")
        tituloLibro: str = input("Ingesa el título del libro: ")

        buscadorDeLibros = Buscador(self.biblioteca, self.librosParaAlquilar)
        buscadorDeLibros.buscarLibroPorTitulo(tituloLibro)

    def opcionSeleccionada5(self):
        print("\n================= Busquemos el libro =================")
        autorLibro: str = input("Ingesa el autor del libro: ")

        buscadorDeLibros = Buscador(self.biblioteca, self.librosParaAlquilar)
        buscadorDeLibros.buscarLibroPorAutor(autorLibro)

    def opcionSeleccionada6(self):
        print("\n================= Busquemos el libro =================")
        añoPublicacion: int = int(input("Ingesa el año de publicación del libro: "))

        buscadorDeLibros = Buscador(self.biblioteca, self.librosParaAlquilar)
        buscadorDeLibros.buscarLibroPorAñoPublicacion(añoPublicacion)

    def opcionSeleccionada7(self):
        print("\n================= Libros disponibles para alquilar =================")
        listados = Listados(self.librosParaAlquilar, self.librosAlquilados)
        listados.enlistarLibrosDisponiblesParaAlquilar()

    def opcionSeleccionada8(self):
        print("\n================= Libros alquilados =================")
        listados = Listados(self.librosParaAlquilar, self.librosAlquilados)
        listados.enlistarLibrosAlquilados()

    def opcionSeleccionada9(self):
        print("\n================= Libros disponibles para alquilar por género =================")
        listados = Listados(self.librosParaAlquilar, self.librosAlquilados)
        listados.enlistarLibrosDisponiblesPorGeneroParaAlquilar()

    def opcionSeleccionada10(self):
        print("\n================= Libros alquilados por género =================")
        listados = Listados(self.librosParaAlquilar, self.librosAlquilados)
        listados.enlistarLibrosAlquiladosPorGenero()

    def opcionSeleccionada11(self):
        print("\n================= Alquilemos un libro por su género =================")
        generoLibro: str = input("Ingesa el género del libro: ")

        if self.librosParaAlquilar.length > 0:
            alquiler = Alquiler(self.librosParaAlquilar, self.librosAlquilados)
            alquiler.alquilarLibroPorGenero(generoLibro)

        else:
            print("No hay libros para alquilar")


    def opcionSeleccionada12(self):
        pass

    def opcionSeleccionada13(self):
        pass

menu = Menu()
menu