from Tkinter import *
polystring = []
scale1 = 1
pawn = [200, 200, 240, 200, 270, 230, 270, 270, 240, 300, 240, 320, 250, 420, 270, 460, 280, 470, 300, 470, 310, 480, 310, 490, 310, 500, 210, 500, 180, 500, 140, 500, 140, 480, 150, 470, 170, 470, 190, 420, 200, 300, 170, 270, 170, 230, 200, 200]
rook = [200, 200, 220, 200, 220, 220, 230, 220, 230, 200, 250, 200, 250, 220, 260, 220, 260, 200, 280, 200, 280, 220, 280, 230, 270, 250, 260, 280, 260, 310, 270, 340, 280, 360, 290, 360, 300, 370, 300, 380, 240, 380, 210, 380, 180, 380, 180, 370, 190, 360, 200, 360, 210, 340, 220, 310, 220, 280, 210, 250, 200, 230, 200, 200]
bishop = [200, 200, 210, 200, 220, 200, 230, 210, 230, 230, 220, 240, 230, 250, 240, 270, 250, 290, 250, 330, 240, 350, 230, 370, 230, 410, 240, 420, 250, 420, 260, 430, 260, 440, 210, 440, 160, 440, 160, 430, 170, 420, 180, 420, 190, 410, 190, 370, 180, 350, 170, 330, 170, 290, 180, 270, 190, 250, 200, 240, 190, 230, 190, 210, 200, 200]
knight = [200, 200, 200, 190, 220, 190, 230, 200, 230, 210, 250, 210, 250, 220, 240, 230, 250, 250, 250, 270, 230, 310, 230, 340, 250, 370, 250, 380, 240, 390, 240, 400, 250, 400, 260, 410, 260, 420, 150, 420, 150, 410, 160, 400, 170, 400, 170, 390, 160, 380, 150, 360, 150, 340, 150, 330, 170, 300, 180, 290, 170, 280, 160, 270, 150, 270, 140, 270, 130, 270, 120, 260, 120, 240, 130, 230, 160, 230, 180, 220, 190, 210, 200, 210, 200, 200,]
king = [200, 200, 200, 180, 210, 180, 210, 200, 230, 200, 230, 210, 210, 210, 210, 240, 250, 240, 230, 280, 240, 280, 240, 300, 230, 300, 230, 380, 230, 390, 240, 390, 250, 400, 250, 410, 210, 410, 200, 410, 160, 410, 160, 400, 170, 390, 180, 390, 180, 300, 170, 300, 170, 280, 180, 280, 160, 240, 200, 240, 200, 210, 180, 210, 180, 200, 200, 200]
queen = [200, 200, 190, 230, 180, 210, 170, 230, 160, 210, 170, 250, 180, 270, 190, 280, 170, 300, 190, 310, 180, 310, 180, 320, 190, 320, 200, 330, 200, 410, 190, 420, 190, 430, 270, 430, 270, 420, 260, 410, 260, 330, 270, 320, 280, 320, 280, 310, 270, 310, 290, 300, 270, 280, 280, 270, 290, 250, 300, 210, 290, 230, 280, 210, 270, 230, 260, 200, 200,200]
root = Tk()

board = Canvas(root,width =720,height =720)
board.pack()


xsquarecounter = 1
ysquarecounter = 1
alternate = 1
while xsquarecounter <=8:
    alternate = alternate * -1
    
    if xsquarecounter == 1:
        letter1 = "a"
    if xsquarecounter == 2:
        letter1 = "b"
    if xsquarecounter == 3:
        letter1 = "c"
    if xsquarecounter == 4:
        letter1 = "d"
    if xsquarecounter == 5:
        letter1 = "e"
    if xsquarecounter == 6:
        letter1 = "f"
    if xsquarecounter == 7:
        letter1 = "g"
    if xsquarecounter == 8:
        letter1 = "h"

    while ysquarecounter <=8:
        alternate = alternate * -1 
        nwcornerx = (xsquarecounter * 90) - 90
        nwcornery = (ysquarecounter * 90) - 90
        secornerx = (xsquarecounter * 90)
        secornery = (ysquarecounter * 90)
        if alternate == 1:
            categorizer = letter1 + str(ysquarecounter)
            board.create_rectangle(nwcornerx,nwcornery,secornerx,secornery,fill = 'red',tag = categorizer)
            vars()[categorizer] = board.coords(categorizer)
        if alternate == -1:
            categorizer = letter1 + str(ysquarecounter)
            board.create_rectangle(nwcornerx,nwcornery,secornerx,secornery,fill = 'blue',tag = categorizer)
            vars()[categorizer] = board.coords(categorizer)
        ysquarecounter = ysquarecounter + 1
    ysquarecounter = 1
    xsquarecounter = xsquarecounter + 1
            
class scaler:
    def __init__(self,scale1,polystring):
       self.polystring = polystring
       self.scale1 = scale1
    def scalemethod(self):
        scalearray1 = []
        limcheck = 0
        center = [501,491]
        xcounter = 0
        ycounter = 1
        loopcounter = 0
        counterlim = len(self.polystring) - 1
        while loopcounter <= counterlim:
            findx = xcounter
            findy = ycounter
            dispx = self.polystring[findx] - center[0]
            dispy = self.polystring[findy] - center[1]
            scalex = dispx * self.scale1
            scaley = dispy * self.scale1
            newx = center[0] + scalex
            newy = center[1] + scaley
            scalearray1.append(newx)
            scalearray1.append(newy)
            xcounter = xcounter + 2
            ycounter = ycounter + 2
            loopcounter = loopcounter + 2
        return scalearray1
            
pawn1 = scaler(0.2,pawn)
scaledpawn = pawn1.scalemethod()

rook1 = scaler(0.35,rook)
scaledrook = rook1.scalemethod()

bishop1 = scaler(0.35,bishop)
scaledbishop = bishop1.scalemethod()

knight1 = scaler(0.35,knight)
scaledknight = knight1.scalemethod()

king1 = scaler(0.35,king)
scaledking = king1.scalemethod()

queen1 = scaler(0.35,queen)
scaledqueen = queen1.scalemethod()

piecelist = []

pawnb1 = board.create_polygon(scaledpawn,tag = 'pawnb1')
piecelist.append(pawnb1)
pawnb2 = board.create_polygon(scaledpawn,tag = 'pawnb2')
piecelist.append(pawnb2)
pawnb3 = board.create_polygon(scaledpawn,tag = 'pawnb3')
piecelist.append(pawnb3)
pawnb4 = board.create_polygon(scaledpawn,tag = 'pawnb4')
piecelist.append(pawnb4)
pawnb5 = board.create_polygon(scaledpawn,tag = 'pawnb5')
piecelist.append(pawnb5)
pawnb6 = board.create_polygon(scaledpawn,tag = 'pawnb6')
piecelist.append(pawnb6)
pawnb7 = board.create_polygon(scaledpawn,tag = 'pawnb7')
piecelist.append(pawnb7)
pawnb8 = board.create_polygon(scaledpawn,tag = 'pawnb8')
piecelist.append(pawnb8)

rookb1 = board.create_polygon(scaledrook,tag = 'rookb1')
piecelist.append(rookb1)
rookb2 = board.create_polygon(scaledrook,tag = 'rookb2')
piecelist.append(rookb2)
bishopb1 = board.create_polygon(scaledbishop,tag = 'bishopb1')
piecelist.append(bishopb1)
bishopb2 = board.create_polygon(scaledbishop,tag = 'bishopb2')
piecelist.append(bishopb2)
knightb1 = board.create_polygon(scaledknight,tag = 'knightb1')
piecelist.append(knightb1)
knightb2 = board.create_polygon(scaledknight,tag = 'knightb2')
piecelist.append(knightb2)
kingb = board.create_polygon(scaledking,tag = 'kingb')
piecelist.append(kingb)
queenb = board.create_polygon(scaledqueen,tag = 'queenb')
piecelist.append(queenb)

pawnw1 = board.create_polygon(scaledpawn,tag = 'pawnw1',fill = 'antique white')
piecelist.append(pawnw1)
pawnw2 = board.create_polygon(scaledpawn,tag = 'pawnw2',fill = 'antique white')
piecelist.append(pawnw2)
pawnw3 = board.create_polygon(scaledpawn,tag = 'pawnw3',fill = 'antique white')
piecelist.append(pawnw3)
pawnw4 = board.create_polygon(scaledpawn,tag = 'pawnw4',fill = 'antique white')
piecelist.append(pawnw4)
pawnw5 = board.create_polygon(scaledpawn,tag = 'pawnw5',fill = 'antique white')
piecelist.append(pawnw5)
pawnw6 = board.create_polygon(scaledpawn,tag = 'pawnw6',fill = 'antique white')
piecelist.append(pawnw6)
pawnw7 = board.create_polygon(scaledpawn,tag = 'pawnw7',fill = 'antique white')
piecelist.append(pawnw7)
pawnw8 = board.create_polygon(scaledpawn,tag = 'pawnw8',fill = 'antique white')
piecelist.append(pawnw8)

rookw1 = board.create_polygon(scaledrook,tag = 'rookw1',fill = 'antique white')
piecelist.append(rookw1)
rookw2 = board.create_polygon(scaledrook,tag = 'rookw2',fill = 'antique white')
piecelist.append(rookw2)
bishopw1 = board.create_polygon(scaledbishop,tag = 'bishopw1',fill = 'antique white')
piecelist.append(bishopw1)
bishopw2 = board.create_polygon(scaledbishop,tag = 'bishopw2',fill = 'antique white')
piecelist.append(bishopw2)
knightw1 = board.create_polygon(scaledknight,tag = 'knightw1',fill = 'antique white')
piecelist.append(knightw1)
knightw2 = board.create_polygon(scaledknight,tag = 'knightw2',fill = 'antique white')
piecelist.append(knightw2)
kingw = board.create_polygon(scaledking,tag = 'kingw',fill = 'antique white')
piecelist.append(kingw)
queenw = board.create_polygon(scaledqueen,tag = 'queenw',fill = 'antique white')
piecelist.append(queenw)

for element in piecelist:
    #unfinished
root.mainloop()


