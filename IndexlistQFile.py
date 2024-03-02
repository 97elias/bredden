class IndexlistQ:
    def __init__(self, __list = []):
        self.__list = __list

    def enqueue(self, item):
        self.__list.append(item)
    
    def dequeue(self):
        extracted = self.__list.pop(0)
        return extracted
    
    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        return False


def basictest():
    q = IndexlistQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()

    # Förväntat resultat
    if (x == 1 and y == 2 and q.isEmpty()):
        print("test OK")
    else:
        print("FAILED expected x=1 and y=2 and an empty list but got x =", x, " y =", y, " and empty list is", q.isEmpty())

if __name__ == '__main__':
    basictest()