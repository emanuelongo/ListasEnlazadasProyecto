from Biblioteca import Biblioteca

class Devolucion:
    
    def __init__(self, librosParaAlquilar: Biblioteca, librosAlquilados: Biblioteca, biblioteca: Biblioteca):
        self.librosParaAlquilar = librosParaAlquilar
        self.librosAlquilados = librosAlquilados
        self.biblioteca = biblioteca

    def devolverLibro(self, numeroLibro: str):
        
        iteracionesLibrosAlquilados = 0
        for elemento in self.librosAlquilados:

            iteracionesLibrosAlquilados += 1
            if elemento.value.numeroLibro == numeroLibro:
                libroObtenidoDeAlquilados = self.librosAlquilados.get(iteracionesLibrosAlquilados - 1).value
                
                self.librosParaAlquilar.append(libroObtenidoDeAlquilados)
                self.librosAlquilados.remove(iteracionesLibrosAlquilados - 1)

                print("\n===================== Libro devuelto =====================\n")  
                print(f"Número del libro: {elemento.value.numeroLibro}")
                print(f"Género del libro: {elemento.value.genero}")
                print(f"Autor del libro: {elemento.value.autor}")
                print(f"Título del libro: {elemento.value.titulo}")
                print(f"Año de publicación del libro: {elemento.value.añoPublicacion}")
                print(f"Tarifa de alquiler del libro: {elemento.value.tarifaAlquiler}")

            elif elemento.value.numeroLibro != numeroLibro and self.librosAlquilados.length > iteracionesLibrosAlquilados:
                pass

            elif elemento.value.numeroLibro != numeroLibro and self.librosAlquilados.length == iteracionesLibrosAlquilados:
                print(f"\nEl libro con número de libro {numeroLibro} no está alquilado.")
                print("\nIngresa el número de un libro alquilado.\n")
                break