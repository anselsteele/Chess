from Tkinter import *
polystring = []
scale = 1
pawn = [200, 200, 240, 200, 270, 230, 270, 270, 240, 300, 240, 320, 250, 420, 270, 460, 280, 470, 300, 470, 310, 480, 310, 490, 310, 500, 210, 500, 180, 500, 140, 500, 140, 480, 150, 470, 170, 470, 190, 420, 200, 300, 170, 270, 170, 230, 200, 200]
rook = [200, 200, 220, 200, 220, 220, 230, 220, 230, 200, 250, 200, 250, 220, 260, 220, 260, 200, 280, 200, 280, 220, 280, 230, 270, 250, 260, 280, 260, 310, 270, 340, 280, 360, 290, 360, 300, 370, 300, 380, 240, 380, 210, 380, 180, 380, 180, 370, 190, 360, 200, 360, 210, 340, 220, 310, 220, 280, 210, 250, 200, 230, 200, 200]
bishop = [200, 200, 210, 200, 220, 210, 220, 220, 210, 230, 220, 240, 230, 260, 230, 290, 220, 310]
knight = [200, 200, 200, 190, 220, 190, 230, 200, 230, 210, 250, 210, 250, 220, 240, 230, 250, 250, 250, 270, 230, 310, 230, 340, 250, 370, 250, 380, 240, 390, 240, 400, 250, 400, 260, 410, 260, 420, 150, 420, 150, 410, 160, 400, 170, 400, 170, 390, 160, 380, 150, 360, 150, 340, 150, 330, 170, 300, 180, 290, 170, 280, 160, 270, 150, 270, 140, 270, 130, 270, 120, 260, 120, 240, 130, 230, 160, 230, 180, 220, 190, 210, 200, 210, 200, 200, 200, 200]
king = [200, 200, 200, 180, 210, 180, 210, 200, 230, 200, 230, 210, 210, 210, 210, 240, 250, 240, 230, 280, 240, 280, 240, 300, 230, 300, 230, 380, 230, 390, 240, 390, 250, 400, 250, 410, 210, 410, 200, 410, 160, 410, 160, 400, 170, 390, 180, 390, 180, 300, 170, 300, 170, 280, 180, 280, 160, 240, 200, 240, 200, 210, 180, 210, 180, 200, 200, 200]
queen = [200, 200, 190, 230, 180, 210, 170, 230, 160, 210, 170, 250, 180, 270, 190, 280, 170, 300, 190, 310, 180, 310, 180, 320, 190, 320, 200, 330, 200, 410, 190, 420, 190, 430, 270, 430, 270, 420, 260, 410, 260, 330, 270, 320, 280, 320, 280, 310, 270, 310, 290, 300, 270, 280, 280, 270, 290, 250, 300, 210, 290, 230, 280, 210, 270, 230, 260, 200, 210, 230, 200,200]
root = Tk()

board = Canvas(root,width =800,height =800)
board.pack()

pawn = board.create_polygon(pawn,tag = 'pawn')
board.move('pawn',100,100)

class scaler:
    def _init_(self,scale,polystring):
       self.polystring = polystring
       self.scale = scale
    def scalemethod(self):
        scalearray1 = []
        limcheck = 0
        center = [501,491]
        xcounter = 0
        ycounter = 1
        loopcounter = 0
        counterlim = len(polystring) - 1
        while loopcounter <= counterlim:
            findx = xcounter
            findy = ycounter
            dispx = polystring[findx] - center[0]
            dispy = polystring1[findy] - center[1]
            scalex = dispx * scale
            scaley = dispy * scale
            newx = center[0] + scalex
            newy = center[1] + scaley
            scalearray1.append(newx)
            scalearray1.append(newy)
            xcounter = xcounter + 2
            ycounter = ycounter + 2
            loopcounter = loopcounter + 2


rook = board.create_polygon(rook,tag = 'rook')
board.move('rook',150,150)
bishop = board.create_polygon(bishop,tag = 'bishop')
board.move('bishop',200,200)
knight = board.create_polygon(knight,tag = 'knight')
board.move('knight',250,250)
king = board.create_polygon(king,tag = 'king')
board.move('king',300,300)
queen = board.create_polygon(queen,tag = 'queen')
board.move('queen',350,350)
root.mainloop()
