class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum=0
        for x in J:
            sum=sum+S.count(x)
        return sum
