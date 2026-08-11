class Queue:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ
    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def Enqueue(self, x):
        if self.first:
            f = self.first
            while f.succ:
                f = f.succ
            f.succ = Queue.Node(x, None)
        else:
            self.first = Queue.Node(x, None)

    def Dequeue(self): ##Exercise A3
        if self.first:
             self.first = self.first.succ

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        return '<' + ', '.join([str(x) for x in self]) + '>'

    def insert(self, key):
        def _insert(r, key):
            if r is None:
                return self.Node(key)
            elif key < r.key:
                r.left = _insert(r.left, key)
            elif key > r.key:
                r.right = _insert(r.right, key)
            else:
                pass
            return r

        self.root = _insert(self.root, key)

    def max(self): ##Exercise A4
        if self.root == None:
            return None
        else:
            while self.root.right:
                self.root = self.root.right
            return self.root.key
class LinkedList:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = LinkedList.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = LinkedList.Node(x, f.succ)

    def copy(self): #can be used in Exercise B2
        res = LinkedList()
        for x in self:
            new_node = LinkedList.Node(x)
            if res.first == None:
                res.first = new_node
                last = res.first
            else:
                last.succ = new_node
                last = last.succ
        return res 


    
        pass
    def middle(self): ##Exercise B3
        if self.first == None:
            return None
        else:
            slow = fast = self.first
            while fast and fast.succ:
                fast = fast.succ.succ
                slow = slow.succ
            return slow.data
        pass

def Merge(ll1,ll2): ##Exercise B2
    x1 = ll1.first
    x2 = ll2.first

    if x1 == None:
        res = ll2.copy()
    elif x2 == None:
        res = ll1.copy()
    else:
        res = LinkedList()
        if x1.data < x2.data:
            res.first = LinkedList.Node(x1.data)
            x1 = x1.succ
        else:
            res.first = LinkedList.Node(x2.data)
            x2 = x2.succ
        r = res.first
        while x1 and x2:
            if x1.data < x2.data:
                r.succ = LinkedList.Node(x1.data)
                x1 = x1.succ
            else:
                r.succ = LinkedList.Node(x2.data)
                x2 = x2.succ
            r = r.succ
        while x1:
            r.succ = LinkedList.Node(x1.data)
            x1 = x1.succ
            r = r.succ
        while x2:
            r.succ = LinkedList.Node(x2.data)
            x2 = x2.succ
            r = r.succ
    return res 

    
def main():
    print("Test A3:")
    queue = Queue()
    for x in ["A", "B", "C", "D", "E"]:
        queue.Enqueue(x)
    print(queue)
    for _ in range(5):
        queue.Dequeue()
        print(queue)
    print("Test A4:")
    X = [ [5, 8, 3, 7, 2, 6, 9], [4, 1, 3, 6, 7, 5, 8], []]
    for x in X:
        bst = BST()
        for i in x:
            bst.insert(i)
        m = bst.max()
        print(m)
    print("Test B2:")
    X = [[1,3,6,7], [], []]
    Y = [[0,2,8,9], [1,2,3], []]
    for lst1, lst2 in zip(X,Y):
        ll1, ll2 = LinkedList(), LinkedList()
        for x in lst1:
            ll1.insert(x)
        for x in lst2:
            ll2.insert(x)
        ll3 = Merge(ll1,ll2)
        print(ll3)
    print("Test B3:")
    print("The complexity of the method in B3 is ?")
    X = [[0], [1,2],[1,2,3],[1,2,3,5],[1,2,3,5,8], list(range(100))] #
    for lst in X:
        ll = LinkedList()
        for x in lst:
            ll.insert(x)
        print(ll.middle(), lst[(len(lst))//2])
if __name__ == '__main__':
    main()
