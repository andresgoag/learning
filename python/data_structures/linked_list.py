class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_values(self, data_list):
        # self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + " --> "
            itr = itr.next

        print(listr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1





#################################
# Macheight

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
    """This is a linked list implementation"""

    def __init__(self):
      self.head = None
      self.length = 0

    def push_front(self, val):
        """Add a new element to the front of the linked list. O(1)"""
        node = Node(val, self.head)
        self.head = node
        self.length += 1

    def get_element(self, index):
        """Returns the value of the element at the provided index. O(n)"""
        if index < 0 and index < self.count():
          raise IndexError
          
        count = 0
        itr = self.head
        while itr:
          if count == index:
            return itr.data
          itr = itr.next
          count += 1

    def count(self):
        """Returns the number of elements in the list. O(1)"""
        return self.length

    def pop_front(self):
        """Removes the val from the front of the list and returns the value
        of that val. O(1)"""
        if self.head is None:
          raise Exception("List is empty")
        value = self.head.data
        self.head = self.head.next
        return value

    def insert_after(self, index, val):
        """Inserts an val in the list after the provided index. O(n)"""
        if index < 0 and index < self.count():
          raise IndexError

        count = 0
        itr = self.head
        while itr:
          if count == index:
            node = Node(val, itr.next)
            itr.next = node
            break
          itr = itr.next
          count += 1
        
    def remove_element(self, index):
        """Removes element at the provided index. Returns the removed
        element. O(n)"""
        if index < 0 and index < self.count():
          raise IndexError

        if index == 0:
          value = self.head.data
          self.head = self.head.next
          return value

        count = 0
        itr = self.head
        while itr:
          if count == index - 1:
            value = itr.next.data
            itr.next = itr.next.next
            break
          itr = itr.next
          count += 1
        return value
        
    def reverse(self):
        """Reverses the direction of the linked list. O(n)"""
        count = 0
        itr = self.head
        prev = None

        while itr:
          temp_next = itr.next
          if temp_next is None:
            self.head = itr

          itr.next = prev
          prev = itr
          itr = temp_next
          count += 1









if __name__ == "__main__":

    li = LinkedList()
    li.insert_at_begining(5)
    li.insert_at_begining(89)
    li.insert_at_end(54)
    li.insert_values(["Andres", "David", "Daniel"])
    print(f"List length is {li.get_length()}")
    li.print()












