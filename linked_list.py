class node:
    def __init__(self,d):
        self.d=d
        self.n=None
class listop:
    def __init__(self):
        self.h=None
    def insertats(self,nd):
        nn=node(nd)
        nn.n=self.h
        self.h=nn
    def insertafter(self,p,nd):
        n=self.h
        if n==None:
            print("LIst is Empty")
            return
        while n.d!=p:
            n=n.n
            if n==None:
                print("Element not found")
                return
        nn=node(nd)
        nn.n=n.n
        n.n=nn
    def insertate(self,nd):
        nn=node(nd)
        if self.h is None:
            self.h=nn
            return
        l=self.h
        while l.n is not None:
            l=l.n
        l.n=nn
        nn.n=None
    def traverse(self):
        n=self.h
        while n:
            print(n.d)
            n=n.n
    def deleteatf(self):
        if self.h is None:
            print("list is empty")
            return
        n=self.h
        self.h=n.n
    def deleteatl(self):
        if self.h is None:
            print("it's empty")
            return
        n=self.h
        if n.n is None:
            self.h=None
            return
        while n is not None:
            if n.n is not None:
                k=n
            n=n.n
        k.n=None
    def deletem(s,e):
        if s.h==None:
            print("List is empty")
            return
        if s.h.d==i:
            s.deleteatf()
            return
        k=s.h
        while k.d!=i:
            if k.n==None:
                print("Element Not Found")
                return
            o=k
            k=k.n
        o.n=k.n
        
n=listop()
while True:
    print("1.Insert at first\n2.Insert at end\n3.Insert in between\n4.delete at first\n5.delete at end\n6.traverse\n7.delete a specific element\n8.exit")
    c=input("Enter your choice: ")
    if c=="1":
        a=int(input("Enter the values :"))
        n.insertats(a)
        print("Inserted successfully")
    elif c=="2":
        a=int(input("Enter the values :"))
        n.insertate(a)
        print("Inserted successfully")
    elif c=="3":
        p=int(input("Enter the privious node :"))
        nd=int(input("Enter the new node :"))
        n.insertafter(p,nd)
    elif c=="4":
        n.deleteatf()
    elif c=="5":
        n.deleteatl()
    elif c=="6":
        print("LINKED LIST : ")
        n.traverse()
    elif c=="7":
        i=int(input("Enter the element to be deleted: "))
        n.deletem(i)
    elif c=="8":
        break
    else:
        print("Invalid Input")
    
        
