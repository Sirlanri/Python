#不会，已经暂时抛弃
class tree():
    def __init__(self,left=0,right=0,value=0):
        self.left=left
        self.right=right
        self.value=value
    def putinleft(self,n):
        self.value=n
    def putinright(self,n):
        self.value=n
   
    def outall(self):
        if self.value ==0:
            return
        print(self.value)
        if not self.left is None:
            tree.outall(self.left)
        if not self.right  is None:
            tree.outall(self.right)
t4=tree(value=4)
t5=tree(value=5)
t3=tree(value=3)
t2=tree(left=t4,right=t5,value=2)
t1=tree(left=t2,right=t3,value='root')

t1.outall()