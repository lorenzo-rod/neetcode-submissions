class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
    
        def search_word(root: Node, idx: int) -> bool:
            node = root
            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if search_word(child, i+1):
                            return True
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.is_end
        
        return search_word(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)