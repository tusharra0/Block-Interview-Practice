# ------------------------------------------------------------
# Technical Interview Question — Character Frequency Tree
# ------------------------------------------------------------
# Part 1:
# Given an arbitrary string, build a mapping between each character
# and the number of times that character occurs.
#
# Example:
#   "aabbbbbcDDD"  →  a:2, b:5, c:1, D:3
#
# Part 2:
# Convert that frequency map into a binary tree.
# At each step:
#   - Take the two nodes with the lowest count.
#   - Create a new parent node with:
#         character = "#" (placeholder)
#         count = sum of children’s counts
#   - The left/right children are the two nodes you combined.
# Continue until only one node remains — that’s the root.
#
# Example tree structure:
#
#          (#, 11)
#         /       \
#     (b,5)       (#,6)
#                /     \
#           (D,3)     (#,3)
#                     /   \
#                 (a,2)   (c,1)
#
# Return a pointer to the root node of that tree.
# ------------------------------------------------------------
from collections import Counter 
import heapq

class Node:
    def __init__(self,char,freq):
        self.char = char 
        self.freq = freq 
        self.left = None
        self.right = None 
    
    def __lt__(self,other):
        return self.freq<other.freq


def build_frequency_map(s):
        return Counter(s)
    

def build_tree(s):
    freq_map = build_frequency_map(s)

    heap = []
    for ch,count in freq_map.items():
         heapq.heappush(heap,Node(ch,count))
        
    while len(heap)>1:
         left = heapq.heappop(heap)
         right = heapq.heappop(heap)

         parent = Node("#", left.freq + right.freq)
         parent.left = left 
         parent.right = right

         heapq.heappush(heap,parent)

    return heap[0]


def print_tree(node,indent =0):
    if not node:
        return 
    print(" "*indent + f"{node.char}:{node.freq}")
    print_tree(node.left, indent + 4)
    print_tree(node.right, indent + 4)
if __name__ == "__main__":
    s = "aabbbbbcDDD"
    root = build_tree(s)
    print_tree(root)