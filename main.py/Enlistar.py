from Biblioteca import Biblioteca

class Listados:

    def __init__(self, librosParaAlquilar: Biblioteca, librosAlquilados: Biblioteca):
        self.librosParaAlquilar = librosParaAlquilar
        self.librosAlquilados = librosAlquilados

    def enlistarLibrosDisponiblesParaAlquilar(self):
        
        if self.librosParaAlquilar.length > 0:

            for elemento in self.librosParaAlquilar:
                print("\n===================== Libro disponible =====================\n")  
                print(f"Número del libro: {elemento.value.numeroLibro}")
                print(f"Género del libro: {elemento.value.genero}")
                print(f"Autor del libro: {elemento.value.autor}")
                print(f"Título del libro: {elemento.value.titulo}")
                print(f"Año de publicación del libro: {elemento.value.añoPublicacion}")
                print(f"Tarifa de alquiler del libro: {elemento.value.tarifaAlquiler}")

        else:
            print("\nNo hay libros disponibles para alquilar.")

    def enlistarLibrosAlquilados(self):

        if self.librosAlquilados.length > 0:

            for elemento in self.librosAlquilados:
                print("\n===================== Libro alquilado =====================\n")  
                print(f"Número del libro: {elemento.value.numeroLibro}")
                print(f"Género del libro: {elemento.value.genero}")
                print(f"Autor del libro: {elemento.value.autor}")
                print(f"Título del libro: {elemento.value.titulo}")
                print(f"Año de publicación del libro: {elemento.value.añoPublicacion}")
                print(f"Tarifa de alquiler del libro: {elemento.value.tarifaAlquiler}")

        else:
            print("\nNo hay libros alquilados.")

    def enlistarLibrosDisponiblesPorGeneroParaAlquilar(self):

        if self.librosParaAlquilar.length > 0:

            for elemento in self.librosParaAlquilar:
                print(f"\n===================== Género: {elemento.value.genero} =====================\n")  
                print(f"Número del libro: {elemento.value.numeroLibro}")
                print(f"Género del libro: {elemento.value.genero}")
                print(f"Autor del libro: {elemento.value.autor}")
                print(f"Título del libro: {elemento.value.titulo}")
                print(f"Año de publicación del libro: {elemento.value.añoPublicacion}")
                print(f"Tarifa de alquiler del libro: {elemento.value.tarifaAlquiler}")

        else:
            print("\nNo hay libros disponibles para alquilar.")

    def enlistarLibrosAlquiladosPorGenero(self):

        if self.librosAlquilados.length > 0:

            for elemento in self.librosAlquilados:
                print(f"\n===================== Género: {elemento.value.genero} =====================\n")  
                print(f"Número del libro: {elemento.value.numeroLibro}")
                print(f"Género del libro: {elemento.value.genero}")
                print(f"Autor del libro: {elemento.value.autor}")
                print(f"Título del libro: {elemento.value.titulo}")
                print(f"Año de publicación del libro: {elemento.value.añoPublicacion}")
                print(f"Tarifa de alquiler del libro: {elemento.value.tarifaAlquiler}")

        else:
            print("\nNo hay libros alquilados.")