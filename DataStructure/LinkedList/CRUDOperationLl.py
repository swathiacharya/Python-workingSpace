'''
1 CREATING
2 PRINTING
3 INSERTION
         i END INSERTION
        ii BEGINNING INSERTION
       iii SPECIFIED POSITION
4 DELETION
         i END DELETION
        ii BEGINNING DELETION
       iii SPECIFIED POSITION

'''

class Node:
    def __init__(self, data, index = 0):
        self.index = index
        self.data = data
        self.next = None


class SinglelinkedList:
    ''' CONSTRUCTOR '''
    def __init__(self):
        self.head = None
        self.tail = None

    ''' INSERTION AT THE END '''
    def append(self, *arg):
        temp = self.head
        # print(arg)
        # //prints the object
        for node in arg:
            self.tail = node
            temp.next = node
            temp = temp.next
         
     '''
         def append(self, *argvNode):
        temp = self.head
        tail = self.tail
        
        if temp.next is None:
            for node in argvNode:
                temp.next = node
                temp = temp.next

            self.tail =temp
        print(self.head)
        print(self.tail)
        else:    
            for node in argvNode:
                self.tail.next = node
                self.tail = node

            
     '''

    ''' BEGINNING INSERTION '''
    def add(self, *arg):
        for node in arg:
            node.next = self.head
            self.head = node
        temp = self.head
        count = 0
        while temp is not None:
            temp.index = count
            count +=1
            temp = temp.next
        
    ''' SPECIFIED INDEX POSITION '''
    def onIndex(self, index, node):
        temp =self.head
        count = index
        node.index = index
        if temp.index == index :
            self.add(node)
        else:
            while temp.index is not index-1:
                temp = temp.next

            node.next = temp.next
            temp.next = node
            temp = node
            temp = temp.next
            while temp is not None:
                temp.index = count + 1
                count +=1
                temp = temp.next


    def printf(self):
        temp = self.head
        while temp is not None:
            print('|{} {}|--->'.format(temp.index, temp.data),end='')
            temp = temp.next
        print('None')

        # print("Head VALUE ==> {}".format(self.head.data))

        # print("Tail VALUE ==> {}".format(self.tail.data))





if __name__ == "__main__" :
    sll = SinglelinkedList()
    # print(sll.head.index)
    sll.head = Node("head", 0)
    # print(sll.head.index)
    
    data1 = Node("data1", 1)
    data2 =  Node("data2", 2)
    data3 = Node("final", 3)

    # printingNode = (Node)input() // Error

    # sll.printf()
    sll.append(data1, data2, data3)
    
    sll.printf()
    
    sll.add(Node('insert beginning'))
    sll.printf()
    
    sll.onIndex(3, Node('specifiedIndex'))
    sll.printf()
    
