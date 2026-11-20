class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
        
    def isempty(self):
        return self.top is None
        
    def push(self,newnode):
        newnode.next=self.top
        self.top=newnode


 
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print("popped element,temp",temp.data)
            self.top=self.top.next
            temp=None

    def reverse(self):
        temp=self.top
        while temp:
            self.push(Node(temp.data))
            temp=temp.next
    
    def print(self):    
        temp=self.top
        print("elements of stack:")
        while temp:
            print(temp.data)
            temp=temp.next
    

st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.print()

st1.reverse()

            

