class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for word in strs:
            count = [0] * (26)
            for i in range(len(word)):
                count[ord(word[i]) - ord('a')] += 1
            my_tuple = tuple(count)
            if my_tuple not in hash_table:
                hash_table[my_tuple] = [word]
            else:
                hash_table[my_tuple].append(word)
        
        return list(hash_table.values())
        

            


        