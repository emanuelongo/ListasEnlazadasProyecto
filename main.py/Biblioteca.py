from Libro import Libro 

class Node:
  __slots__ = 'value', 'next', 'prev'

  def __init__(self, value):
      self.value = value
      self.next = None
      self.prev = None

  def __str__(self):
    return str(self.value)

class Biblioteca:
    def __init__(self):
        self.head = None
        self.length = 0

    def __iter__(self):
        curr_node = self.head
        while curr_node is not None:
            yield curr_node
        curr_node = curr_node.next

    def __str__(self):
        result = [str(x.prev) + '<--' + str(x.value)+ '-->'+ str(x.next) for x in self]
        #result = [str(x.value) for x in self]
        return '  '.join(result)

    def agregarLibro(self, libro: Libro):
        new_node = Node(libro)
        if not self.head:
            self.head = new_node
        else:
            lastnode = self.obtenerLibro(self.length-1)
            lastnode.next = new_node
            new_node.prev = lastnode
        self.length += 1

    def obtenerLibro(self, indice):

        if indice < -1 or indice >= self.length :
            return None
        indextemp = 0
        for cur_nodo in self:
            if indextemp==indice:
                return cur_nodo
        indextemp +=1
    
    def eliminarLibro(self, libro: Libro):
        for elemento in self:
            if elemento == libro:
                if elemento.next == None:
                    elemento.prev.next = None
                else:
                    elemento.prev.next = elemento.next.value
                    elemento.next.prev = elemento.prev.value
            else:
                pass
#Voy acá haciendo funcionalidades de Biblioteca.