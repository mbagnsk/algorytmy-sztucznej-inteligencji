class Queue:
    maxSize = 0
    queue = []

    def __init__(self, maxSize):
        self.maxSize = maxSize

    def put(self, value):
        if len(self.queue) < self.maxSize:
            self.queue.append(value)
        else:
            self.queue.pop(0)
            self.queue.append(value)
