class node:
    data=0
    nxt=None
class ll:
    def __init__(s):
        s.head=None
        s.tail=None
    def insertf(s,f):
        nn=node()
        nn.data=f
        if s.head==None:
            s.head=nn
            nn.nxt=s.head
            s.tail=nn
        else:
            nn.nxt=s.head
            s.head=nn
            s.tail.nxt=s.head
    def inserte(s,e):
        nn=node()
        if s.head==None:
            s.head=nn
            s.tail=nn
        nn.data=e
        s.tail.nxt=nn
        nn.nxt=s.head
        s.tail=nn
    def insertm(s,p,m):
        if s.head==None:
            print("list is empty we cannot insert in between")
            return
        k=s.head
        while k.data!=p:
            if k.nxt==s.head:
                print("Element not found")
                return
            k=k.nxt
        nn=node()
        nn.data=m
        nn.nxt=k.nxt
        k.nxt=nn
        if nn.nxt==s.head:
            s.tail=nn
    def deletef(s):
        if s.head==None:
            print("No nodes to delete")
        elif s.head.nxt==s.head:
            s.head=None
        else:
            s.head=s.head.nxt
            s.tail.nxt=s.head
    def deletee(s):
        if s.head==None:
            print("No nodes to delete")
        elif s.head==s.head.nxt:
            s.head=None
        else:
            k=s.head
            while k.nxt!=s.tail:
                k=k.nxt
            k.nxt=s.head
            s.tail=k
    def deletem(s,p):
        if s.head==None:
            print("list is empty we cannot delete in between")
            return
        if s.head.data==p:
            s.deletef()
            return
        k=s.head
        while k.data!=p:
            if k.nxt==s.head:
                print("Element not found")
                return
            o=k
            k=k.nxt
        o.nxt=k.nxt
    def display(s):
        if s.head==None:
            print("list is empty")
            return
        k=s.head
        while True:
            print(k.data)
            if k.nxt==s.head:
                break
            k=k.nxt   
l=ll()
while True:
    print("1.insert at first\n2.insert at the end\n3.insert after a value\n4.display\n5.delete the first value\
\n6.delete at end\n7.delete a specific element\n8.exit\n")
    c=input("Enter your choice(1 to 5): ")
    if c=="1":
        a=int(input("Enter the data : "))
        l.insertf(a)
    elif c=="2":
        a=int(input("Enter the data : "))
        l.inserte(a)
    elif c=="3":
        b=int(input("Enter the privious data: "))
        a=int(input("Enter the data : "))
        l.insertm(b,a)
    elif c=="4":
        l.display()
    elif c=="5":
        l.deletef()
    elif c=="6":
        l.deletee()
    elif c=="7":
        a=int(input("Enter the data to be deleted: "))
        l.deletem(a)
    elif c=="8":
        break
    else:
        print("INVALID INPUT")
        
        
        
