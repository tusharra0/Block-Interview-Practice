class Canvas:

    def __init__(self,rows = 10, cols = 15):
        self.rows = rows 
        self.cols = cols 
        self.grid = []

        for r in range(rows):
            row=[]
            for c in range(cols):
                row.append('0')
            self.grid.append(row)

    def blank_canvas(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append('O')
            self.grid.append(row)
    
    def show_canvas(self):
        for row in self.grid:
            print(''.join(row))


    def set_pixel(self,x,y,char="X"):
        if 0<=x<self.cols and 0<=y<self.rows:
            self.grid[x][y] = char


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self,canvas):
        pass

class Point(Shape):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self,canvas):
        canvas.set_pixel(self.x,self.y)

class Line(Shape):
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1 
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def draw(self,canvas):
        if self.x1 == self.x2:
            for i in range(min(self.y1,self.y2),max(self.y1,self.y2)+1):
                canvas.set_pixel(self.x1,i)
        elif self.y1 == self.y2:
            for i in range(min(self.x1,self.x2),max(self.x1,self.x2)+1):
                canvas.set_pixel(i,self.y1)

class Rectangle(Shape):
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1 
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def draw(self,canvas):
        Line(self.x1,self.y1,self.x2,self.y1).draw(canvas)
        Line(self.x1,self.y2,self.x2,self.y2).draw(canvas)
        Line(self.x1,self.y1,self.x1,self.y2).draw(canvas)
        Line(self.x2,self.y1,self.x2,self.y2).draw(canvas)
        


if __name__ == "__main__":
    canvas= Canvas(10,15)
    p = Point(2,3)
    p.draw(canvas)

    l1 = Line(0, 0, 5, 0)
    l1.draw(canvas)

    l2 = Line(0, 0, 0, 5)
    l2.draw(canvas)

    rect = Rectangle(1, 1, 4, 4)
    rect.draw(canvas)

    canvas.show_canvas()






