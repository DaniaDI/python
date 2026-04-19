
class SNode:
        def __init__(self ,val):
            self.val =val
            self.next =None


class SList:
        def __init__(self):
            self.head =None

        def add_to_front(self,val):
            new_node =SNode(val)
            new_node.next =self.head
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
                return self
        

        def remove_from_front(self):
            if self.head == None:#فاضية ما يرجع ايششي 
                return None

            value = self.head.val # يدخل القيمة في متغير
            self.head = self.head.next # يغير اول head  الى التالي
            return value
        
        def remove_from_back(self):
                if self.head == None:#فاضية ما يرجع ايششي 
                    return None

                if self.head.next == None:#في حالة وجود عنصر واحد فقط
                    value = self.head.val
                    self.head = None
                    return value

                runner = self.head

                while runner.next.next != None:#"إذا اللي بعد اللي بعده مش فاضي، كمل"
                    runner = runner.next

                value = runner.next.val
                runner.next = None # "خلي اللي بعده يساوي فاضي، يعني حذف العنصر الأخير"
                return value

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()