class Node:
    def __init__(self, ThisData):
        self.__LeftPointer = -1  #INTEGER
        self.__Data = ThisData  #INTEGER
        self.__RightPointer = -1  #INTEGER
        
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    
    def SetLeft(self, ThisLeft):
        self.__LeftPointer = ThisLeft
    def SetRight(self, ThisRight):
        self.__RightPointer = ThisRight
    def SetData(self, ThisData):
        self.__Data = ThisData

class TreeClass:
    def __init__(self):
        self.__Tree = [] #20 elements of type Node
        self.__FirstNode = -1 #INTEGER
        self.__NumberNodes = 0 #INTEGER
        for i in range(20):
            self.__Tree.append(Node(-1))

    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes = self.__NumberNodes + 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            NextPointer = self.__FirstNode
            PrePointer = -1
            Turn = 'None'
            while NextPointer != -1:
                PrePointer = NextPointer
                if NewNode.GetData() < self.__Tree[NextPointer].GetData():
                    NextPointer = self.__Tree[NextPointer].GetLeft()
                    Turn = 'Left'
                elif NewNode.GetData() > self.__Tree[NextPointer].GetData():
                    NextPointer = self.__Tree[NextPointer].GetRight()
                    Turn = 'Right'
            if Turn == 'Left':
                self.__Tree[PrePointer].SetLeft(self.__NumberNodes)
            elif Turn == 'Right':
                self.__Tree[PrePointer].SetRight(self.__NumberNodes)
            self.__NumberNodes = self.__NumberNodes + 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No Nodes")
        else:
            print("LeftPointer Data RightPointer")
            #print("{:^12} {:^12} {:^12}".format("LeftPointer","Data","RightPointer"))
            for j in range(0, self.__NumberNodes):
                print(self.__Tree[j].GetLeft(), self.__Tree[j].GetData(),self.__Tree[j].GetRight())
                #print("{:^12} {:^12} {:^12}".format(self.__Tree[j].GetLeft(), self.__Tree[j].GetData(), self.__Tree[j].GetRight()))

TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()
            
