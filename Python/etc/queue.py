class Queue:
    list = []

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        return self.list.pop(0)


queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
