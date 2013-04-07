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
magician = scaler(0.25,magician1)
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

king = scaler(0.3,king1)
scaledking = king.scalemethod()

queen = scaler(0.2,queen1)
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

startlist = ['a2','b2','c2','d2','e2','f2','g2','h2','i2','j2','k2','l2','m2','n2','o2','p2','a1','b1','c1','d1','e1','f1','g1','h1','i1','j1','k1','l1','m1','n1','o1','p1','a16','b16','c16','d16','e16','f16','g16','h16','i16','j16','k16','l16','m16','n16','o16','p16','a15','b15','c15','d15','e15','f15','g15','h15','i15','j15','k15','l15','m15','n15','o15','p15']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
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
    if xsquarecounter == 9:
        letter1 = 'i'
    if xsquarecounter == 10:
        letter1 = 'j'
    if xsquarecounter == 11:
        letter1 = 'k'
    if xsquarecounter == 12:
        letter1 = 'l'
    if xsquarecounter == 13:
        letter1 = 'm'
    if xsquarecounter == 14:
        letter1 = 'n'
    if xsquarecounter == 15:
        letter1 = 'o'
    if xsquarecounter == 16:
        letter1 = 'p'

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
            square = board.create_rectangle(nwcornerx,nwcornery,secornerx,secornery,fill = 'khaki',tag = identifier)
        if alternate == -1:
            square = board.create_rectangle(nwcornerx,nwcornery,secornerx,secornery,fill = 'slate blue',tag = identifier)
        board.lower(identifier)
        
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
    
board.create_polygon(piecelist[0],tag = 'white1',fill = 'light pink')
board.create_polygon(piecelist[1],tag = 'white2',fill = 'light pink')
board.create_polygon(piecelist[2],tag = 'white3',fill = 'light pink')
board.create_polygon(piecelist[3],tag = 'white4',fill = 'light pink')
board.create_polygon(piecelist[4],tag = 'white5',fill = 'light pink')
board.create_polygon(piecelist[5],tag = 'white6',fill = 'light pink')
board.create_polygon(piecelist[6],tag = 'white7',fill = 'light pink')
board.create_polygon(piecelist[7],tag = 'white8',fill = 'light pink')
board.create_polygon(piecelist[8],tag = 'white9',fill = 'light pink')
board.create_polygon(piecelist[6],tag = 'white10',fill = 'light pink')
board.create_polygon(piecelist[5],tag = 'white11',fill = 'light pink')
board.create_polygon(piecelist[4],tag = 'white12',fill = 'light pink')
board.create_polygon(piecelist[3],tag = 'white13',fill = 'light pink')
board.create_polygon(piecelist[2],tag = 'white14',fill = 'light pink')
board.create_polygon(piecelist[1],tag = 'white15',fill = 'light pink')
board.create_polygon(piecelist[0],tag = 'white16',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white17',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white18',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white19',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white20',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white21',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white22',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white23',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white24',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white25',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white26',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white27',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white28',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white29',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white30',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white31',fill = 'light pink')
board.create_polygon(piecelist[9],tag = 'white32',fill = 'light pink')

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
board.create_polygon(piecelist[9],tag = 'black17',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black18',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black19',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black20',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black21',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black22',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black23',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black24',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black25',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black26',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black27',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black28',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black29',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black30',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black31',fill = 'black')
board.create_polygon(piecelist[9],tag = 'black32',fill = 'black')

whitecentroids = []
blackcentroids = []
counter = 1
while counter <= 32:
    xlist = []
    ylist = []
    name = 'white' + str(counter)
    coordlist = board.coords(name)
    oscillator = 1
    for element in coordlist:
        if oscillator == 1:
            xlist.append(element)
        if oscillator == -1:
            ylist.append(element)
        oscillator = oscillator * -1
    totalx = 0
    for element in xlist:
        totalx = totalx + element
    totaly = 0
    for element in ylist:
        totaly = totaly + element
    avgx = totalx/len(xlist)
    avgy = totaly/len(ylist)
    datapoint = [avgx,avgy]
    whitecentroids.append(datapoint)
    counter = counter +1
counter = 1
while counter <= 32:
    xlist = []
    ylist = []
    name = 'black' + str(counter)
    coordlist = board.coords(name)
    oscillator = 1
    for element in coordlist:
        if oscillator == 1:
            xlist.append(element)
        if oscillator == -1:
            ylist.append(element)
        oscillator = oscillator * -1
    totalx = 0
    for element in xlist:
        totalx = totalx + element
    totaly = 0
    for element in ylist:
        totaly = totaly + element
    avgx = totalx/len(xlist)
    avgy = totaly/len(ylist)
    datapoint = [avgx,avgy]
    blackcentroids.append(datapoint)
    counter = counter + 1
counter = 1
newlist = []
while counter <= 32:
    indexcounter = counter -1
    item1 = 'white' + str(counter)
    wcent = whitecentroids[indexcounter]
    wcentx = wcent[0]
    wcenty = wcent[1]
    squarecent = squaredata[indexcounter]
    squarecentx = squarecent[1]
    squarecenty = squarecent[2]
    dispx = squarecentx - wcentx
    dispy = squarecenty - wcenty
    board.move(item1,dispx,dispy)
    newx = wcentx + dispx
    newy = wcenty + dispy
    newdata = [item1,newx,newy]
    newlist.append(newdata)
    counter = counter + 1
whitecentroids = newlist
newlist = []
counter = 1
while counter <= 32:
    indexcounter = counter - 1
    item1 = 'black' + str(counter)
    wcent = blackcentroids[indexcounter]
    wcentx = wcent[0]
    wcenty = wcent[1]
    sqcount = counter + 223
    squarecent = squaredata[sqcount]
    squarecentx = squarecent[1]
    squarecenty = squarecent[2]
    dispx = squarecentx - wcentx
    dispy = squarecenty - wcenty
    board.move(item1,dispx,dispy)
    newx = wcentx + dispx
    newy = wcenty + dispy 
    newdata = [item1,newx,newy]
    newlist.append(newdata)
    counter = counter + 1
blackcentroids = newlist
newlist = []
counter = 1
while counter <=16:
    indexcounter = counter - 1
    item1= 'black' + str(counter)
    board.move(item1,45,0)
    blackcent = blackcentroids[indexcounter]
    xfix = blackcent[1] + 45
    yfix = blackcent[2]
    fixedcent = [blackcent[0],xfix,yfix]
    newlist.append(fixedcent)
    counter = counter + 1
while counter <=32:
    indexcounter = counter -1
    item1 = 'black' + str(counter)
    board.move(item1,-45,0)
    blackcent = blackcentroids[indexcounter]
    xfix = blackcent[1] - 45
    yfix = blackcent[2]
    fixedcent = [blackcent[0],xfix,yfix]
    newlist.append(fixedcent)
    counter = counter + 1
blackcentroids = newlist


clicked = -1
oldx = 0
oldy = 0

def reposit(event):
    global squaredata
    global clicked
    global selected
    global oldx 
    global oldy
    global whitecentroids
    global blackcentroids
    if clicked == -1:
        selected = ''
        xevent = event.x
        yevent = event.y
        comparex = 100
        comparey = 100
        for element in squaredata:
            xele = element[1]
            yele = element[2]
            if abs(xevent - xele) < comparex:
                comparex = abs(xevent - xele)
                bestx = xele
            if abs(yevent - yele) < comparey:
                comparey = abs(yevent - yele)
                besty = yele
        for element in whitecentroids:
            xcent = element[1]
            ycent = element[2]
            if xcent == bestx and ycent == besty:
                selected = element[0]
                oldx = xcent
                oldy = ycent
  
        for element in blackcentroids:
            xcent = element[1]
            ycent = element[2]
            if xcent == bestx and ycent == besty:
                selected = element[0]
                oldx = xcent
                oldy = ycent
        polycoords = board.coords(selected)
        board.delete(selected)
        board.create_polygon(polycoords,tag = selected,fill = 'blue')


    if clicked == 1 and selected != '':
        xevent = event.x
        yevent = event.y
        comparex = 100
        comparey = 100
        for element in squaredata:
            xele = element[1]
            yele = element[2]
            if abs(xevent - xele) < comparex:
                comparex = abs(xevent - xele)
                bestx = xele
            if abs(yevent - yele) < comparey:
                comparey = abs(yevent - yele)
                besty = yele
        dispx = bestx - oldx
        dispy = besty - oldy
        board.move(selected,dispx,dispy)
        newlist = []
        if selected[0] == 'b':
            for element in blackcentroids:

                if element[0] == selected:
                    datapoint = [element[0],bestx,besty]
                    newlist.append(datapoint)
                else:
                    newlist.append(element)
            blackcentroids = newlist
            fstring = 'black'
        if selected[0] == 'w':
            for element in whitecentroids:
                if element[0] == selected:
                    datapoint = [element[0],bestx,besty]
                    newlist.append(datapoint)
                else:
                    newlist.append(element)
            whitecentroids = newlist
            fstring = 'white'
        polycoords = board.coords(selected)
        board.delete(selected)
        board.create_polygon(polycoords,tag = selected,fill = fstring)




    clicked = clicked * -1
    coordslist = []
    for element in whitecentroids:
        tagger = element[0]
        xele = element[1]
        yele = element[2]
        for item in squaredata:
            sqtag = item[0]
            findx = item[1]
            findy = item[2]

            if findx == xele and findy == yele:
                datapoint = [tagger,sqtag]
                coordslist.append(datapoint)

    for element in blackcentroids:
        tagger = element[0]
        xele = element[1]
        yele = element[2]
        for item in squaredata:
            sqtag = item[0]
            findx = item[1]
            findy = item[2]

            if findx == xele and findy == yele:
                datapoint = [tagger,sqtag]
                coordslist.append(datapoint)
    for element in coordslist:
        if element[0] == selected:
            sqcheck = element[1]
    for element in coordslist:
        if element[0] != selected and element[1] == sqcheck:
            board.delete(element[0])

                              
board.bind('<Button-1>',reposit)
while True:

    board.update()        
    
