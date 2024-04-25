from Biblioteca import Biblioteca

class Alquiler:
    
    def __init__(self, librosParaAlquilar: Biblioteca, librosAlquilados: Biblioteca):
        self.librosParaAlquilar = librosParaAlquilar
        self.librosAlquilados = librosAlquilados
        

    def alquilarLibroPorGenero(self, generoLibro: str):
        
        cantidadUnidadesDisponiblesPorGenero = 0
        for elemento in self.librosParaAlquilar:

            if elemento.value.genero == generoLibro:
                cantidadUnidadesDisponiblesPorGenero += 1

                print("\n===================== Libro =====================\n")  
                print(f"Número del libro: {elemento.value.numeroLibro}")
                print(f"Género del libro: {elemento.value.genero}")
                print(f"Autor del libro: {elemento.value.autor}")
                print(f"Título del libro: {elemento.value.titulo}")
                print(f"Año de publicación del libro: {elemento.value.añoPublicacion}")
                print(f"Tarifa de alquiler del libro: {elemento.value.tarifaAlquiler}")

            else:
                pass

        print(f"\nPara el género {generoLibro}, {cantidadUnidadesDisponiblesPorGenero} unidad(es) está(n) disponible(s) para alquilar.")

        if cantidadUnidadesDisponiblesPorGenero > 0:
            cantidadDelibrosParaLlevar = self.saberCantidadDeLibrosParaLlevar(cantidadUnidadesDisponiblesPorGenero, generoLibro)
        
            if cantidadDelibrosParaLlevar == 0:
                print("===============================================================")
                print(f"\nNo alquilaste ningún libro para el género {generoLibro}.\n")
                print("===============================================================")

            elif cantidadDelibrosParaLlevar > cantidadUnidadesDisponiblesPorGenero:
                print("La cantidad ingresada no debe superar la cantidad de libros que hay.")
                self.alquilarLibroPorGenero(generoLibro)

            else:
                for numero in range(cantidadDelibrosParaLlevar):
                    print("=========================================")
                    print(f"\nAlquilar libro {numero + 1}.\n")
                    print("=========================================")
                    self.alquilarLibroDisponible(generoLibro)
        
        else:
            print("\nNo puedes alquilar un libro por ese género en este momento.")


    def alquilarLibro(self, numeroLibro: str):

        iteracionesLibrosParaAlquilar = 0
        for elemento in self.librosParaAlquilar:

            iteracionesLibrosParaAlquilar += 1
            if elemento.value.numeroLibro == numeroLibro:
                libroObtenidoDeDisponiblesParaALquilar = self.librosParaAlquilar.get(iteracionesLibrosParaAlquilar - 1).value
                self.librosAlquilados.append(libroObtenidoDeDisponiblesParaALquilar)
                self.librosParaAlquilar.remove(iteracionesLibrosParaAlquilar - 1)

                print("\n===================== Libro alquilado =====================\n")  
                print(f"Número del libro: {elemento.value.numeroLibro}")
                print(f"Género del libro: {elemento.value.genero}")
                print(f"Autor del libro: {elemento.value.autor}")
                print(f"Título del libro: {elemento.value.titulo}")
                print(f"Año de publicación del libro: {elemento.value.añoPublicacion}")
                print(f"Tarifa de alquiler del libro: {elemento.value.tarifaAlquiler}")

            elif elemento.value.numeroLibro != numeroLibro and self.librosParaAlquilar.length > iteracionesLibrosParaAlquilar:
                pass

            elif elemento.value.numeroLibro != numeroLibro and self.librosParaAlquilar.length == iteracionesLibrosParaAlquilar:
                print(f"\nEl libro con número de libro {numeroLibro} no está disponible para alquilar.")
                print("\nIngresa el número de un libro disponible.\n")
                break 



    def saberCantidadDeLibrosParaLlevar(self, cantidadUnidadesDisponiblesPorGenero, generoLibro) -> int:
        cantidadDeLibrosParaLlevar = int(input(f"\nIngresa la cantidad de libros que deseas llevar con el género {generoLibro}: "))

        if cantidadDeLibrosParaLlevar > cantidadUnidadesDisponiblesPorGenero:
            print("\nDebes ingresar una cantidad existente.")
            cantidadDeLibrosParaLlevar = self.saberCantidadDeLibrosParaLlevar(cantidadUnidadesDisponiblesPorGenero, generoLibro)

        elif cantidadDeLibrosParaLlevar < 0:
            print("\nDebes ingresar una cantidad mayor a 0.")
            cantidadDeLibrosParaLlevar = self.saberCantidadDeLibrosParaLlevar(cantidadUnidadesDisponiblesPorGenero, generoLibro)

        elif cantidadDeLibrosParaLlevar == 0:
            print("\nNo alquilarás ningún libro.")

        else:
            None

        return cantidadDeLibrosParaLlevar
    

    def alquilarLibroDisponible(self, generoLibro):
        numeroLibroParaAlquilar = input(f"Ingresa el número del libro que es de género {generoLibro}: ")
        
        iteraciones = 0
        for elemento in self.librosParaAlquilar:

            iteraciones += 1
            if elemento.value.numeroLibro == numeroLibroParaAlquilar and elemento.value.genero == generoLibro:
                libroObtenidoDeDisponiblesParaALquilar = self.librosParaAlquilar.get(iteraciones - 1).value
                self.librosAlquilados.append(libroObtenidoDeDisponiblesParaALquilar)
                self.librosParaAlquilar.remove(iteraciones - 1)
                
                print("=========================================")
                print("\nLibro alquilado.\n")
                print("=========================================")
                break

            elif (elemento.value.numeroLibro != numeroLibroParaAlquilar or elemento.value.genero != generoLibro) and self.librosParaAlquilar.length > iteraciones:
                pass

            elif (elemento.value.numeroLibro != numeroLibroParaAlquilar or elemento.value.genero != generoLibro) and self.librosParaAlquilar.length == iteraciones:
                print(f"\nEl número del libro que ingresaste no conincide con el del libro de género {generoLibro}.")
                print("\nIngresa el número correcto.\n")
                self.alquilarLibroDisponible(generoLibro)
                break 