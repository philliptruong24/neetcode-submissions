class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for word in strs:
            count = [0] * (26)
            for char in range(len(word)):
                count[ord(word[char]) - ord('a')] += 1
            hash_table[tuple(count)].append(word)
        
        return list(hash_table.values())
        

            


        