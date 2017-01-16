from rectangle import Rectangle
import turtle

class Square(Rectangle):

    def __init__(self,side):

        super(Square,self).__init__(side, side)

        if side>=0 :
            self.side=side
        else :
            self.side=0

        
s = Square(100)
