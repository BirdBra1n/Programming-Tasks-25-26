"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size  
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.num_items = 0
    
    def is_empty(self):
        return self.num_items == 0
        
    def is_full(self):
        return self.num_items == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            print(f"Queue is full, Cannot add '{item}'.")
            return False
        
        self.rear = self.rear + 1
        self.items[self.rear] = item
        self.num_items = self.num_items + 1
        print(f"Item '{item}' added at index {self.rear}.")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, Cannot remove item.")
            return None
        
        removed_item = self.items[self.front]
        self.items[self.front] = None

        self.front = self.front + 1
        self.num_items = self.num_items - 1
        print(f"Item '{removed_item}' removed from index {self.front - 1}.")
        return removed_item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def display(self):
        print(self.items)

def main():
    shop_line = Queue(3)

    shop_line.enqueue("Alice")
    shop_line.enqueue("Bob")
    shop_line.enqueue("Charlie")
    shop_line.display()

    shop_line.enqueue("Diana")

    print(shop_line.peek())
    shop_line.dequeue()
    shop_line.display()

if __name__ == "__main__":
    main()
