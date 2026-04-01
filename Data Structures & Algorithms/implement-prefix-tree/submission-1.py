class TreeNode:
    def __init__(self, children: dict, end: bool):
        self.children = children
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = TreeNode(children={}, end=False)

    def insert(self, word: str) -> None:
        curr = self.root
        for i,c in enumerate(word):
            #check if the letter is present in root
            if c in curr.children: # go into that subtree
                curr = curr.children[c]
                if i == len(word)-1:
                    curr.end = True
            else:
                end = i == len(word)-1
                newNode = TreeNode({}, end)
                curr.children[c] = newNode
                curr = newNode

    def search(self, word: str) -> bool:
        curr = self.root
        for i,c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
                if i == len(word)-1 and curr.end:
                    return True
            else:
                return False

        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i,c in enumerate(prefix):
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False

        return True
        