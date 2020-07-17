"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #1. base case 
            # if the value of this node matches the target, then TRUE 
            # compare the target against this node's value to determine which direction to go in
        #2. how do we move closer to the base case
            # if the target is less 
                #if left is Null
                #value is not contained in the tree 
                # else call 'contains' on the left child 
            #else if the target is more 
                #if right is Null
                #value is not contaied in the tree 
                # else call 'contains' on the right child

        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else: 
                return self.left.contains(target)
        else:
            if self.right is None:
                return False 
            else: 
                return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        #Check the right most value in the tree 
        # we'll keep going right until there is no right child node 

        if self.right is None:      #base case
            return self.value
        else:
            return self.right.get_max() #recurisve statement

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the anonymous function on 'self.value'
        # if this node has a left child 
            #pass the anonymous fn to it
        #if this node has a right child 
            #pass the anonymous fn to it 

        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        #1. if value on the left is not None 
        #    then call in_order_print() on itself
        #       else if left is None
        #       print the value stored inside

        #2. if value on the right is not None 
        #   then call the in in_order_print() on itself 
        #   else if right is None 
        #   print the value stored inside 

        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque
        # BFT: FIFO 
        # use a queue to faciitate the ordering 
        queue = deque()
        queue.append(self)

        #continue to traverse so long as there are nodes in the queue 
        while len(queue) > 0:
            current = queue.popleft()
    #add the right child first 
            if current.left: 
                queue.append(current.left)
    #add the left child 
            if current.right:
                queue.append(current.right)
            
            print(current.value)
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #DFT: LIFO 
        # we'll use a stack
        stack = []
        stack.append(self)

        # so long as our stack has nodes in it 
        # there's more nodes to traverse 
        while len(stack) > 0: 
            # pop the top node from the stack 
            current = stack.pop()

            # add the current node's right child first
            if current.right:
                stack.append(current.right)
            # add the current node's left child 
            if current.left:
                stack.append(current.left)
            
            print(current.value)

