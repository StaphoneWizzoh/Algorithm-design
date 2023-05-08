class StandardNode: 
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
    def __str__(self,data):
        return str(data)


class DetailedNode:
    def __init__(self,data=None,next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
    def __str__(self,data):
        return str(data)
    
class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
        
    
    def append(self, data):
        # time complexity of O(1)
        
        node = StandardNode(data)
        if self.head: 
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1
        
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
            
    def search(self,data):
        for node in  self.iter():
            if data == node:
                return True
        return False
            
            
    def delete(self,data):
        current = self.tail
        prev = self.tail
        
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
            
    def clear(self):
        self.head = None 
        self.tail = None
            
        
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None 
        self.tail = None
        self.count = 0
        
    def append(self,data):
        new_node = DetailedNode(data,None,None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1
            
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
            
    def delete(self,data):
        current = self.head
        node_deleted = False
        if current is None: # Node not found in the list
            node_deleted = False
            
        elif current.data == data: # Node is located at the list start
            self.head = current.next
            self.head.prev = None
            node_deleted = True
            
        elif self.tail.data == data: # Node is located at the list end
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else: # Node is at the middle, hence searc for it and delete it
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                current = current.next
        if node_deleted:
            self.count -=1
        
    def contain(self,data):
        for node_data in self.iter():
            if data == node_data:
                return True
            return False
            
    
    
    
    
words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append("bacon")


for word in words.iter():
    print(word)
    
print(words.count)

# words.delete("ham")
# for word in words.iter():
#     print(word)
    
# print(words.count)
# print(words.contain("bacon"))