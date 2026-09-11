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
        def dfs(i, node):
            if i == len(word):
                return node.isWord

            char = word[i]
            if char != '.':
                if char not in node.children:
                    return False
                
                return dfs(i + 1, node.children[char])
            
            elif char == '.':
                for charNode in node.children.values():
                    if dfs(i + 1, charNode):
                        return True

                return False
        return dfs(0, self.root)

        
