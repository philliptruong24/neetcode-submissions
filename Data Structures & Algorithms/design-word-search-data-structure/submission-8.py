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
        def dfs(i, node):
            if i == len(word):
                return node.isWord

            char = word[i]
            if char != '.':
                if char not in node.children:
                    return False
                else:
                    return dfs(i + 1, node.children[char])
            
            elif char == '.':
                flag = False
                for charNode in node.children.values():
                    flag = flag or dfs(i + 1, charNode)

                return flag
        return dfs(0, node)

        
