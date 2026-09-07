def isAnagram(self, s: str, t: str) -> bool:
        mydict={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            mydict[s[i]]=mydict.get(s[i],0)+1
        for i  in range(len(t)):
            if t[i] not in mydict:
                return False
            if t[i] in mydict:
                mydict[t[i]]-=1
        for num in mydict:
            if mydict[num]!=0:
                return False
        return True