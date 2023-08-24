class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print("Empty")
        else:
            h=self.head
            while h is not None:
                print(h.data,"--->",end=" ")
                h=h.next

    def first(self,value):
        n=Node(value)
        n.next=self.head
        self.head=n

    def end(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            h=self.head
            while h.next is not None:
                h=h.next
            h.next=n

    def after(self,value,x):
        h=self.head
        while h is not None:
            if(h.data==x):
                break
            h=h.next

        if h is None:
            print("Not found")
        else:
            n=Node(value)
            n.next=h.next
            h.next=n

    def before(self,value,x):
        h=self.head
        if h is None:
            return
        if h.data==x:
            self.first(value)
            return
        temp=self.head
        while h is not None:
            if(h.data==x):
                break
            h=h.next
        while temp is not None:
            if(temp.next==h):
                break
            temp=temp.next
        if temp is None:
            print("Not found")
        else:
            n=Node(value)
            n.next=temp.next
            temp.next=n

s=Linked_list()
s.first(10)
s.end(1)
s.after(12,10)
s.before(88,1)
s.print()
