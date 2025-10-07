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
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def draw(self, canvas):
        print("Inside draw")
        # vertical
        if self.x1 == self.x2:
            for i in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                canvas.set_pixel(self.x1, i)
        
        # horizontal
        elif self.y1 == self.y2:
            for i in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                canvas.set_pixel(i, self.y1)
        
        # diagonal
        else:
            print("inside diag")
            x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2

            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1

            dx = x2 - x1
            dy = y2 - y1
            

            slope = dy/dx

            print("before abs(slop ==1)")
            if abs(slope)==1:
                print("before x1>x2")

                x_step = 1 if x2 > x1 else -1
                y =y1

                print("before for loop")
                for x in range(x1,x2+x_step,x_step):
                    print("Inside the line forloop")
                    canvas.set_pixel(x,y)
                    y+=1
            else:
                print(f"Unsupported slope {slope}")
                


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

    l2 = Line(3, 5, 6, 2)
    l2.draw(canvas)
    canvas.show_canvas()





