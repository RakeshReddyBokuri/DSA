class node:
    data=None
    prv=None
    nxt=None
class ll:
    def __init__(s):
        s.head=None
    def insertf(s,i):
        nn=node()
        nn.data=i
        if s.head==None:
            s.head=nn
            return
        s.head.prv=nn
        nn.nxt=s.head
        s.head=nn
    def inserte(s,i):
        if s.head==None:
            s.insertf(i)
            return
        k=s.head
        while k.nxt!=None:
            k=k.nxt
        nn=node()
        nn.data=i
        k.nxt=nn
        nn.prv=k
    def insertm(s,p,i):
        k=s.head
        while k.nxt!=None:
            if k.data==p:
                break
            k=k.nxt
        if k.data!=p:
            print(f"{p} not found\n\n")
            return
        nn=node()
        nn.data=i
        nn.prv=k
        nn.nxt=k.nxt
        k.nxt=nn
    def display(s):
        if s.head==None:
            print("list is empty")
        k=s.head
        print(k.data)
        while k.nxt!=None:
            k=k.nxt
            print(k.data)
    def deletef(s):
        if s.head==None:
            print("List Is Empty")
            return
        s.head=s.head.nxt
        return
    def deletee(s):
        k=s.head
        if k==None:
            print("List Is Empty")
            return
        elif k.nxt==None:
            s.head=None
            return
        while k.nxt.nxt!=None:
            k=k.nxt
        k.nxt=None
    def deletem(s,p):
        k=s.head
        if k==None:
            print("List is Empty")
            return
        if k.data==p:
            s.deletef()
            return
        while k.data!=p:
            if k.nxt==None:
                print("Element not found")
                return
            k=k.nxt
        k.prv.nxt=k.nxt
        
l=ll()
while True:
    print("1.insert at first\n2.insert at the end\n3.insert at the end\n4.display\n5.delete the first value\
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
