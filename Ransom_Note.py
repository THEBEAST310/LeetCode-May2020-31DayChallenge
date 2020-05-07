class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for x in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            if (ransomNote.count(x)>magazine.count(x)):
                return False
        return True
