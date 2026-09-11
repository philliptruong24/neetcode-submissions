class Node:
    def __init__(self):
        self.children = {} 
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        lastNode = self.root

        for i in range(len(word)):
            if word[i] not in lastNode.children:
                lastNode.children[word[i]] = Node()
            lastNode = lastNode.children[word[i]]

        lastNode.isWord = True

    def search(self, word: str) -> bool:
        lastNode = self.root
        for i in range(len(word)):
            if word[i] not in lastNode.children:
                return False
            else:
                lastNode = lastNode.children[word[i]]

        return lastNode.isWord

    def startsWith(self, prefix: str) -> bool:
        lastNode = self.root
        for i in range(len(prefix)):
            if prefix[i] not in lastNode.children:
                return False
            else:
                lastNode = lastNode.children[prefix[i]]

        return True

        
        