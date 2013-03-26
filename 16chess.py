from Tkinter import *
import math
piecelist = []
newlist = []
bestlist = []

magician1 = [200, 200, 220, 200, 230, 200, 230, 230, 220, 230, 220, 240, 230, 270, 240, 270, 240, 280, 190, 280, 190, 270, 200, 270, 210, 240, 210, 230, 200, 230, 200, 200]
pawn1 = [200, 200, 220, 200, 230, 210, 230, 230, 220, 240, 200, 240, 190, 230, 190, 210, 200, 200]
berzerker1 = [200, 200, 200, 190, 220, 190, 220, 200, 230, 210, 240, 210, 240, 230, 230, 230, 220, 240, 220, 250, 200, 250, 200, 240, 190, 230, 180, 230, 180, 210, 190, 210, 200, 200]
rook1 = [200, 200, 190, 200, 190, 180, 200, 180, 200, 190, 210, 190, 210, 180, 220, 180, 220, 190, 230, 190, 230, 180, 240, 180, 240, 200, 230, 200, 230, 220, 220, 220, 220, 230, 230, 260, 240, 260, 240, 270, 190, 270, 190, 260, 200, 260, 210, 230, 210, 220, 200, 220, 200, 200]
bishop1 = [200, 200, 190, 190, 190, 170, 200, 150, 210, 150, 220, 170, 220, 190, 210, 200, 220, 230, 230, 230, 230, 240, 180, 240, 180, 230, 190, 230, 200, 200]
knight1 = [200, 200, 200, 180, 200, 170, 230, 170, 250, 170, 250, 190, 230, 190, 230, 200, 220, 210, 230, 240, 240, 240, 240, 250, 190, 250, 190, 240, 200, 240, 210, 210, 200, 200]
king1 = [200, 200, 200, 170, 210, 170, 210, 160, 200, 160, 200, 150, 210, 150, 210, 140, 220, 140, 220, 150, 230, 150, 230, 160, 220, 160, 220, 170, 230, 170, 230, 200, 220, 200, 220, 210, 230, 240, 240, 240, 240, 250, 190, 250, 190, 240, 200, 240, 210, 210, 210, 200, 200, 200]
queen1 = [200, 200, 190, 180, 210, 190, 220, 170, 230, 190, 250, 180, 240, 200, 240, 220, 230, 230, 240, 270, 250, 270, 250, 280, 190, 280, 190, 270, 200, 270, 210, 230, 200, 220, 200, 200]
vanguard1 = [200, 200, 190, 190, 180, 170, 180, 160, 190, 160, 190, 170, 200, 190, 210, 200, 220, 190, 230, 170, 230, 160, 240, 160, 240, 170, 230, 190, 220, 200, 230, 200, 230, 230, 220, 230, 220, 240, 230, 280, 240, 280, 240, 290, 180, 290, 180, 280, 190, 280, 200, 240, 200, 230, 190, 230, 190, 200, 200, 200]
crusader1 = [200, 200, 200, 190, 190, 190, 180, 190, 180, 160, 170, 160, 170, 150, 190, 150, 190, 180, 200, 180, 200, 170, 230, 170, 230, 180, 240, 180, 240, 150, 260, 150, 260, 160, 250, 160, 250, 190, 230, 190, 230, 200, 220, 210, 230, 250, 240, 250, 240, 260, 190, 260, 190, 250, 200, 250, 210, 210, 200, 200]

print pawn1
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
magician = scaler(2,magician1)
scaledmagician = magician.scalemethod()
            
pawn = scaler(0.25,pawn1)
scaledpawn = pawn.scalemethod()

berzerker = scaler(0.25,berzerker1)
scaledberzerker = berzerker.scalemethod()

rook = scaler(0.25,rook1)
scaledrook = rook.scalemethod()

vanguard = scaler(0.25,vanguard1)
scaledvanguard = vanguard.scalemethod()

bishop = scaler(0.25,bishop1)
scaledbishop = bishop.scalemethod()

knight = scaler(0.25,knight1)
scaledknight = knight.scalemethod()

king = scaler(0.25,king1)
scaledking = king.scalemethod()

queen = scaler(0.25,queen1)
scaledqueen = queen.scalemethod()

crusader = scaler(0.25,crusader1)
scaledcrusader = crusader.scalemethod()

piecelist.append(scaledmagician)
piecelist.append(scaledrook)
piecelist.append(scaledknight)
piecelist.append(scaledvanguard)
piecelist.append(scaledcrusader)
piecelist.append(scaledbishop)
piecelist.append(scaledbishop)
piecelist.append(scaledqueen)
piecelist.append(scaledking)
piecelist.append(scaledpawn)

startlist = ['a2','b2','c2','d2','e2','f2','g2','h2','a1','b1','c1','d1','e1','f1','g1','h1','a8','b8','c8','d8','e8','f8','g8','h8','a7','b7','c7','d7','e7','f7','g7','h7']
letters = ['a','b','c','d','e','f','g','h']
root = Tk()
board = Canvas(root,width = 720,height = 720)

board.pack()

position = [['white1','a1'],['white2','b1'],['white3','c1'],['white4','d1'],['white5','e1'],['white6','f1'],['white7','g1'],['white8','h1'],['white9','a2'],['white10','b2'],['white11','c2'],['white12','d2'],['white13','e2'],['white14','f2'],['white15','g2'],['white16','h2'],['black1','a8'],['black2','b8'],['black3','c8'],['black4','d8'],['black5','e8'],['black6','f8'],['black7','g8'],['black8','h8'],['black9','a7'],['black10','b7'],['black11','c7'],['black12','d7'],['black13','e7'],['black14','f7'],['black15','g7'],['black16','h7']]
xsquarecounter = 1
ysquarecounter = 1
alternate = 1
squaredata = []
best = 0
whiteturn = 1
blackturn = 0
selected = 0
xevent = 0
yevent = 0
xevent1 = 0
yevent1 = 0
moverange = []




while xsquarecounter <=16:
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
    while ysquarecounter <=16:
        alternate = alternate * -1
        #corners of the square
        nwcornerx = (xsquarecounter * 45) - 45
        nwcornery = (ysquarecounter * 45) - 45
        secornerx = (xsquarecounter * 45)
        secornery = (ysquarecounter * 45)
        
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
#for element in piecelist:
 #   newlist = []
  #  for coordinate in element:
   #     newcoordinate = coordinate - 200
    #    newlist.append(newcoordinate)
    #bestlist.append(newlist)
    
board.create_polygon(piecelist[0],tag = 'white1',fill = 'white')
board.create_polygon(piecelist[1],tag = 'white2',fill = 'white')
board.create_polygon(piecelist[2],tag = 'white3',fill = 'white')
board.create_polygon(piecelist[3],tag = 'white4',fill = 'white')
board.create_polygon(piecelist[4],tag = 'white5',fill = 'white')
board.create_polygon(piecelist[5],tag = 'white6',fill = 'white')
board.create_polygon(piecelist[6],tag = 'white7',fill = 'white')
board.create_polygon(piecelist[7],tag = 'white8',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white9',fill = 'white')
board.create_polygon(piecelist[6],tag = 'white10',fill = 'white')
board.create_polygon(piecelist[5],tag = 'white11',fill = 'white')
board.create_polygon(piecelist[4],tag = 'white12',fill = 'white')
board.create_polygon(piecelist[3],tag = 'white13',fill = 'white')
board.create_polygon(piecelist[2],tag = 'white14',fill = 'white')
board.create_polygon(piecelist[1],tag = 'white15',fill = 'white')
board.create_polygon(piecelist[0],tag = 'white16',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white17',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white18',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white19',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white20',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white21',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white22',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white23',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white24',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white25',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white26',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white27',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white28',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white29',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white30',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white31',fill = 'white')
board.create_polygon(piecelist[8],tag = 'white32',fill = 'white')

board.create_polygon(piecelist[0],tag = 'black1',fill = 'black')
board.create_polygon(piecelist[1],tag = 'black2',fill = 'black')
board.create_polygon(piecelist[2],tag = 'black3',fill = 'black')
board.create_polygon(piecelist[3],tag = 'black4',fill = 'black')
board.create_polygon(piecelist[4],tag = 'black5',fill = 'black')
board.create_polygon(piecelist[5],tag = 'black6',fill = 'black')
board.create_polygon(piecelist[6],tag = 'black7',fill = 'black')
board.create_polygon(piecelist[7],tag = 'black8',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black9',fill = 'black')
board.create_polygon(piecelist[6],tag = 'black10',fill = 'black')
board.create_polygon(piecelist[5],tag = 'black11',fill = 'black')
board.create_polygon(piecelist[4],tag = 'black12',fill = 'black')
board.create_polygon(piecelist[3],tag = 'black13',fill = 'black')
board.create_polygon(piecelist[2],tag = 'black14',fill = 'black')
board.create_polygon(piecelist[1],tag = 'black15',fill = 'black')
board.create_polygon(piecelist[0],tag = 'black16',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black17',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black18',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black19',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black20',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black21',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black22',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black23',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black24',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black25',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black26',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black27',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black28',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black29',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black30',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black31',fill = 'black')
board.create_polygon(piecelist[8],tag = 'black32',fill = 'black')
print board.coords('black32')
root.mainloop()
