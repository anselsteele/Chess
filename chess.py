from Tkinter import *
pawn = [200, 200, 240, 200, 270, 230, 270, 270, 240, 300, 240, 320, 250, 420, 270, 460, 280, 470, 300, 470, 310, 480, 310, 490, 310, 500, 210, 500, 180, 500, 140, 500, 140, 480, 150, 470, 170, 470, 190, 420, 200, 300, 170, 270, 170, 230, 200, 200]
rook = [200, 200, 220, 200, 220, 220, 230, 220, 230, 200, 250, 200, 250, 220, 260, 220, 260, 200, 280, 200, 280, 220, 280, 230, 270, 250, 260, 280, 260, 310, 270, 340, 280, 360, 290, 360, 300, 370, 300, 380, 240, 380, 210, 380, 180, 380, 180, 370, 190, 360, 200, 360, 210, 340, 220, 310, 220, 280, 210, 250, 200, 230, 200, 200]
bishop = [200, 200, 210, 200, 220, 200, 230, 210, 230, 230, 220, 240, 230, 250, 240, 270, 250, 290, 250, 330, 240, 350, 230, 370, 230, 410, 240, 420, 250, 420, 260, 430, 260, 440, 210, 440, 160, 440, 160, 430, 170, 420, 180, 420, 190, 410, 190, 370, 180, 350, 170, 330, 170, 290, 180, 270, 190, 250, 200, 240, 190, 230, 190, 210, 200, 200]
knight = [200, 200, 200, 190, 220, 190, 230, 200, 230, 210, 250, 210, 250, 220, 240, 230, 250, 250, 250, 270, 230, 310, 230, 340, 250, 370, 250, 380, 240, 390, 240, 400, 250, 400, 260, 410, 260, 420, 150, 420, 150, 410, 160, 400, 170, 400, 170, 390, 160, 380, 150, 360, 150, 340, 150, 330, 170, 300, 180, 290, 170, 280, 160, 270, 150, 270, 140, 270, 130, 270, 120, 260, 120, 240, 130, 230, 160, 230, 180, 220, 190, 210, 200, 210, 200, 200,]
king = [200, 200, 200, 180, 210, 180, 210, 200, 230, 200, 230, 210, 210, 210, 210, 240, 250, 240, 230, 280, 240, 280, 240, 300, 230, 300, 230, 380, 230, 390, 240, 390, 250, 400, 250, 410, 210, 410, 200, 410, 160, 410, 160, 400, 170, 390, 180, 390, 180, 300, 170, 300, 170, 280, 180, 280, 160, 240, 200, 240, 200, 210, 180, 210, 180, 200, 200, 200]
queen = [200, 200, 190, 230, 180, 210, 170, 230, 160, 210, 170, 250, 180, 270, 190, 280, 170, 300, 190, 310, 180, 310, 180, 320, 190, 320, 200, 330, 200, 410, 190, 420, 190, 430, 270, 430, 270, 420, 260, 410, 260, 330, 270, 320, 280, 320, 280, 310, 270, 310, 290, 300, 270, 280, 280, 270, 290, 250, 300, 210, 290, 230, 280, 210, 270, 230, 260, 200, 200,200]
startlist = ['a1','b1','c1','d1','e1','f1','g1','h1','a2','b2','c2','d2','e2','f2','g2','h2','a8','b8','c8','d8','e8','f8','g8','h8','a7','b7','c7','d7','e7','f7','g7','h7']
root = Tk()
board = Canvas(root,width = 720,height = 720)
board.pack()

xsquarecounter = 1
ysquarecounter = 1
alternate = 1
squaredata = []

while xsquarecounter <=8:
    alternate = alternate * -1
    
    if xsquarecounter == 1:
        letter1 = 'a'
    if xsquarecounter == 2:
        letter1 = 'b'
    if xsquarecounter == 3:
        letter1 = 'c'
    if xsquarecounter == 4:
        letter1 = 'd'
    if xsquarecounter == 5:
        letter1 = 'e'
    if xsquarecounter == 6:
        letter1 = 'f'
    if xsquarecounter == 7:
        letter1 = 'g'
    if xsquarecounter == 8:
        letter1 = 'h'
    while ysquarecounter <=8:
        alternate = alternate * -1
        #corners of the square
        nwcornerx = (xsquarecounter * 90) - 90
        nwcornery = (ysquarecounter * 90) - 90
        secornerx = (xsquarecounter * 90)
        secornery = (ysquarecounter * 90)
        
        identifier = letter1 + str(ysquarecounter)
        xavg = (nwcornerx + secornerx)/2
        yavg = (nwcornery + secornery)/2
        datapoint = [identifier,xavg,yavg]
        
        if alternate == 1:
            square = board.create_rectangle(nwcornerx,nwcornery,secornerx,secornery,fill = 'red',tag = identifier)
        if alternate == -1:
            square = board.create_rectangle(nwcornerx,nwcornery,secornerx,secornery,fill = 'blue',tag = identifier)
        
        squaredata.append(datapoint)
        ysquarecounter = ysquarecounter+1
    ysquarecounter = 1
    xsquarecounter = xsquarecounter + 1
#print squaredata

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

rookw1 = board.create_polygon(scaledrook,tag = 'white1',fill = 'antique white')
piecelist.append(rookw1)
knightw1 = board.create_polygon(scaledknight,tag = 'white2',fill = 'antique white')
piecelist.append(knightw1)
bishopw1 = board.create_polygon(scaledbishop,tag = 'white3',fill = 'antique white')
piecelist.append(bishopw1)
queenw = board.create_polygon(scaledqueen,tag = 'white4',fill = 'antique white')
piecelist.append(queenw)
kingw = board.create_polygon(scaledking,tag = 'white5',fill = 'antique white')
piecelist.append(kingw)
bishopw2 = board.create_polygon(scaledbishop,tag = 'white6',fill = 'antique white')
piecelist.append(bishopw2)
knightw2 = board.create_polygon(scaledknight,tag = 'white7',fill = 'antique white')
piecelist.append(knightw2)
rookw2 = board.create_polygon(scaledrook,tag = 'white8',fill = 'antique white')
piecelist.append(rookw2)

pawnw1 = board.create_polygon(scaledpawn,tag = 'white9',fill = 'antique white')
piecelist.append(pawnw1)
pawnw2 = board.create_polygon(scaledpawn,tag = 'white10',fill = 'antique white')
piecelist.append(pawnw2)
pawnw3 = board.create_polygon(scaledpawn,tag = 'white11',fill = 'antique white')
piecelist.append(pawnw3)
pawnw4 = board.create_polygon(scaledpawn,tag = 'white12',fill = 'antique white')
piecelist.append(pawnw4)
pawnw5 = board.create_polygon(scaledpawn,tag = 'white13',fill = 'antique white')
piecelist.append(pawnw5)
pawnw6 = board.create_polygon(scaledpawn,tag = 'white14',fill = 'antique white')
piecelist.append(pawnw6)
pawnw7 = board.create_polygon(scaledpawn,tag = 'white15',fill = 'antique white')
piecelist.append(pawnw7)
pawnw8 = board.create_polygon(scaledpawn,tag = 'white16',fill = 'antique white')
piecelist.append(pawnw8)

rookb1 = board.create_polygon(scaledrook,tag = 'black1')
piecelist.append(rookb1)
knightb1 = board.create_polygon(scaledknight,tag = 'black2')
piecelist.append(knightb1)
bishopb1 = board.create_polygon(scaledbishop,tag = 'black3')
piecelist.append(bishopb1)
queenb = board.create_polygon(scaledqueen,tag = 'black4')
piecelist.append(queenb)
kingb = board.create_polygon(scaledking,tag = 'black5')
piecelist.append(kingb)
bishopb2 = board.create_polygon(scaledbishop,tag = 'black6')
piecelist.append(bishopb2)
knightb2 = board.create_polygon(scaledknight,tag = 'black7')
piecelist.append(knightb2)
rookb2 = board.create_polygon(scaledrook,tag = 'black8')
piecelist.append(rookb2)

pawnb1 = board.create_polygon(scaledpawn,tag = 'black9')
piecelist.append(pawnb1)
pawnb2 = board.create_polygon(scaledpawn,tag = 'black10')
piecelist.append(pawnb2)
pawnb3 = board.create_polygon(scaledpawn,tag = 'black11')
piecelist.append(pawnb3)
pawnb4 = board.create_polygon(scaledpawn,tag = 'black12')
piecelist.append(pawnb4)
pawnb5 = board.create_polygon(scaledpawn,tag = 'black13')
piecelist.append(pawnb5)
pawnb6 = board.create_polygon(scaledpawn,tag = 'black14')
piecelist.append(pawnb6)
pawnb7 = board.create_polygon(scaledpawn,tag = 'black15')
piecelist.append(pawnb7)
pawnb8 = board.create_polygon(scaledpawn,tag = 'black16')
piecelist.append(pawnb8)

centlist = []
white = 1
black = 0
counter = 0
for element in piecelist:
    
    if white == 1:
        colorstring = 'white'
    if black == 1:
        colorstring = 'black'
    if counter == 16:
        black = 1
        colorstring = 'black'
        counter = 0
    counter = counter + 1
    fullstring = colorstring + str(counter)
    
    coords = board.coords(fullstring)
    alternate = 1
    xcent = 0
    ycent = 0
    divisor = 1
    for element in coords:
        if alternate == 1:
            xcent = xcent + element
        if alternate == -1:
            ycent = ycent + element
        alternate = alternate * -1
        divisor = divisor + 1
    finalx = xcent/divisor
    finaly = ycent/divisor
    finalcent = [fullstring,finalx,finaly]
    centlist.append(finalcent)
centroidlist = []    
counter = 1
newlist = []
for element in startlist:
    for thing in squaredata:
        if thing[0] == element:
            newlist.append(thing)
print newlist
counter = 0          
for element in centlist:
    identifier = element[0]
    centroidx = element[1]
    centroidy = element[2]
    datapoint = newlist[counter]
    data = datapoint[0]
    datax = datapoint[1]
    datay = datapoint[2]
    differencex = datax - centroidx
    differencey = datay - centroidy
    differences = [differencex,differencey]
    centroidlist.append(differences)
    counter = counter + 1
counter = 0
for element in centlist:
    identifier = element[0]
    unpack = centroidlist[counter]
    movex = unpack[0]
    movey = unpack[1]
    board.move(identifier,movex,movey)
    counter = counter + 1

root.mainloop()



        



