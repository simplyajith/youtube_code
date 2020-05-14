"""
Basics:

As words gets added, each character in word starts from index 0 is subchildren of root *
index1 will be child of index 0 character and at the end of the last character,make the word complete
by setting a boolean variable, isWord = True.

So a Trie node should contain
self.char = each character
self.children = {character(key): TrieNode(value)}
self.isWord = False(default)

Trie starts  with * as root.

"""

class  TrieNode:
    def __init__(self,char):
        self.char = char
        self.isWord =False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("*")

    def insert(self,word):
        current = self.root

        for char in word:
            if char in current.children:
                current = current.children[char]
            else:

                current.children[char] = TrieNode(char)
                current = current.children[char]

        current.isWord =True

    def search(self, word):
        current =self.root

        for char in word:
            if char in current.children:
                print(current.children)
                current = current.children[char]
            else:
                return False

        if current.isWord:
            return True
        else:
            return False

    def startswith(self, pre):
        prefix = True
        current = self.root
        for char in pre:
            if char not in current.children:
                prefix = False
                return prefix
        return prefix







x = Trie()
x.insert("abc")
x.insert("bc")
x.insert("cat")
# print(x.root.children)
print(x.search("abc"))
# print(x.search("cat"))
# print(x.search("ca"))


