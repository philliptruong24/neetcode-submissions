class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.isWord = True

    def search(self, word: str) -> bool:

        node = self.root
        def dfs(i):
            nonlocal node
            if i == len(word):
                return node.isWord
            
            if not node.children:
                return False
            
            if word[i] != '.':
                if word[i] not in node.children:
                    return False
                else:
                    node = node.children[word[i]]
                    return dfs(i + 1)
            
            elif word[i] == '.':
                flag = False
                for charNode in node.children.values():
                    oldNode = node
                    node = charNode
                    flag = flag or dfs(i + 1)

                    node = oldNode
                
                return flag
        return dfs(0)

        
