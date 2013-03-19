from Tkinter import *
import math
pawn = [200, 200, 240, 200, 270, 230, 270, 270, 240, 300, 240, 320, 250, 420, 270, 460, 280, 470, 300, 470, 310, 480, 310, 490, 310, 500, 210, 500, 180, 500, 140, 500, 140, 480, 150, 470, 170, 470, 190, 420, 200, 300, 170, 270, 170, 230, 200, 200]
rook = [200, 230, 220, 230, 220, 250, 230, 250, 230, 230, 250, 230, 250, 250, 260, 250, 260, 230, 280, 230, 280, 250, 280, 260, 270, 280, 260, 310, 260, 340, 270, 370, 280, 390, 290, 390, 300, 400, 300, 410, 240, 410, 210, 410, 180, 410, 180, 400, 190, 390, 200, 390, 210, 370, 220, 340, 220, 310, 210, 280, 200, 260, 200, 230]
bishop = [200, 160, 210, 160, 220, 160, 230, 170, 230, 190, 220, 200, 230, 210, 240, 230, 250, 250, 250, 290, 240, 310, 230, 330, 230, 370, 240, 380, 250, 380, 260, 390, 260, 400, 210, 400, 160, 400, 160, 390, 170, 380, 180, 380, 190, 370, 190, 330, 180, 310, 170, 290, 170, 250, 180, 230, 190, 210, 200, 200, 190, 190, 190, 170, 200, 160]
knight = [200, 173, 200, 163, 220, 163, 230, 173, 230, 183, 250, 183, 250, 193, 240, 203, 250, 223, 250, 243, 230, 283, 230, 313, 250, 343, 250, 353, 240, 363, 240, 373, 250, 373, 260, 383, 260, 393, 150, 393, 150, 383, 160, 373, 170, 373, 170, 363, 160, 353, 150, 333, 150, 313, 150, 303, 170, 273, 180, 263, 170, 253, 160, 243, 150, 243, 140, 243, 130, 243, 120, 233, 120, 213, 130, 203, 160, 203, 180, 193, 190, 183, 200, 183, 200, 173]
king = [230, 210, 230, 190, 240, 190, 240, 210, 260, 210, 260, 220, 240, 220, 240, 250, 280, 250, 260, 290, 270, 290, 270, 310, 260, 310, 260, 390, 260, 400, 270, 400, 280, 410, 280, 420, 240, 420, 230, 420, 190, 420, 190, 410, 200, 400, 210, 400, 210, 310, 200, 310, 200, 290, 210, 290, 190, 250, 230, 250, 230, 220, 210, 220, 210, 210, 230, 210]
queen = [200, 200, 190, 230, 180, 210, 170, 230, 160, 210, 170, 250, 180, 270, 190, 280, 170, 300, 190, 310, 180, 310, 180, 320, 190, 320, 200, 330, 200, 410, 190, 420, 190, 430, 270, 430, 270, 420, 260, 410, 260, 330, 270, 320, 280, 320, 280, 310, 270, 310, 290, 300, 270, 280, 280, 270, 290, 250, 300, 210, 290, 230, 280, 210, 270, 230, 260, 200, 200,200]
startlist = ['a2','b2','c2','d2','e2','f2','g2','h2','a1','b1','c1','d1','e1','f1','g1','h1','a8','b8','c8','d8','e8','f8','g8','h8','a7','b7','c7','d7','e7','f7','g7','h7']
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

bishop1 = scaler(0.3,bishop)
scaledbishop = bishop1.scalemethod()

knight1 = scaler(0.3,knight)
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
        white = 0
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
    board.move(identifier,-movex,-movey)
    counter = counter + 1
white = 1
black = 0
counter = 1
piecequotes = []
done = False
while done == False:
    if white == 1:
        stringcolor = 'white'
        sput = stringcolor + str(counter)
        if counter >= 9:
            board.move(sput,57,-60)
        else:
            board.move(sput,103,175)
    if black == 1:
        white = 0
        stringcolor = 'black'
        sput = stringcolor + str(counter)
        if counter >= 9:
            board.move(sput,58,30)
        else:
            board.move(sput,110,85)
    if counter == 16 and black == 1:
        done = True
    if counter == 16:
        black = 1
        counter = 0
    piecequotes.append(sput)
    counter = counter + 1
board.move('white1',-100,-180)
bestx = 100
besty = 100

newpiecelist = []
for element in centlist:
    newpiecelist.append(element[0])
coordlist = []
for element in newpiecelist:
    coords = board.coords(element)
    indexer = [element,coords]
    coordlist.append(indexer)
    
def possible(event):
    global selected
    if selected == 0:
        xposit = event.x
        yposit = event.y
        coordlist = []
        for element in newpiecelist:
            coords = board.coords(element)
            indexer = [element,coords]
            coordlist.append(indexer)
        boundarylist = []
        for element in coordlist:
            tag = element[0]
            thingone = element[1]
            alternate = 1
            biggestx = 0
            biggesty = 0
            smallestx = 720
            smallesty = 720
            for element in thingone:
                if alternate == 1:
                    if element > biggestx:
                        biggestx = element
                    if element < smallestx:
                        smallestx = element
                if alternate == -1:
                    if element > biggesty:
                        biggesty = element
                    if element < smallesty:
                        smallesty = element
                alternate = alternate * -1
            boundary = [tag,biggestx,biggesty,smallestx,smallesty]
            boundarylist.append(boundary)
        global xevent
        global yevent
        xevent = event.x
        yevent = event.y
        global xevent1
        global yevent1
        xevent1 = xevent
        yevent1 = yevent
        xconstant = 500
        yconstant = 500 
        for element in squaredata:
            elementx = element[1]
            elementy = element[2]
            if abs(xevent1 - elementx) < xconstant:
                xconstant = abs(xevent1 - elementx)
                xevent = elementx
            if abs(yevent1 - elementy) < yconstant:
                yconstant = abs(yevent1 - elementy)
                yevent = elementy
        #print xevent, yevent

        for element in boundarylist:
            biggestx = element[1]
            biggesty = element[2]
            smallestx = element[3]
            smallesty = element[4]
            if xevent >=smallestx and xevent <= biggestx:
                if yevent >=smallesty and yevent <= biggesty:
                    global best
                    best = element[0]
    if selected != 0:
        #print xevent,yevent
        newxevent = 0
        newyevent = 0
        dispx = 0
        dispy = 0
        rawxmover = 0
        rawymover = 0
        xmover = 0
        ymover = 0
        finalx = 0
        finaly = 0
        newxevent = event.x
        newyevent = event.y
        dispx = newxevent -xevent
        dispy = newyevent -yevent
        rawxmover = dispx/90
        rawymover = dispy/90
        xmover = math.floor(rawxmover)
        ymover = math.floor(rawymover)
        finalx = xmover * 90
        finaly = ymover * 90
        xconstant = 500
        yconstant = 500
        xelement = 0
        yelement = 0
        finaltag = ''
        for element in squaredata:
            squaretag = element[0]
            elementx = element[1]
            elementy = element[2]
            if abs(newxevent - elementx) < xconstant:
                xconstant = abs(newxevent - elementx)
                xelement = elementx
            if abs(newyevent - elementy) < yconstant:
                yconstant = abs(newyevent - elementy)
                yelement = elementy
        for element in squaredata:
            if element[1] == xelement and element[2] == yelement:
                finaltag = element[0]

        xdisp = xelement - xevent
        ydisp = yelement - yevent
        print position
        print selected
        board.move(selected,xdisp,ydisp)
        for element in position:
            if element[0] == selected:
                element[1] = finaltag
        print position
        selected = 0
board.bind('<Button-1>',possible)
while True:
    

    

    if best != 0:
        for element in newpiecelist:
            bwcolor = ''
            tagger = element
            coords = board.coords(tagger)
            board.delete(tagger)
            for char in tagger:
                if char == 'b':
                    bwcolor = 'black'
                    blackturn = 1
                    whiteturn = 0
                if char == 'w':
                    bwcolor = 'white'
                    blackturn = 0
                    whiteturn = 1
            board.create_polygon(coords,tag = tagger,fill = bwcolor)
        coords = board.coords(best)
        board.delete(best)
        board.create_polygon(coords,tag = best,fill = 'green')
        selected = best
        best = 0
        
        
        
    board.update()  
root.mainloop()
