from Tkinter import *
import math

magician = [200, 200, 220, 200, 230, 200, 230, 230, 220, 230, 220, 240, 230, 270, 240, 270, 240, 280, 190, 280, 190, 270, 200, 270, 210, 240, 210, 230, 200, 230, 200, 200]

pawn = [200, 200, 220, 200, 230, 210, 230, 230, 220, 240, 200, 240, 190, 230, 190, 210, 200, 200]
berzerker = [200, 200, 200, 190, 220, 190, 220, 200, 230, 210, 240, 210, 240, 230, 230, 230, 220, 240, 220, 250, 200, 250, 200, 240, 190, 230, 180, 230, 180, 210, 190, 210, 200, 200]

rook = [200, 200, 190, 200, 190, 180, 200, 180, 200, 190, 210, 190, 210, 180, 220, 180, 220, 190, 230, 190, 230, 180, 240, 180, 240, 200, 230, 200, 230, 220, 220, 220, 220, 230, 230, 260, 240, 260, 240, 270, 190, 270, 190, 260, 200, 260, 210, 230, 210, 220, 200, 220, 200, 200]
bishop = [200, 200, 190, 190, 190, 170, 200, 150, 210, 150, 220, 170, 220, 190, 210, 200, 220, 230, 230, 230, 230, 240, 180, 240, 180, 230, 190, 230, 200, 200]
knight = [200, 200, 200, 180, 200, 170, 230, 170, 250, 170, 250, 190, 230, 190, 230, 200, 220, 210, 230, 240, 240, 240, 240, 250, 190, 250, 190, 240, 200, 240, 210, 210, 200, 200]
king = [200, 200, 200, 170, 210, 170, 210, 160, 200, 160, 200, 150, 210, 150, 210, 140, 220, 140, 220, 150, 230, 150, 230, 160, 220, 160, 220, 170, 230, 170, 230, 200, 220, 200, 220, 210, 230, 240, 240, 240, 240, 250, 190, 250, 190, 240, 200, 240, 210, 210, 210, 200, 200, 200]
queen = [200, 200, 190, 230, 180, 210, 170, 230, 160, 210, 170, 250, 180, 270, 190, 280, 170, 300, 190, 310, 180, 310, 180, 320, 190, 320, 200, 330, 200, 410, 190, 420, 190, 430, 270, 430, 270, 420, 260, 410, 260, 330, 270, 320, 280, 320, 280, 310, 270, 310, 290, 300, 270, 280, 280, 270, 290, 250, 300, 210, 290, 230, 280, 210, 270, 230, 260, 200, 200,200]
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
            square = board.create_rectangle(nwcornerx,nwcornery,secornerx,secornery,fill = 'black',tag = identifier)
        if alternate == -1:
            square = board.create_rectangle(nwcornerx,nwcornery,secornerx,secornery,fill = 'white',tag = identifier)
        
        squaredata.append(datapoint)
        ysquarecounter = ysquarecounter+1
    ysquarecounter = 1
    xsquarecounter = xsquarecounter + 1
root.mainloop()
