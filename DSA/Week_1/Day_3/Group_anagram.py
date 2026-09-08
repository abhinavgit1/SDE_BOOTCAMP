def groupAnagrams(self, strs):
        mydict={}
        for word in strs:
            sword="".join(sorted(word))
            mydict.setdefault(sword,[]).append(word)
        return list(mydict.values())