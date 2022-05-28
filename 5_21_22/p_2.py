class Stack:
    def __init__(self):
        self.__stack = []
        self.__size = 0

    def getSize(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0

    def push(self,element):
        self.__stack.append(element)
        self.__size += 1
    
    def pop(self):
        try:
            return_value = self.__stack.pop()
        except IndexError:
            print("Stack is empty")
            return None
        else:
            self.__size -= 1
            return return_value

if __name__ == "__main__":

    stack = Stack()

    for i in range(10):
        stack.push(i)

    while not stack.isEmpty():
        print(stack.pop(),end = " ")

    

