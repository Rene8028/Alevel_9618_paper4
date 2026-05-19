class Node:
    def __init__(self, ND):
        self.__NodeData = ND # INTEGER
        self.__LeftNode = None # Node
        self.__RightNode = None # Node
    def GetLeft(self):
        return self.__LeftNode
    def GetRight(self):
        return self.__RightNode
    def GetData(self):
        return self.__NodeData
    def SetLeft(self, lnode):
        self.__LeftNode = lnode
    def SetRight(self, rnode):
        self.__RightNode = rnode

class Tree:
    def __init__(self, FN):
        self.__FirstNode = FN # Node
    def GetRootNode(self):
        return self.__FirstNode
    def Insert(self, NewNode):
        CI = self.__FirstNode
        Done = False
        while not Done and not CI == None:
            if NewNode.GetData() < CI.GetData():
                if CI.GetLeft() == None:
                    CI.SetLeft(NewNode)
                    Done = True
                else:
                    CI = CI.GetLeft()
            else:
                if CI.GetRight() == None:
                    CI.SetRight(NewNode)
                    Done = True
                else:
                    CI = CI.GetRight()
                    
def OutputInOrder(ThisNode):
    if not ThisNode.GetLeft() == None:
        OutputInOrder(ThisNode.GetLeft())
    print(ThisNode.GetData())
    if not ThisNode.GetRight() == None:
        OutputInOrder(ThisNode.GetRight())
        

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

MyTree = Tree(Node1)
MyTree.Insert(Node2)
MyTree.Insert(Node3)
MyTree.Insert(Node4)
MyTree.Insert(Node5)
OutputInOrder(MyTree.GetRootNode())
    
