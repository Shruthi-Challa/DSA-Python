class MyCircularDeque(object):

    def __init__(self, k):
        self.deque = [0] * k
        self.size = k
        self.count = 0
        self.front = 0
        self.rear = -1

    def insertFront(self, value):
        if self.isFull():
            return False

        self.front = (self.front -1 + self.size) % self.size
        self.deque[self.front] = value
        self.count +=1
        return True
        

    def insertLast(self, value):
        if self.isFull():
            return False

        self.rear = (self.rear + 1 )%self.size
        self.deque[self.rear] = value
        self.count += 1
        return True
        

    def deleteFront(self):
        if self.isEmpty():
            return False

        self.front = (self.front + 1  )%self.size
        self.count -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1 + self.size ) % self.size
        self.count -=1
        return True
        

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.deque[self.front]
        

    def getRear(self):
        if self.isEmpty():
            return -1

        return self.deque[self.rear]
        

    def isEmpty(self):
        return self.count == 0
        

    def isFull(self):
        return self.count == self.size