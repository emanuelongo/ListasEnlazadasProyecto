from Biblioteca import Biblioteca

class Buscador:
    
    def __init__(self, listaBiblioteca: Biblioteca, listaDisponibles: Biblioteca):
        self.biblioteca = listaBiblioteca
        self.librosParaAlquilar = listaDisponibles

    def buscarLibroPorGenero(self, generoLibro: str):
        
        iteraciones = 0
        cantidadUnidadesEnBiblioteca = 0
        cantidadUnidadesDisponiblesPorGenero = 0
        for elemento in self.biblioteca:

            iteraciones += 1
            if elemento.value.genero == generoLibro:
                cantidadUnidadesEnBiblioteca += 1

                if self.librosParaAlquilar.length > 0:

                    for elementoParaAlquilar in self.librosParaAlquilar:

                        if elementoParaAlquilar.value.genero == generoLibro:
                            cantidadUnidadesDisponiblesPorGenero += 1

                        else:
                            pass

                else:
                        cantidadUnidadesDisponiblesPorGenero += 0
                print("\n===================== Libro =====================\n")  
                print(f"Número del libro: {elemento.value.numeroLibro}")
                print(f"Género del libro: {elemento.value.genero}")
                print(f"Autor del libro: {elemento.value.autor}")
                print(f"Título del libro: {elemento.value.titulo}")
                print(f"Año de publicación del libro: {elemento.value.añoPublicacion}")
                print(f"Tarifa de alquiler del libro: {elemento.value.tarifaAlquiler}")
            
            else:
                pass
            
        print(f"\nPara el género {generoLibro}, {cantidadUnidadesEnBiblioteca} unidad(es) hace(n) parte de la biblioteca  y {cantidadUnidadesDisponiblesPorGenero} unidad(es) está(n) disponible(s) para alquilar.")

    def buscarLibroPorTitulo(self, tituloLibro: str):
        
        iteraciones = 0
        for elemento in self.biblioteca:

            iteraciones += 1
            if elemento.value.titulo == tituloLibro:
                print(f"\nEl libro que tiene por título '{tituloLibro}' SÍ está en la biblioteca")
                if self.librosParaAlquilar.length > 0:
                    iteracionesParaAlquiler = 0
                    for elementoParaAlquilar in self.librosParaAlquilar:
                        iteracionesParaAlquiler += 1
                        if elementoParaAlquilar.value.titulo == tituloLibro:
                            print(f"\nEl libro que tiene por título '{tituloLibro}' SÍ está disponible para alquilar.")
                            break

                        elif elementoParaAlquilar.value.titulo != tituloLibro and self.librosParaAlquilar.length > iteracionesParaAlquiler:
                            pass

                        elif elementoParaAlquilar.value.titulo != tituloLibro and self.librosParaAlquilar.length == iteracionesParaAlquiler:
                            print(f"\nEl libro que tiene por título '{tituloLibro}' NO está disponible para alquilar.")

                else:
                    print(f"\nEl libro que tiene por título '{tituloLibro}' NO está disponible para alquilar.")
                break

            elif elemento.value.titulo != tituloLibro and self.biblioteca.length > iteraciones:
                pass

            elif elemento.value.titulo != tituloLibro and self.biblioteca.length == iteraciones:
                print(f"\nEl libro que tiene por título '{tituloLibro}' NO está en la biblioteca")
                print(f"\nEl libro que tiene por título '{tituloLibro}' NO está disponible para alquilar.")

    def buscarLibroPorAutor(self, autorLibro: str):

        iteraciones = 0
        for elemento in self.biblioteca:

            iteraciones += 1
            if elemento.value.autor == autorLibro:
                print(f"\nEl libro que tiene por autor '{autorLibro}' SÍ está en la biblioteca")
                if self.librosParaAlquilar.length > 0:
                    iteracionesParaAlquiler = 0
                    for elementoParaAlquilar in self.librosParaAlquilar:
                        iteracionesParaAlquiler += 1
                        if elementoParaAlquilar.value.autor == autorLibro:
                            print(f"\nEl libro que tiene por autor '{autorLibro}' SÍ está disponible para alquilar.")
                            break

                        elif elementoParaAlquilar.value.autor != autorLibro and self.librosParaAlquilar.length > iteracionesParaAlquiler:
                            pass

                        elif elementoParaAlquilar.value.autor != autorLibro and self.librosParaAlquilar.length == iteracionesParaAlquiler:
                            print(f"\nEl libro que tiene por actor '{autorLibro}' NO está disponible para alquilar.")
                            
                else:
                    print(f"\nEl libro que tiene por título '{autorLibro}' NO está disponible para alquilar.")
                break

            elif elemento.value.autor != autorLibro and self.biblioteca.length > iteraciones:
                pass

            elif elemento.value.autor != autorLibro and self.biblioteca.length == iteraciones:
                print(f"\nEl libro que tiene por autor '{autorLibro}' NO está en la biblioteca")
                print(f"\nEl libro que tiene por autor '{autorLibro}' NO está disponible para alquilar.")

    def buscarLibroPorAñoPublicacion(self, añoPublicacion: int):

        iteraciones = 0
        for elemento in self.biblioteca:

            iteraciones += 1
            if elemento.value.añoPublicacion == añoPublicacion:
                print(f"\nEl libro publicado en el año '{añoPublicacion}' SÍ está en la biblioteca")
                if self.librosParaAlquilar.length > 0:
                    iteracionesParaAlquiler = 0
                    for elementoParaAlquilar in self.librosParaAlquilar:
                        iteracionesParaAlquiler += 1
                        if elementoParaAlquilar.value.añoPublicacion == añoPublicacion:
                            print(f"\nEl libro publicado en el año '{añoPublicacion}' SÍ está disponible para alquilar.")
                            break

                        elif elementoParaAlquilar.value.añoPublicacion != añoPublicacion and self.librosParaAlquilar.length > iteracionesParaAlquiler:
                            pass

                        elif elementoParaAlquilar.value.añoPublicacion != añoPublicacion and self.librosParaAlquilar.length == iteracionesParaAlquiler:
                            print(f"\nEl libro publicado en el año  '{añoPublicacion}' NO está disponible para alquilar.")
                            
                else:
                    print(f"\nEl libro publicado en el año  '{añoPublicacion}' NO está disponible para alquilar.")
                break

            elif elemento.value.añoPublicacion != añoPublicacion and self.biblioteca.length > iteraciones:
                pass

            elif elemento.value.añoPublicacion != añoPublicacion and self.biblioteca.length == iteraciones:
                print(f"\nEl libro publicado en el año '{añoPublicacion}' NO está en la biblioteca")
                print(f"\nEl libro publicado en el año '{añoPublicacion}' NO está disponible para alquilar.")