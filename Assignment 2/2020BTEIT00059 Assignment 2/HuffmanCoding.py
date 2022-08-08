# Ankur Singh
# CA Assignment 2
# PRN -> 2020BTEIT00059

# Code for Huffman Compression.

from ctypes.wintypes import PSIZE
from multiprocessing.spawn import old_main_modules
from xml.dom.minicompat import NodeList
from PIL import Image

# A Huffman Tree Node.
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

        # Tree Direction. (0/1)
        self.huff = ''

class pixel_node:
    # Node construction Method.
    def __init__(self, right=None, left=None, parent=None, weight=0, code=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.weight = weight
        self.code = code

def printNodes(node, val=''):
    # Huffman code for current node.
    newVal = val + str(node.huff)

    # if node is not ans edge node then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)

    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")

# Characters for hufmann tree.
chars = ['a', 'b', 'c', 'd', 'e', 'f']

# Frequency of characters.
freq = [5, 9, 12, 13, 16, 45]

# List containing unused nodes
nodes = []

# Converting characters and frequencies into huffman tree nodes
for x in range(len(chars)):
    nodes.append(Node(freq[x], chars[x]))

while(len(nodes) > 1):
    # Sort all the nodes in ascending order based on their frequency.
    nodes = sorted(nodes, key=lambda x: x.freq)

    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]

    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # Combine the 2 smallest node to create new node as their parent.
    newNode = Node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    # Remove the 2 nodes and add their parent as new node among others.
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

printNodes(nodes[0])

def pixel_frequency(pxl_lst):
    pxl_freq = {}
    for i in pxl_lst:
        if i not in pxl_freq.keys():
            pxl_freq[i] = 1
        else:
            pxl_freq[i] += 1
        
    return pxl_freq

def construct_node(pixel):
    node_lst = []
    for i in range(len(pixel)):
        node_lst.append(pixel_node(weight=pixel[i][1], code=str(pixel[i][0])))
    
    return node_lst

def construct_tree(node_lst):
    node_lst = sorted(node_lst, key=lambda pixel_node: pixel_node.weight)

    while(len(node_lst) != 1):
        # 0 is left, 1 is right
        node0 = node_lst[0]
        node1 = node_lst[1]
        merge_node = pixel_node(left=node0, right=node1, weight=node0.weight+node1.weight)
        node0.parent = merge_node
        node1.parent = merge_node
        node_lst.remove(node0)
        node_lst.remove(node1)
        node_lst.append(merge_node)
        node_lst = sorted(node_lst, key=lambda pixel_node:pixel_node.weight)
    
    return node_lst


def huffman_encoding(img):
    width = img.size[0]
    height = img.size[1]
    im = img.load()
    pixel_lst = []
    for i in range(width):
        for j in range(height):
            pixel_lst.append(im[i, j])
        
    pixel_freq = pixel_frequency(pixel_lst)
    pixel_freq = sorted(pixel_freq.items(), key=lambda item:item[1])

    node_lst = construct_node(pixel_freq)
    huff_tree_head = construct_tree(node_lst)[0]
    encoding_table = {}

    for x in node_lst:
        currNode = x
        encoding_table.setdefault(x.code, "")
        while(currNode != huff_tree_head):
            if(currNode.parent.left == currNode):
                encoding_table[x.code] = "1"+encoding_table[x.code]
            else:
                encoding_table[x.code] = "0"+encoding_table[x.code]
            currNode = currNode.parent
    
    for key in encoding_table.keys():
        print("Source Pixel: "+ key +"\nCode strength after encoding:"+ encoding_table[key])

    print("Encoding Table: ", encoding_table)

if __name__ == '__main__':
    img = Image.open('Compressed.png')
    g_img = img.convert('L')
    huffman_encoding(g_img)