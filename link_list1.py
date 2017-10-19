class node:
    data=None;
    next=None;

class linked_list:
    def __init__(self):
        self.curr_node=None;
    
    def add_prepend(self,data):
        new_node=node();
        new_node.data=data;
        new_node.next=self.curr_node;
        self.curr_node=new_node;
    
    def add_append(self,data):
        new_node=node();
        new_node.data=data;
        new_node.next=None;
        temp=self.curr_node;
        while(temp.next!=None):
            temp=temp.next;
        temp.next=new_node;


    def print_list(self):
        while(self.curr_node!=None):
            print(self.curr_node.data,end=' ');
            self.curr_node=self.curr_node.next;
        print();
        

ll=linked_list();
ll.add_prepend(1);
ll.add_append(2);
ll.add_append(3);
ll.add_append(4);
ll.print_list();