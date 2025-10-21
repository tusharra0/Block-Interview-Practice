'''
Part 1 — Basic Pairing

You are given a list of socks.
Each sock has two attributes:

Side — either "left" or "right"

Color — a string such as "red", "white", etc.

Your goal is to pair socks such that:

each pair contains one left sock and one right sock, and

both socks have the same color.

Each sock can be used in at most one pair.
Output all valid pairs as tuples of their original indices (1-indexed): (left_sock_index, right_sock_index)

Example:
Input:

left, red,
left, white,
right, white,
right, red,

Output:

(1, 4)
(2, 3)
'''


def basicpairing(socks):
    left = {}
    right = {}
    for i in range(len(socks)):
        if socks[i][0] == "left":
            left[i] = socks[i][1]
        else:
            right[i]=socks[i][1]
    
    
    seen = set()
    for key_1 in left:
        for key_2 in right:
            if right[key_2] == left[key_1] and key_2 not in seen and key_1 not in seen:

                print(left[key_1])
                print(right[key_2])
                seen.add(key_1)
                seen.add(key_2)
    




'''
Part 2 — Acceptable (Cross-Color) Pairing

After forming all exact color pairs, there may still be unpaired socks.
You are given a list of acceptable color combinations, which specify alternative pairings between different colors.

Each combination is written as (color1, color2) meaning a sock of color1 can be paired with a sock of color2 (regardless of which side each is on).

These combinations are given in priority order — pairs should be formed using earlier combinations first.

Rules:

First, pair all exact color matches (as in Part 1).

Then, use the acceptable color combinations (in order) to pair any remaining socks.

Each sock can still only appear in one pair.

Example:
left, blue
right, white
right, black

Acceptable combinations:

(white, blue)
(black, blue)

Output:

(2, 1)

'''


def acceptable(socks):
    left = {}
    right = {}
    for i in range(len(socks)):
        if socks[i][0] == "left":
            left[i] = socks[i][1]
        else:
            right[i]=socks[i][1]
    
    
    seen = set()
    for key_1 in left:
        for key_2 in right:
            if right[key_2] == left[key_1] and key_2 not in seen and key_1 not in seen:

                print(left[key_1])
                print(right[key_2])
                print("----------------------")
                seen.add(key_1)
                seen.add(key_2)
    




    for key_1 in left:
        for key_2 in right:
            if (
                (right[key_2] == "blue" and left[key_1] in ["black", "white"]) or
                (left[key_1] == "blue" and right[key_2] in ["black", "white"])
            ) and key_2 not in seen and key_1 not in seen:
                
                print(f"Acceptable match: ({key_2+1}, {key_1+1})")
                seen.add(key_1)
                seen.add(key_2)

x = [("left","blue"),
     ("right", "white"),
     ("right","black")
     ]


acceptable(x)
