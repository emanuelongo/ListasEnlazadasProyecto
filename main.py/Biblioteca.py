from Libro import Libro 

class Node:
  __slots__ = 'value', 'next', 'prev'

  def __init__(self, value: Libro):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.value)


class Biblioteca:

  def __init__(self):
    self.head = None
    self.tail = None
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


  def append(self, value: Libro):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1
    return "\nLibro agregado"

  def prepend(self, value: Libro):
    new_node = Node(value)
    if self.head == None:
       self.head = new_node
       self.tail = new_node
    else:
       new_node.next = self.head
       self.head.prev = new_node
       self.head = new_node
    self.length += 1

  def get(self, index):
    if index == -1 or index == self.length-1:
       return self.tail
    elif index < -1 or index >= self.length :
       return None

    indextemp = 0
    for cur_nodo in self:
      if indextemp==index:
        return cur_nodo
      indextemp +=1

  def insert(self, value: Libro, index: int):
    if index== 0:
      self.prepend(value)
      return True
    elif index ==-1 or index == self.length-1:
      self.append(value)
      return True
    elif index < -1 or index > self.length-1:
      return False
    else:
      new_node = Node(value)
      prev_node = self.get(index-1)
      nextnode = self.get(index)
      new_node.next = prev_node.next
      new_node.prev = prev_node
      prev_node.next = new_node
      nextnode.prev = new_node
      self.length += 1
      return True

    return False

  def traverse(self):
    for cur_node in self:
      print(cur_node.value)

  def search(self,target):
    index = 0
    for cur_node in self:
      if cur_node.value == target:
        return index
      index += 1
    return -1


  def set(self, index: int, value: Libro):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False

  def pop_first(self):
    if self.length == 0:
      return None
    popped_node = self.head
    if self.length == 1:
      self.head = self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
      popped_node.next = None
    self.length -= 1
    return popped_node

  def pop(self):
    if self.length == 0:
      return None
    popped_node = self.tail
    if self.length == 1:
      self.head = self.tail = None
    else:
      prevtail_node = self.get(self.length-2)
      prevtail_node.next = None
      self.tail = prevtail_node
    self.length -= 1
    return popped_node

  def remove(self, index):
    if index < -1 and index >= self.length:
      return None
    elif index == 0:
      self.pop_first()
      return "\nLibro eliminado"
    elif index == -1 or index == self.length -1:
      self.pop()
      return "\nLibro eliminado"
    else:
        prev_node = self.get(index-1)
        next_node = self.get(index)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        next_node.prev = prev_node
        popped_node.next = None
        self.length -= 1
        return "\nLibro eliminado"

  def delete_all(self):
    self.head = None
    self.tail = None
    self.length = 0