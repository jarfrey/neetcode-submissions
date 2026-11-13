class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # maybe sort each string, find in a hashmap, group together
        # group it using arrays. if it finds a new collection of 
        # characters it's a new index (i.e. act : 0, pots : 1)
        # if it finds an anagram it adds it to a list, with all
        # other anagrams from the same index
        anaGroups = []
        anaIndex = {}
        i = 0
        for strr in strs:
            strChanged = "".join(sorted(strr))
            if (strChanged in anaIndex):
                anaGroups[anaIndex[strChanged]].append(strr) 
            else:
                anaIndex[strChanged] = i
                anaGroups.append([strr])
                i+= 1
            #anaGroups = [[strr,strr],[strr]]
        return anaGroups
