class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None]* self.__max_size
        self.__rear = -1
        self.__front = -1
    def is_full(self):
        if ((self.__front == 0 and self.__rear == self.__max_size-1) or (self.__front == self.__rear +1)):
            return True
        else:
            return False
    def is_empty(self):
        if self.__front == -1 and self.__rear == -1:
            return True
        else:
            return False
    def enqueue(self,data):
        if self.is_full():
            print("Overflow")
            return
        else:
            if self.is_empty():
                self.__front = 0
                self.__rear = 0
            elif self.__rear == self.__max_size-1:
                self.__rear = 0
            else:
                self.__rear = self.__rear + 1
            #print(self.__elements[self.__rear])    
        self.__elements[self.__rear] = data
        print("Insertion Succesfull",data)
                      
            
    def dequeue(self):
        if self.__front == -1 and self.__rear == -1:
            print("Underflow")
            return
        elif self.__front == self.__rear == 0:
            self.__rear = -1
            self.__front = -1
            del(self.__elements[0])
            print("One element deleted")
        else:
            if self.__front == self.__max_size -1:
                self.__front = 0
            else:
                self.__front+=1
            self.__elements[self.__front-1] = None
            print("Deleted element")
                
    def display(self):
        print(self.__elements)
        if self.__front == -1:
            print("Circular list empty")
            return
        else:
            limit = self.__max_size
            if self.__front < self.__rear:
                limit = self.__rear
            else:
                limit = self.__max_size - 1
            for l in range(self.__front,limit+1):
                print(self.__elements[l],end=" ")
            if self.__front > self.__rear:
                for l in range(0,self.__rear+1):
                    print(self.__elements[l],end=" ")
                    
                
q = Queue(5)
q.dequeue()
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)
q.enqueue(55)
q.display()
q.dequeue()
q.dequeue()
q.display() 
q.enqueue(55)
q.enqueue(66)
q.display()
