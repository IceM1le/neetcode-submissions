class Node:
    
    def __init__(self, key: int=0, value:int=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.cache = {}
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Node) -> None:
        node.next = self.head.next
        self.head.next = node 
        node.prev = self.head
        node.next.prev = node

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if not key in self.cache: return -1                
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])                                
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.cap:
            last_node = self.tail.prev
            del self.cache[last_node.key]
            self._remove(last_node)