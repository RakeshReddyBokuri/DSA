class node:
    data=None
    prv=None
    nxt=None
class dll:
    def __init__(s):
        s.head=None
        s.tail=None
    def insertf(s,i):
        nn=node()
        nn.data=i
        if s.head==None:
            s.head,s.tail=nn,nn
            nn.nxt=s.tail
            nn.prv=s.head
            return
        s.head.prv=nn
        nn.nxt=s.head
        s.head=nn
        s.head.prv=s.tail
        s.tail.nxt=s.head
    def inserte(s,i):
        if s.head==None:
            s.insertf(i)
            return
        k=s.head
        while k.nxt!=s.head:
            k=k.nxt
        nn=node()
        nn.data=i
        k.nxt=nn
        nn.prv=k
        nn.nxt=s.head
        s.tail=nn
    def insertm(s,p,i):
        k=s.head
        while k.nxt!=s.head:
            if k.data==p:
                break
            k=k.nxt
        if k.data!=p:
            print(f"{p} not found\n\n")
            return
        nn=node()
        nn.data=i
        nn.prv=k
        if k.nxt==s.head:
            s.tail=nn
            nn.nxt=s.head
        nn.nxt=k.nxt
        k.nxt=nn
    def display(s):
        if s.head==None:
            print("list is empty")
            return
        k=s.head
        print(k.data)
        while k.nxt!=s.head:
            k=k.nxt
            print(k.data)
    def deletef(s):
        if s.head==None:
            print("List Is Empty")
            return
        if s.head==s.tail:
            s.head,s.tail=None,None
            return
        s.head=s.head.nxt
        s.head.prv=s.tail
        s.tail.nxt=s.head
        return
    def deletee(s):
        k=s.head
        if k==None:
            print("List Is Empty")
            return
        elif k.nxt==s.head:
            s.head=None
            return
        while k.nxt.nxt!=s.head:
            k=k.nxt
        k.nxt=s.head
        s.tail=k
    def deletem(s,p):
        k=s.head
        if k==None:
            print("List Is Empty")
            return
        elif k.nxt==s.head:
            s.head,s.tail=None,None
        while k.data!=p:
            if k.nxt==s.head:
                print("Element not found")
                return
            k=k.nxt
        k.prv.nxt=k.nxt
        if k.nxt==s.head:
            s.tail=k.prv
l=dll()
while True:
    print("1.insert at first\n2.insert at the end\n3.insert after an element\n4.display\n5.delete the first value\
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
