class SNode:
        def __init__(self ,val):
            self.val =val
            self.prev =None
            self.next =None


class SList:
        def __init__(self):
            self.head =None

            """ 
            1- add_to_front(val): This method creates a new node with the  (value ,next ,prev)
            2- print_values(): This method traverses the list and prints the value of each node.
            3- add_to_back(val): This method creates a new node with the given value and adds it to the back of the list.
            """

        def add_to_front(self,val):
            new_node =SNode(val)
            new_node.next =self.head
            if self.head:
                self.head.prev =new_node
            self.head=new_node
            return self
        

        
        def print_values(self):
                runner = self.head

                while runner != None:
                    print(runner.val)
                    runner = runner.next

                return self
        

        def add_to_back(self, val):
                new_node = SNode(val)

                if self.head == None:
                    self.head = new_node
                    return self

                runner = self.head

                while runner.next != None:
                    runner = runner.next

                runner.next = new_node
                new_node.prev = runner
                return self
        


my_linked_list = SList()
my_linked_list.add_to_front(1).add_to_front(2).add_to_back(3).print_values()