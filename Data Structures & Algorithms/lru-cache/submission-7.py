class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head
    
    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.cap:
            last = self.tail.prev
            self._remove(last)
            del self.cache[last.key]