# Square Interview Question — IP Routing Table
#
# We want to design a simple IP Routing Table that can store IP prefixes
# and determine which port an incoming IP address should be routed to,
# based on the **longest prefix match**.
#
# You’ll need to implement two main operations:


# ------------------------------------------------------------
# Part 1 — Basic Binary IP Routing
# ------------------------------------------------------------
# Each IP address and prefix is represented as a binary string (e.g., "010", "1111").
# Each prefix maps to a port number.
#
# Implement two functions:
#
#   insert(ipPrefix: str, port: int) -> None
#       Adds a new prefix–port mapping to the routing table.
#
#   lookup(ip: str) -> int
#       Returns the port associated with the longest matching prefix
#       for the given IP address. If no prefix matches, return -1.
#
# Example:
#   Prefixes:
#       10   → 3
#       010  → 4
#       1111 → 5
#
#   lookup("010110") → 4
#   lookup("111111") → 5
#   lookup("000000") → -1

# ------------------------------------------------------------
# Part 2 — Default Port
# ------------------------------------------------------------
# Add support for a **default port**, which should be returned when
# no prefix matches.
#
# New function:
#   setDefaultPort(port: int) -> None
#
# Example:
#   insert("10", 3)
#   insert("010", 4)
#   insert("1111", 5)
#
#   lookup("000000") → -1
#   setDefaultPort(999)
#   lookup("000000") → 999


class TrieNode:
    def __init__(self):
        self.children = {}
        self.port=None

class RoutingTable:
    def __init__(self):
        self.root = TrieNode()
        self.default_port = -1
    

    def insert(self, isPrefix, port):
        node = self.root

        for bit in isPrefix:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        
        node.port= port 
    
    def setDefaultPort(self,port):
        self.default_port = port

    
    def lookup(self,ip):
        node = self.root
        longest_match = None 

        for bit in ip:
            if bit not in node.children:
                break
            node = node.children[bit]
            if node.port is not None:
                longest_match = node.port 
        if longest_match is not None:
            return longest_match

        else:
            return self.default_port

# ------------------------------------------------------------
# Part 3 — IPv4 Routing (without converting to binary)
# ------------------------------------------------------------
# Extend your routing table to handle **real IPv4-style prefixes**
# (dot-separated strings like "34.126").
#
# For lookups, match on the longest numeric prefix, not just binary bits.
#
# Example:
#   Prefixes:
#       34.126 → 301
#       34.120 → 120
#
#   lookup("34.126.7.1") → 301
#   lookup("34.120.8.1") → 120
#   lookup("192.168.0.1") → -1
#
# ------------------------------------------------------------
# Goal:
#   - Implement the data structure and all operations cleanly.
#   - Ensure correctness and clarity.
#   - Optionally print results or write small test cases.


    def ipv4_insert(self,ipPrefix,port):
        node = self.root

        for part in ipPrefix.split('.'):
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        node.port=port


    def ipv4_lookup(self,ip):
        node = self.root
        longest_match = None 

        for part in ip.split('.'):
            if part not in node.children:
                break
            node = node.children[part]
        
            if node.port is not None:
                longest_match = node.port
        
    
        if longest_match is not None:
            return longest_match
    
        return self.default_port 
    

rt = RoutingTable()
rt.insert("10", 3)
rt.insert("010", 4)
rt.insert("1111", 5)

print(rt.lookup("010110"))  # 4
print(rt.lookup("111111"))  # 5
print(rt.lookup("000000"))  # -1



rt.setDefaultPort(999)
print(rt.lookup("000000"))  # 999 



print("\n--- IPv4 Tests ---")
rt = RoutingTable()
rt.ipv4_insert("34.126", 301)
rt.ipv4_insert("34.120", 120)

print(rt.ipv4_lookup("34.126.7.1"))  # 301 
print(rt.ipv4_lookup("34.120.8.1"))  # 120 
print(rt.ipv4_lookup("192.168.0.1")) # -1 

