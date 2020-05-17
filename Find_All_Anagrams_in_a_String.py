class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(p)
        list1=[]
        p=sorted(p)
        p=''.join(p)
        for x in range(len(s)-n+1):
            new=s[x:x+n]
            new=sorted(new)
            new=''.join(new)
            if new==p:
                list1.append(x)
        return list1
