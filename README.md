# ListasEnlazadasProyecto

Eres un desarrollador de software encargado de crear un sistema de gestión de alquiler de
libros en una biblioteca. El sistema debe permitir a los usuarios registrar información sobre
libros disponibles para alquilar, realizar alquileres y gestionar la devolución de libros,
adicionalmente los libros de un mismo género deben estar almacenados en forma contigua.
Requisitos:

Crea una clase llamada Libro que tenga los siguientes atributos:

Número Libro (identificador único).

Género.

Autor.

Título

Año de publicación.

Tarifa diaria de alquiler.

La implementación debe utilizar listas enlazadas que almacenarán objetos de la clase Libro.

Cada nodo de la lista debe representar un libro. El sistema debe permitir realizar las
siguientes operaciones

●Agregar un libro, debe ser posible agregar nuevos libros.se debe permitir registrar un
nuevo libro con todos sus atributos.

● Eliminar un libro, debe permitir la opción de eliminar libros.

● Buscar todos los libros por género, debe retornar cuantos libros se tienen, la
información de cada uno y adicionalmente si está o no disponible para el alquiler

● Buscar un libro por título, debe retornar si se tiene el libro en la biblioteca y
adicionalmente si está o no disponible para el alquiler 

● Buscar un libro por autor, debe retornar si se tiene el libro en la biblioteca y
adicionalmente si está o no disponible para el alquiler

● Buscar un libro por año de publicación, debe retornar si se tiene el libro en la
biblioteca y adicionalmente si está o no disponible para el alquiler

● Listar todos los libros disponibles para alquilar, los usuarios deben poder ver la lista
de libros disponibles para alquilar, mostrando todos los atributos de cada libro.

● Listar todos los libros que se encuentran alquilados, los usuarios deben poder ver la
lista de libros NO disponibles para alquilar, mostrando todos los atributos de cada
libro.

● Listar todos los libros disponibles para alquilar x Género, los usuarios deben poder
ver la lista de libros disponibles para alquilar, mostrando todos los atributos de cada
libro.

● Listar todos los libros que se encuentran alquilados x Género, los usuarios deben
poder ver la lista de libros NO disponibles para alquilar, mostrando todos los
atributos de cada libro.

● Alquilar un libro x Género, los usuarios deben poder alquilar un libro específico de la
lista enlazada.

● Alquilar un libro, los usuarios deben poder alquilar un libro específico de la lista
enlazada.

● Devolver un libro, Los usuarios también deben poder registrar la devolución de un
libro alquilado.

● Se debe otorgar un dcto del 10% x libro, si el mismo usuario alquila 2 o más libros. #DEBO RECORDAR DEVOLVER LA TUPLA DONDE PIDO LA CANTIDAD DE LIBROS

● Se debe retornar el ingreso total obtenido por alquileres de libros hasta el momento.

● Se debe permitir intercambiar los libros que estén deteriorados por un libro nuevo.

En este caso, se intercambiarán los nodos, no los valores de los nodos. Los libros
nuevos deben quedar en las mismas posiciones de los libros que están
reemplazando x deterioro.

● Sólo pueden usar listas enlazadas (en cualquiera de sus variaciones) para resolver
todos los aspectos del problema. NO pueden usar otras colecciones (por ejemplo
listas, diccionarios, tuplas, etc.).
