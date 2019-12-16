class Node:
    def __init__(self):
        self.charRefDict = {}
        self.endOfWordFlg = False

class MyTrie:
    def __init__(self):
        # Initialize the trie node as needed
        self.root_node = Node()
        self.words = []
        self.inserted_words = []

    def insert(self, word):
        # Insert a word into this trie node
        self.insert_helper(self.root_node, word, 0)

    def insert_helper(self, root, word, idx):
        if idx == len(word):
            root.endOfWordFlg = True
            self.inserted_words.append(word)
            return

        char = word[idx]
        child_node = root.charRefDict.get(char)

        if not child_node:
            child_node = Node()
            root.charRefDict[char] = child_node

        self.insert_helper(child_node, word, idx + 1)

    def exists(self, word, position=0):
        # Return true if the passed word exists in this trie node
        # A terminal node will return true if the word passed is ""

        current_node = self.root_node
        found = True

        for char in word:
            if not current_node.charRefDict.get(char):
                found = False
                break

            current_node = current_node.charRefDict[char]

        return current_node and current_node.endOfWordFlg and found

    def isTerminal(self):
        if not self.root_node.endOfWordFlg:
            return True
        else:
            return False

    def returnWordStartingWith(self, root, word):
        if root.endOfWordFlg:
            self.words.append(word)

        for k, v in root.charRefDict.items():
            self.returnWordStartingWith(v, word + k)

    def autoComplete(self, prefix, position=0):


        # Return every word that extends this prefix in alphabetical order
        self.words = []
        current_node = self.root_node
        not_found = False
        word = ''

        # Check to see if each character in the prefix is linked to each other
        for char in prefix:
            if not current_node.charRefDict.get(char):
                not_found = True
                return []

            word += char
            current_node = current_node.charRefDict[char]

        if not_found:
            return 0
        elif current_node.endOfWordFlg and not current_node.charRefDict:
            return -1


        # Recursive Call
        self.returnWordStartingWith(current_node, word)

        if self.words:
            return self.words
        else:
            return []

    def __len__(self):
        print(f'Length of inserted words is {len(self.inserted_words)}')
        return len(self.inserted_words)