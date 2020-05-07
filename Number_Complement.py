class Solution:
    def findComplement(self, num: int) -> int:
        ans=bin(num)[2:]
        ans1=''
        for x in range(len(ans)):
            if ans[x]=='0':
                ans1=ans1+'1'
            else:
                ans1=ans1+'0'
        ans1=int(ans1,2)
        return ans1
