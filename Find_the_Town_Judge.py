class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        list1=[]
        for x in range(len(trust)):
            list1.append(trust[x][0])
        list2=[]
        for x in range(len(trust)):
            list2.append(trust[x][1])

        flag=0
        for x in range(1,N+1):
            if not(x in list1) and list2.count(x)==N-1:

                flag=1
                return x

        if flag==0:
            return("-1")
                
