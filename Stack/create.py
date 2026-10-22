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

    def print(self):
        temp=self.top
        print("elements of stack:")
        while temp:
            print(temp.data)
            temp=temp.next

    def pop(self):
        temp=self.top
        print("popped element,temp",temp.data)
        self.top=self.top.next
        temp=None


st=stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.print()
st.pop()
st.print()

            

