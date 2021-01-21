# queue 기능 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.list = None
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_queue = Node(value)
        if self.is_empty():  # 초기상태 (한개일경우 처음이자 끝이기때문)
            self.head = new_queue
            self.tail = new_queue
            return

        self.tail.next = new_queue
        self.tail = new_queue
        # 어떻게 하면 될까요?

    def dequeue(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            print("queue is empty! ")

        delete_queue = self.head
        self.head = self.head.next

        return delete_queue.data

    def peek(self):
        if self.is_empty():
            return "queue is empty!"
        # 어떻게 하면 될까요?
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.list.head is None


queue = Queue
queue.enqueue(3)
print(queue.peek())
