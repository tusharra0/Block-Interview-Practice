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
import heapq

class Node:
    def __init__(self,char,count):
        self.char = char
        self.count = count 
        self.left = None
        self.right = None 
    
    def __lt__(self,other):
        return self.count<other.count 


def build_frequency_map(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch,0)+1
    
    return freq 

