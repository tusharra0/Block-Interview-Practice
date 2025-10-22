# ------------------------------------------------------------
# PART 1 — Basic Single-Line Text Editor
# ------------------------------------------------------------
# Design a simple text editor with a cursor that supports:
# 1. Adding text at the cursor position.
# 2. Deleting text to the left of the cursor (backspace behavior).
# 3. Moving the cursor left or right within the text.
#
# Implement the following methods:
#
#   TextEditor()
#       → Initializes the editor with empty text.
#
#   addText(text: str) -> None
#       → Inserts text at the current cursor position.
#
#   deleteText(k: int) -> int
#       → Deletes up to k characters to the left of the cursor.
#         Returns the number of characters actually deleted.
#
#   cursorLeft(k: int) -> str
#   cursorRight(k: int) -> str
#       → Moves the cursor left or right up to k times.
#         Returns the last min(10, len) characters to the left of the cursor.
#
# Example:
#   textEditor = TextEditor()
#   textEditor.addText("leetcode")   # "leetcode|"
#   textEditor.deleteText(4)         # "leet|"
#   textEditor.addText("practice")   # "leetpractice|"
#   textEditor.cursorLeft(8)         # "leet|practice"
#   textEditor.deleteText(10)        # "|practice"
# ------------------------------------------------------------

class TextEditor:

    def __init__(self):
        self.array = []
        self.cursor=0 
    
    def addText(self, text: str) -> None:
        n = len(text) # 4 elements 
        for i in range(len(text)):
            self.array.append(text[i])
        self.cursor = self.cursor+n 

    def deleteText(self, k: int) -> int:
        for i in range(k):
            self.array.pop()
        
        self.cursor = self.cursor - k

    
    def cursorLeft(self, k: int) -> str:
        self.cursor-=k

        for i in range(self.cursor):
            print(self.array[i])
        


    def cursorLeft(self, k: int) -> str:
        # move cursor left but not past start
        self.cursor = max(0, self.cursor - k)
        # return last up to 10 chars to the left of cursor
        start = max(0, self.cursor - 10)
        return ''.join(self.array[start:self.cursor])
        

    def cursorRight(self, k: int) -> str: 
        # move cursor right but not beyond text length
        self.cursor = min(len(self.array), self.cursor + k)
        # return last up to 10 chars to the left of cursor
        start = max(0, self.cursor - 10)
        return ''.join(self.array[start:self.cursor])
    

textEditor = TextEditor()
textEditor.addText("leetcode")
print(textEditor.deleteText(4))      # 4
textEditor.addText("practice")
print(textEditor.cursorRight(3))     # "etpractice"
print(textEditor.cursorLeft(8))      # "leet"
print(textEditor.deleteText(10))     # 4
print(textEditor.cursorLeft(2))      # ""
print(textEditor.cursorRight(6))     # "practi"





# ------------------------------------------------------------
# PART 2 — Multiline Extension
# ------------------------------------------------------------
# Extend your text editor to handle multiple lines of text.
# The text may contain '\n' characters that represent line breaks.
#
# New cursor behavior:
# - The cursor can now move UP or DOWN between lines.
# - If moving up/down to a shorter line, the cursor should land
#   at the end of that line.
#
# Add the following methods:
#
#   cursorUp(k: int) -> None
#   cursorDown(k: int) -> None
#
# Example:
#   addText("hello\nworld")
#   # hello|
#   # world
#   cursorUp(1)
#   addText("hey ")
#   # hey hello|
#   # world
# ------------------------------------------------------------

