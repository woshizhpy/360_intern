class Node(object):
    def __init__(self, data = -1, lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree(object):
    def __init__(self):
        self.root = Node()
		
	#add函数 在父节点k，下插入子节点v，若k已经有一个值为v的子节点 则不插入；若k的左右子节点有为空的，则在其中插入v；
	#若k的左右节点均存在，则将v插入为右节点，再将原本的右节点插入树中	
    def add(self,k,v):
        a=0
        b=-1
        node = self.root
        if node == None:
            return
        
        queue = []
        queue.append(node)

        while queue and a==0:
            node = queue.pop(0)
            if node.data==k:
                print 'find!'
                a=1;
            if node.rchild:
                queue.append(node.rchild)
            elif a==1:
                node3=Node(v)
                node.rchild=node3
                return
            if node.lchild:
                queue.append(node.lchild)
            elif a==1:
                node3=Node(v)
                node.lchild=node3
                return
        #node1=node.lchild
        #node2=node.rchild
        #if node1.data==v or node2.data==v:
        #    print "exist"
        if a==0:
            print 'no such k'
            return
        node1=queue.pop(0)
        node2=queue.pop(0)
        #print node1.data
        #print node2.data
        if node1.data==v or node2.data==v:
            print "exist"
        else:
            if node1 and node2: 
                b=node1.data
                node1.data=v
                self.add_1(b)
            if node1==None:
                node3=Nnode(v)
                node.rchild=node3
            if node2==None:
                node.lchild=node3
        #p=node.
        print
    
    def get(self,k):
        a=0
        b=-1
        node = self.root
        if node == None:
            return
        
        queue = []
        queue.append(node)

        while queue and a==0:
            node = queue.pop(0)
            if node.data==k:
                print 'find!'
                a=1;
            if node.rchild:
                queue.append(node.rchild)
            if node.lchild:
                queue.append(node.lchild)
        print node.data
        if node.rchild==None and node.lchild==None:
            print node.data,
        if a==0:
            print 'no such k node'
            return
        else:
            while queue:
                
                node = queue.pop(0)
                if node.rchild:
                    queue.append(node.rchild)
                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild==None and node.lchild==None:
                    print node.data,
            print
            
            
        
    def add_1(self, data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node.lchild == None:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild == None:
                    tree_node.rchild = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)

 


        
        
        
    

    
    

    #if lchild and rchild are None or lchild and rchild are printed, print the parent node node and pop out of the stack
    #else lchild and rchild push into the stack
    def post_order_loop1(self):
        if self.isEmpty():
            return

        stack = []
        top = -1
        node = self.root
        stack.append(node)
        #we need to recognize the last printed node
        top += 1
        pre = None
        while stack:
            node = stack[-1]
            if node.lchild is None and node.rchild is None:
                print node.data,
                pre = node
                top -= 1
            elif not pre and (node.lchild == pre or node.rchild == pre):
                print node.data,
                pre = node
                top -= 1
            else:
                if node.rchild:
                    if top < len(stack)-1:
                        stack[top] = node.rchild
                    else:
                        stack.append(node.rchild)
                if node.lchild:
                    if top < len(stack)-1:
                        stack[top] = node.lchild
                    else:
                        stack.append(node.lchild)

    def level_order(self):
        node = self.root
        if node == None:
            return
        
        queue = []
        queue.append(node)

        while queue:
            node = queue.pop(0)
            print node.data,
            if node.rchild:
                queue.append(node.rchild)
            if node.lchild:
                queue.append(node.lchild)
        print
    

    def isEmpty(self):
        return True if self.root.data == -1 else False

if __name__ == '__main__':
    b=1
    print 'b=',b
    arr = []
    for i in range(3):
        arr.append(i)
    print arr

    tree = BinaryTree()
    for i in arr:
        tree.add_1(i)
    print 'level_order:'
    tree.level_order()
    print 'add'
    tree.add(0,12)
    print 'get'
    tree.get(0)
    print 'level_order:'
    tree.level_order()
    
    
    print '\npost_order_loop1:'
    #tree.post_order_loop1()
