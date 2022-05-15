class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr=[]
        self.itr(nestedList)
        self.arr=self.arr[::-1]
        
    def itr(self,nl):
        if(type(nl)==list):
            for i in nl:
                self.itr(i)
        else:
            if(nl.isInteger()):
                self.arr.append(nl.getInteger())
            res=nl.getList()
            if(res):
                self.itr(res)
        
    def next(self) -> int:
        return self.arr.pop()
    
    def hasNext(self) -> bool:
        return len(self.arr)>0
