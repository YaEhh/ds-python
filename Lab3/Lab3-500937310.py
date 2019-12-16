import operator
import time

class MyHuffman():
    root = ""
    charCodeDict = {}

    def build(self, weights):
        queue = []

        for char,freq in weights.items():
            queue.append(Node(char,freq));

        queue.sort(key=lambda x: x.timestamp, reverse=True)
        queue.sort(key=lambda x: x.value, reverse=True)
        queue.sort(key=lambda x: x.data, reverse=True)

        while len(queue) > 1:
            first_node = queue.pop()
            second_node = queue.pop()

            if (first_node.data == second_node.data):
            # If the frequencies are equal

                # If frequencies are equal AND both are created AND first character is less than the second character - Left first
                if (first_node.value and second_node.value) and (first_node.value < second_node.value):
                    parent_node = Node("", first_node.data + second_node.data, first_node, second_node)

                #   If frequencies are equal AND both are created AND first character is greater than the second character - Right first
                elif (first_node.value and second_node.value) and (first_node.value > second_node.value):
                    parent_node = Node("", first_node.data + second_node.data, second_node, first_node)

                #   If frequencies are equal AND but the first is created - Left first
                elif not first_node.value and second_node.value:
                    parent_node = Node("", first_node.data + second_node.data, first_node, second_node)

                # If frequencies are equal AND the second is created - Right first
                elif first_node.data and not second_node.data:
                    parent_node = Node("", first_node.data + second_node.data, second_node, first_node)

                # If both nodes are created then first created goes left - Left first
                elif not first_node.value and not second_node.value:
                    parent_node = Node("", first_node.data + second_node.data, first_node, second_node)

            # If the frequencies are not equal
            else:

                # If the frequency of the first is less than frequency of the second - Left first
                if first_node.data < second_node.data:
                    parent_node = Node("", first_node.data + second_node.data, first_node, second_node)

                #If the frequncy of the first is greater than frequncy of the second - Right first
                elif first_node.data > second_node.data:
                    parent_node = Node("", first_node.data + second_node.data , second_node, first_node)

                # If the frequencies are not equal and the first is a created node - Left first
                elif first_node.value and second_node.value:
                    parent_node = Node("", first_node.data + second_node.data, first_node, second_node)

                # If the frequencies are not equal and the second is a created node - Right first
                elif first_node.value and not second_node.value:
                    parent_node = Node("", first_node.data + second_node.data , second_node, first_node)

                # If the frequencies are not equal and both are created node - Left first
                elif not first_node.value and not second_node.value:
                    parent_node = Node("", first_node.data + second_node.data, first_node, second_node)
                # If the frequencies are not equal and neither is a created node
                else:
                    parent_node = Node("", first_node.data + second_node.data, first_node, second_node)

            queue.append(parent_node)
            # queue.sort(key=lambda x: x.data, reverse=True)
            queue.sort(key=lambda x: x.timestamp, reverse=True)
            queue.sort(key=lambda x: x.value, reverse=True)
            queue.sort(key=lambda x: x.data, reverse=True)

        self.root = queue.pop()
        return self.root


    def encode(self, word):
        self.charCodeDict = {}
        code = ""
        if self.root:
            self.encoding_helper(self.root, code)
        else:
            return ""

        for char in word:
            if char in self.charCodeDict:
                code = code + self.charCodeDict[char]
            else:
                return ""

        return code

    def encoding_helper(self, root, code):
        if not root.left and not root.right:
            self.charCodeDict[root.value] = code

        if root.left:
            self.encoding_helper(root.left, code + "1")

        if root.right:
            self.encoding_helper(root.right, code + "0")


    def decode(self, bitstring):
        self.charCodeDict = {}
        word = ''
        if self.root:
            self.encoding_helper(self.root, word)
        else:
            return None

        while bitstring:
            for (k,v) in self.charCodeDict.items():
                if bitstring.startswith(v):
                    word += k
                    bitstring = bitstring[len(v):]
                    break

        return word

class Node:
    def __init__(self,value,data,left=None,right=None):
        self.value = value
        self.data = data
        self.left = left
        self.right = right
        self.timestamp = time.time() * 1000


