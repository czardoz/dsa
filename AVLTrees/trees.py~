'''
Created on Sep 5, 2012

@author: czardoz
'''

def printval(node):
    if node is not None:
        print node.data

class Node:
    def __init__(self, data, left = None,
                 right = None, parent = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data
        
    def __str__(self):
        x  = z = w = ""
        if self.parent is not None:
            x = "    Parent: " + str(self.parent.data)
        y = "    Me: " + str(self.data)
        if self.left is not None:
            z = "    My left: " + str(self.left.data)
        if self.right is not None:
            w = "    My right: " + str(self.right.data)
        return x+y+z+w
    
    def numofchildren(self):
        count = 0
        if self.left:
            count+=1
        if self.right:
            count+=1
        return count
        
    def lookup(self, value):
        if value == self.data:
            return self
        elif value > self.data:
            if self.right == None:
                return None
            else:
                return self.right.lookup(value)
        else:
            if self.left == None:
                return None
            else:
                return self.left.lookup(value)
    
    def insert(self, value):
        if value > self.data:
            if self.right == None:
                self.right = Node(value, parent = self)
            else:
                self.right.insert(value)
        elif value < self.data:
            if self.left == None:
                self.left = Node(value, parent = self)
            else:
                self.left.insert(value)        
     
    def delete(self, data):
        node = self.lookup(data)
        if node is None:
            return
        parent = node.parent
        if node is not None:
            children_count = node.numofchildren()
            if children_count == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                    n.parent = parent
                else:
                    parent.right = n
                    n.parent = parent
                del node
            else:
                successor = self.getsucessor(node.data)
                node.data = successor.data
                if successor.isleftchild():
                    successor.parent.left = None
                else:
                    successor.parent.right = None

    def get_data(self):
        stack = []
        node = self
        while stack or node: 
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right

    def get_array(self):
        array = []
        for i in self.get_data():
            array.append(i)
        return array

    def get_min(self):
        x = self
        while x.left != None:
            x = x.left
        return x

    def get_max(self):
        x = self
        while x.right != None:
            x = x.right
        return x

    def get_height(self):
        if self.numofchildren() == 0:
            return 0
        else:
            if self.left != None:
                hleft = self.left.getheight()
            else:
                hleft = 0
            if self.right != None:
                hright = self.right.getheight()
            else:
                hright = 0
            return 1 + max(hleft, hright)        
    
    def display(self, prefix = '    '):
        if self.left != None:
            self.left.display(prefix + '    ')
        print prefix + str(self.data)
        if self.right != None:
            self.right.display(prefix+'    ')
    
    def printdetails(self):
        root = self
        for i in self.get_data():
            print root.lookup(i)
    
    def get_sucessor(self, value):
        asorted = self.getarray()
        i = asorted.index(value)
        return self.lookup(asorted[i+1])
        
    def get_predecessor(self, value):
        asorted = self.getarray()
        i = asorted.index(value)
        return self.lookup(asorted[i-1])
        
    def isleftchild(self):
        if self.parent == None:
            return False
        if self.parent.left == self:
            return True
        else:
            return False
    
    def isrightchild(self):
        if self.parent == None:
            return False
        if self.parent.right == self:
            return True
        else:
            return False

    def rotateright(self):
        if self.left is None:
            return
        q = self
        above = q.parent
        p = q.left
        b = p.right
        p.parent = above
        if q.isleftchild():
            if above is not None:
                above.left = p
        else:
            if above is not None:
                above.right = p
        p.right = q
        q.parent = p
        q.left = b
        if b is not None:
            b.parent = q
                
    def get_root(self):
        curr = self
        while curr.parent is not None:
            curr = curr.parent
        return curr

def maketree(a):
    root = Node(a.pop(0))
    for i in a:
        root.insert(i)
    return root        
        
def main():
    a = [23,212,21,4,51,13,124,57,74]
    x = maketree(a)
    x.display()
    print "==========================="
    z = x.lookup(124)
    z.rotateright()
    print "==========================="
    x.get_root().display()
    print "==========================="
        
if __name__ == '__main__':
    main()