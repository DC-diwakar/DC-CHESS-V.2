from tkinter import *
from PIL import Image, ImageTk
class xxx:
 kingInAction=""
 selectedPlayer="NONE"
 selectedPlayerXCR=-1
 selectedPlayerYCR=-1 
 blueKingInDanger=False
 blackKingInDanger=False
 blueKingXCR=4 
 blueKingYCR=7 
 blackKingXCR=4 
 blackKingYCR=0
 rrd=0
def redrawBoard():
 y=0
 while y<=canvasHeight:
  canvasBoard.create_line(0, y, canvasWidth, y, fill="black",width=2)
#  canvasBoard.create_rectangle(0,y,80,80,fill="white")
  y=y+80

 x=0
 while x<=canvasWidth:
  canvasBoard.create_line(x, 0, x, canvasHeight, fill="black",width=2)
#  canvasBoard.create_rectangle(x,0,80,80,fill="white")
  x=x+80



def pathForKing(xcor,ycor,colorOfOppositeTeam):
 mm.selectedPlayerXCR=xcor
 mm.selectedPlayerYCR=ycor  
 if xcor-1>-1 and ycor-1 >-1:
  if chessModel[ycor-1][xcor-1]==0:
   pathForSelectedPlayer[ycor-1][xcor-1]=True
  else:
   if chessModel[ycor-1][xcor-1].startswith(colorOfOppositeTeam,0):
    pathForSelectedPlayer[ycor-1][xcor-1]=True
 if ycor-1 >-1:
  if chessModel[ycor-1][xcor]==0:
   pathForSelectedPlayer[ycor-1][xcor]=True
  else:
   if chessModel[ycor-1][xcor].startswith(colorOfOppositeTeam,0):
    pathForSelectedPlayer[ycor-1][xcor]=True
 if xcor+1<8 and ycor-1 >-1:
  if chessModel[ycor-1][xcor+1]==0:
   pathForSelectedPlayer[ycor-1][xcor+1]=True
  else:
   if chessModel[ycor-1][xcor+1].startswith(colorOfOppositeTeam,0):
    pathForSelectedPlayer[ycor-1][xcor+1]=True    
 if xcor-1>-1:
  if chessModel[ycor][xcor-1]==0:
   pathForSelectedPlayer[ycor][xcor-1]=True
  else:
   if chessModel[ycor][xcor-1].startswith(colorOfOppositeTeam,0):
    pathForSelectedPlayer[ycor][xcor-1]=True

 if xcor+1<8:
  if chessModel[ycor][xcor+1]==0: 
   pathForSelectedPlayer[ycor][xcor+1]=True
  else:
   if chessModel[ycor][xcor+1].startswith(colorOfOppositeTeam,0):
    pathForSelectedPlayer[ycor][xcor+1]=True

 if xcor-1>-1 and ycor+1 <8:
  if chessModel[ycor+1][xcor-1]==0:
   pathForSelectedPlayer[ycor+1][xcor-1]=True
  else:
   if chessModel[ycor+1][xcor-1].startswith(colorOfOppositeTeam,0):
    pathForSelectedPlayer[ycor+1][xcor-1]=True

 if ycor+1<8:
  if chessModel[ycor+1][xcor]==0:
   pathForSelectedPlayer[ycor+1][xcor]=True
  else:
   if chessModel[ycor+1][xcor].startswith(colorOfOppositeTeam,0):
    pathForSelectedPlayer[ycor+1][xcor]=True

 if xcor+1<8 and ycor+1<8:
  if chessModel[ycor+1][xcor+1]==0:
   pathForSelectedPlayer[ycor+1][xcor+1]=True
  else:
   if chessModel[ycor+1][xcor+1].startswith(colorOfOppositeTeam,0):
    pathForSelectedPlayer[ycor+1][xcor+1]=True



def highlightForSelectedPath():
 i=0
 j=0
 for i in range(8):
  for j in range(8):
   if pathForSelectedPlayer[i][j]==True:
    highlightSquare(j,i,"orange")

def pathForPawn(xcor,ycor,colorOfOppositeTeam):
  mm.selectedPlayerXCR=xcor
  mm.selectedPlayerYCR=ycor
  a=xcor
  b=ycor
  if colorOfOppositeTeam=="black" and b>0:
   if chessModel[b-1][a]==0:
    pathForSelectedPlayer[b-1][a]=True
   if a<7 and chessModel[b-1][a+1]!=0 and chessModel[b-1][a+1].startswith("black",0):
    pathForSelectedPlayer[b-1][a+1]=True
   if a>0 and  chessModel[b-1][a-1]!=0 and chessModel[b-1][a-1].startswith("black",0):
    pathForSelectedPlayer[b-1][a-1]=True
  else:
   if colorOfOppositeTeam=="blue" and b<7:
    if chessModel[b+1][a]==0:
     pathForSelectedPlayer[b+1][a]=True
    if a<7 and chessModel[b+1][a+1]!=0 and chessModel[b+1][a+1].startswith("blue",0):
     pathForSelectedPlayer[b+1][a+1]=True
    if a>0 and chessModel[b+1][a-1]!=0 and chessModel[b+1][a-1].startswith("blue",0):
     pathForSelectedPlayer[b+1][a-1]=True
  
def pathForRook(a,b,colorOfOppositeTeam):
    mm.selectedPlayerXCR=a
    mm.selectedPlayerYCR=b
    xcr=a+1
    ycr=b
    while xcr<8:
     if chessModel[ycr][xcr]==0:
      pathForSelectedPlayer[ycr][xcr]=True
     else:
      if chessModel[ycr][xcr].startswith(colorOfOppositeTeam,0):
       pathForSelectedPlayer[ycr][xcr]=True
      break
     xcr=xcr+1
    xcr=a
    ycr=b+1
    while ycr<8:
     if chessModel[ycr][xcr]==0:
      pathForSelectedPlayer[ycr][xcr]=True
     else:
      if chessModel[ycr][xcr].startswith(colorOfOppositeTeam,0):
       pathForSelectedPlayer[ycr][xcr]=True
      break
     ycr=ycr+1
    xcr=a-1
    ycr=b
    while xcr>-1:
     if chessModel[ycr][xcr]==0:
      pathForSelectedPlayer[ycr][xcr]=True
     else:
      if chessModel[ycr][xcr].startswith(colorOfOppositeTeam,0):
       pathForSelectedPlayer[ycr][xcr]=True
      break
     xcr=xcr-1
    xcr=a
    ycr=b-1
    while ycr>-1:
     if chessModel[ycr][xcr]==0:
      pathForSelectedPlayer[ycr][xcr]=True
     else:
      if chessModel[ycr][xcr].startswith(colorOfOppositeTeam,0):
       pathForSelectedPlayer[ycr][xcr]=True
      break
     ycr=ycr-1

def clearPathDS():
 i=0
 e=0
 for i in range(8):
  for e in range(8):
   pathForSelectedPlayer[i][e]=False
 mm.selectedPlayerXCR=-1
 mm.selectedPlayerYCR=-1


def pathForBishop(a,b,colorOfOppositeTeam):
     mm.selectedPlayerXCR=a
     mm.selectedPlayerYCR=b
     xcr=a+1
     ycr=b-1
     while xcr<8 and ycr>-1:
      if chessModel[ycr][xcr]==0:
       pathForSelectedPlayer[ycr][xcr]=True
      else:
       if chessModel[ycr][xcr].startswith(colorOfOppositeTeam,0):
        pathForSelectedPlayer[ycr][xcr]=True
       break
      xcr=xcr+1
      ycr=ycr-1
     xcr=a-1
     ycr=b-1
     while xcr>-1 and ycr>-1:
      if chessModel[ycr][xcr]==0:
       pathForSelectedPlayer[ycr][xcr]=True
      else:
       if chessModel[ycr][xcr].startswith(colorOfOppositeTeam,0):
        pathForSelectedPlayer[ycr][xcr]=True
       break
      xcr=xcr-1
      ycr=ycr-1
     xcr=a-1
     ycr=b+1
     while xcr>-1 and ycr<8:
      if chessModel[ycr][xcr]==0:
       pathForSelectedPlayer[ycr][xcr]=True
      else:
       if chessModel[ycr][xcr].startswith(colorOfOppositeTeam,0):
        pathForSelectedPlayer[ycr][xcr]=True
       break
      xcr=xcr-1
      ycr=ycr+1
     xcr=a+1
     ycr=b+1
     while xcr<8 and ycr<8:
      if chessModel[ycr][xcr]==0:
       pathForSelectedPlayer[ycr][xcr]=True
      else:
       if chessModel[ycr][xcr].startswith(colorOfOppositeTeam,0):
        pathForSelectedPlayer[ycr][xcr]=True
       break
      xcr=xcr+1
      ycr=ycr+1


 
def pathForKnight(xcor,ycor,colorOfKnight):
  mm.selectedPlayerXCR=xcor
  mm.selectedPlayerYCR=ycor
  a=xcor
  b=ycor
  if a-1 >-1 and b+2<8:
   if chessModel[b+2][a-1]==0  or chessModel[b+2][a-1].startswith(colorOfKnight,0)==False:
    pathForSelectedPlayer[b+2][a-1]=True    
  if a+1 <8 and b+2<8:
   if chessModel[b+2][a+1]==0 or chessModel[b+2][a+1].startswith(colorOfKnight,0)==False:
    pathForSelectedPlayer[b+2][a+1]=True
  if a-1 >-1 and b-2>-1:
   if chessModel[b-2][a-1]==0 or chessModel[b-2][a-1].startswith(colorOfKnight,0)==False:
    pathForSelectedPlayer[b-2][a-1]=True
  if a+1 <8 and b-2>-1:
   if chessModel[b-2][a+1]==0 or chessModel[b-2][a+1].startswith(colorOfKnight,0)==False:
    pathForSelectedPlayer[b-2][a+1]=True
  if a+2 <8 and b+1<8:
   if chessModel[b+1][a+2]==0 or chessModel[b+1][a+2].startswith(colorOfKnight,0)==False:
    pathForSelectedPlayer[b+1][a+2]=True
  if a+2 <8 and b-1>-1:
   if chessModel[b-1][a+2]==0 or chessModel[b-1][a+2].startswith(colorOfKnight,0)==False:
    pathForSelectedPlayer[b-1][a+2]=True
  if a-2 >-1 and b+1<8:
   if chessModel[b+1][a-2]==0 or chessModel[b+1][a-2].startswith(colorOfKnight,0)==False:
    pathForSelectedPlayer[b+1][a-2]=True
  if a-2 >-1 and b-1>-1:
   if chessModel[b-1][a-2]==0 or  chessModel[b-1][a-2].startswith(colorOfKnight,0)==False:
    pathForSelectedPlayer[b-1][a-2]=True
  
def highlightSquare(xcor,ycor,colorName):
 canvasBoard.create_line(xcor*80, ycor*80,xcor*80,ycor*80+80, fill=colorName,width=2)
 canvasBoard.create_line(xcor*80, ycor*80,xcor*80+80,ycor*80, fill=colorName,width=2)
 canvasBoard.create_line(xcor*80, ycor*80+80,xcor*80+80,ycor*80+80, fill=colorName,width=2)
 canvasBoard.create_line(xcor*80+80, ycor*80,xcor*80+80,ycor*80+80, fill=colorName,width=2)

def clearAttackZones():
 xcor=0
 ycor=0
 for xcor in range(8):
  for ycor in range(8):
   attackZoneForBlue[ycor][xcor]=False
   attackZoneForBlack[ycor][xcor]=False



def updateAttackZones():
 clearAttackZones()
 clearPathDS() 
 xcor=0
 ycor=0
 for xcor in range(8):
  for ycor in range(8):
   sp=chessModel[ycor][xcor]
   if sp!=0:
    if sp=='bluePawn':
     pathForPawn(xcor,ycor,"black")
    else:
     if sp=='blueRook':
      pathForRook(xcor,ycor,"black")
     else:
      if sp=='blueBishop':
       pathForBishop(xcor,ycor,"black")
      else:
       if sp=='blueKnight':
        pathForKnight(xcor,ycor,"blue")
       else:
        if sp=='blueQueen':
         pathForBishop(xcor,ycor,"black")
         pathForRook(xcor,ycor,"black")
        else:
         if sp=='blueKing':
          pathForKing(xcor,ycor,"black")
 xcor=0
 ycor=0
 for xcor in range(8):
  for ycor in range(8):
   attackZoneForBlue[ycor][xcor]=pathForSelectedPlayer[ycor][xcor]  
 clearPathDS()
 xcor=0
 ycor=0
 for xcor in range(8):
  for ycor in range(8):
   sp=chessModel[ycor][xcor]
   if sp!=0:
     if sp=='blackPawn':
      pathForPawn(xcor,ycor,"blue")
     else:
      if sp=='blackRook':
       pathForRook(xcor,ycor,"blue")
      else:
       if sp=='blackBishop':
        pathForBishop(xcor,ycor,"blue")
       else:
        if sp=='blackKnight':
         pathForKnight(xcor,ycor,"black")
        else:
         if sp=='blackQueen':
          pathForBishop(xcor,ycor,"blue")
          pathForRook(xcor,ycor,"blue")
         else:
          if sp=='blackKing':
           pathForKing(xcor,ycor,"blue")
 xcor=0
 ycor=0
 for xcor in range(8):
  for ycor in range(8):
   attackZoneForBlack[ycor][xcor]=pathForSelectedPlayer[ycor][xcor]
 clearPathDS()

 
def updateKingInAction():
 print("update king in action called")
 if mm.kingInAction=="blue":
  mm.kingInAction="black"
  canvasBoard.delete("blk")
  canvasBoard.create_image(640+130,260,anchor=NW,image=bckTT,tag="bck")

 else:
  if mm.kingInAction=="black":
   mm.kingInAction="blue"
   canvasBoard.delete("bck")
   canvasBoard.create_image(640+130,260,anchor=NW,image=blkTT,tag="blk")

def movePlayer(event): 
 if mm.selectedPlayer!="NONE": 
  print("mm.selectedPlayer")
  xcor=int(event.x/80)
  ycor=int(event.y/80)
  if xcor>7 or ycor>7:
   return
  selectedPlayerXCR=mm.selectedPlayerXCR
  selectedPlayerYCR=mm.selectedPlayerYCR
  if pathForSelectedPlayer[ycor][xcor]==True:   
   print("move")
   playerAttacked=chessModel[ycor][xcor]
   chessModel[selectedPlayerYCR][selectedPlayerXCR]=0
   chessModel[ycor][xcor]=mm.selectedPlayer
   updateAttackZones()
   print("attack zone")
   print(attackZoneForBlack[ycor][xcor])
   if mm.selectedPlayer=="blueKing":
     if  attackZoneForBlack[ycor][xcor]==False:
      mm.blueKingXCR=xcor
      mm.blueKingYCR=ycor
     else:
      chessModel[selectedPlayerYCR][selectedPlayerXCR]=mm.selectedPlayer
      chessModel[ycor][xcor]=playerAttacked
      redrawBoard()
      highlightSquare(mm.blueKingXCR,mm.blueKingYCR,"red")
      updateAttackZones()
      return  
   if mm.selectedPlayer=="blackKing":
     if  attackZoneForBlue[ycor][xcor]==False:
      mm.blackKingXCR=xcor
      mm.blackKingYCR=ycor
     else:
      chessModel[selectedPlayerYCR][selectedPlayerXCR]=mm.selectedPlayer
      chessModel[ycor][xcor]=playerAttacked
      redrawBoard()
      highlightSquare(mm.blackKingXCR,mm.blackKingYCR,"red")
      updateAttackZones()
      return 
   if mm.kingInAction=="blue":
    if attackZoneForBlack[mm.blueKingYCR][mm.blueKingXCR]==True:
     print("khud se khatra")
     chessModel[selectedPlayerYCR][selectedPlayerXCR]=mm.selectedPlayer
     chessModel[ycor][xcor]=playerAttacked
     redrawBoard()
     highlightSquare(mm.blueKingXCR,mm.blueKingYCR,"red")
     updateAttackZones()
    else:
#     chessModel[selectedPlayerYCR][selectedPlayerXCR]=mm.selectedPlayer
#     chessModel[ycor][xcor]=playerAttacked
     canvasBoard.delete(imgId[ycor][xcor])
     canvasBoard.move(imgId[selectedPlayerYCR][selectedPlayerXCR],(xcor-selectedPlayerXCR)*80,(ycor-selectedPlayerYCR)*80)
     imgId[ycor][xcor]=imgId[selectedPlayerYCR][selectedPlayerXCR]
     imgId[selectedPlayerYCR][selectedPlayerXCR]=0
     chessModel[selectedPlayerYCR][selectedPlayerXCR]=0
     chessModel[ycor][xcor]=mm.selectedPlayer
     updateAttackZones()
#     canvasBoard.create_text(640+100,30+mm.rrd,text=chr(selectedPlayerXCR+97)+""+str(8-selectedPlayerYCR)+"-->"+chr(xcor+97)+""+str(8-ycor),fill="blue",font="bold")
     mm.rrd=mm.rrd+15
#     if mm.kingInAction=="blue" and attackZoneForBlue[mm.blackKingYCR][mm.blackKingXCR]==True:
#      print("black ko check")
#      highlightSquare(mm.blackKingXCR,mm.blackKingYCR,"red")

#     if mm.selectedPlayer=="blueKing":
#      print("BLUEKING")
#      mm.blueKingXCR=xcor
#      mm.blueKingYCR=ycor
#     mm.selectedPlayer="NONE"
     clearPathDS()
     redrawBoard()
     if mm.kingInAction=="blue" and attackZoneForBlue[mm.blackKingYCR][mm.blackKingXCR]==True:
      print("black ko check")
      redrawBoard()
      highlightSquare(mm.blackKingXCR,mm.blackKingYCR,"red")
#     updateAttackZones()
     updateKingInAction()
     return
     print("updated"+mm.kingInAction)
   if mm.kingInAction=="black":
    if attackZoneForBlue[mm.blackKingYCR][mm.blackKingXCR]==True:
     print("khud se khatra")
     chessModel[selectedPlayerYCR][selectedPlayerXCR]=mm.selectedPlayer
     chessModel[ycor][xcor]=playerAttacked
     redrawBoard()
     highlightSquare(mm.blackKingXCR,mm.blackKingYCR,"red")       
     updateAttackZones()
    else:     
     chessModel[selectedPlayerYCR][selectedPlayerXCR]=mm.selectedPlayer
     chessModel[ycor][xcor]=playerAttacked
     canvasBoard.move(imgId[selectedPlayerYCR][selectedPlayerXCR],(xcor-selectedPlayerXCR)*80,(ycor-selectedPlayerYCR)*80)
     canvasBoard.delete(imgId[ycor][xcor])
     imgId[ycor][xcor]=imgId[selectedPlayerYCR][selectedPlayerXCR] 
     imgId[selectedPlayerYCR][selectedPlayerXCR]=0
     chessModel[selectedPlayerYCR][selectedPlayerXCR]=0 
     chessModel[ycor][xcor]=mm.selectedPlayer
     updateAttackZones()
#     canvasBoard.create_text(640+100,30+mm.rrd,text=chr(selectedPlayerXCR+97)+""+str(8-selectedPlayerYCR)+"-->"+chr(xcor+97)+""+str(8-ycor),fill="black",font="bold")
     mm.rrd=mm.rrd+15
      
#     if mm.kingInAction=="black" and attackZoneForBlack[mm.blueKingYCR][mm.blueKingXCR]==True:
#      print("blue ko check")
#      highlightSquare(mm.blueKingXCR,mm.blueKingYCR,"red")
#     if mm.selectedPlayer=="blackKing":
#      print("BLACKKING")
#      mm.blackKingXCR=xcor
#      mm.blackKingYCR=ycor
#     mm.selectedPlayer="NONE"
     clearPathDS()
     redrawBoard()
     if mm.kingInAction=="black" and attackZoneForBlack[mm.blueKingYCR][mm.blueKingXCR]==True:
      print("blue ko check")
      redrawBoard()
      highlightSquare(mm.blueKingXCR,mm.blueKingYCR,"red")
#     updateAttackZones()
     updateKingInAction()
     return
def selectPlayer(event):
 a=int(event.x/80)
 b=int(event.y/80)
 if a>7 or b>7:
  return
 redrawBoard()
 clearPathDS()
 highlightSquare(a,b,"black")
 cm=chessModel[b][a]
 print(mm.kingInAction) 
 if mm.kingInAction=="blue" and cm!=0 and  cm.startswith("blue",0): 
#  mm.kingInAction="black"
  mm.selectedPlayer=cm

  if cm=='bluePawn':
   pathForPawn(a,b,"black")
   print("bluePawn")
  else:
   if cm=='blueRook':
    pathForRook(a,b,"black")
   else:
    if cm=='blueBishop':
     pathForBishop(a,b,"black")
     print("blueBishop")
    else:
     if cm=='blueKnight':
      pathForKnight(a,b,"blue")
      print('blueKnight')
     else:
      if cm=='blueQueen':
       pathForBishop(a,b,"black")
       pathForRook(a,b,"black")
      else:
       if cm=='blueKing':
        pathForKing(a,b,"black") 
        print("blueKing")
 else:
  if mm.kingInAction=="black" and cm!=0 and cm.startswith("black"):
#   mm.kingInAction="blue"
   print(mm.selectedPlayer+"blackie")
   mm.selectedPlayer=cm
   print(cm)
   if cm=='blackPawn':
    pathForPawn(a,b,"blue")
    print("blackPawn")
   else: 
    if cm=='blackRook': 
     pathForRook(a,b,"blue")
     print("blackRook")
    else:
     if cm=='blackBishop':
      pathForBishop(a,b,"blue")
      print("blackBishop")
     else:
      if cm=='blackKnight':
       pathForKnight(a,b,"black")
       print('blackKnight')
      else:
       if cm=='blackQueen':
        pathForBishop(a,b,"blue")  
        pathForRook(a,b,"blue")
        print("blackQueen")
       else:
        if cm=='blackKing':
         pathForKing(a,b,"blue")
         print("blackKing")
 highlightForSelectedPath()   


pathForSelectedPlayer=[False]*8
for i in range(8):
 pathForSelectedPlayer[i]=[False]*8


attackZoneForBlack=[False]*8
attackZoneForBlue=[False]*8
for i in range(8):
 attackZoneForBlack[i]=[False]*8
 attackZoneForBlue[i]=[False]*8

chessModel= [0]*8
for i in range(8):
 chessModel[i] = [0]*8



for i in range(8):
 chessModel[1][i]='blackPawn'
 chessModel[6][i]='bluePawn'

imgId=[0]*8
for i in range(8):
 imgId[i]=[0]*8

chessModel[0][0]='blackRook'
chessModel[0][1]='blackKnight'
chessModel[0][2]='blackBishop'
chessModel[0][3]='blackQueen'
chessModel[0][4]='blackKing'
chessModel[0][5]='blackBishop'
chessModel[0][6]='blackKnight'
chessModel[0][7]='blackRook'

chessModel[7][0]='blueRook'
chessModel[7][1]='blueKnight'
chessModel[7][2]='blueBishop'
chessModel[7][3]='blueQueen'
chessModel[7][4]='blueKing'
chessModel[7][5]='blueBishop'
chessModel[7][6]='blueKnight'
chessModel[7][7]='blueRook'
master=Tk()
canvasWidth = 640
canvasHeight = 640
canvasBoard = Canvas(master,width=1000,height=640+20)

canvasBoard.pack()
blackPawn= Image.open("blackPawn.png64")
bluePawn=Image.open("bluePawn.png64")
bluePawnTT=ImageTk.PhotoImage(bluePawn)
blackPawnTT = ImageTk.PhotoImage(blackPawn)
blackKnight=Image.open("knightBlack.png64")
blackKnightTT=ImageTk.PhotoImage(blackKnight)
blueKnight=Image.open("blueKnight.png64")
blueKnightTT=ImageTk.PhotoImage(blueKnight)
blackQueen=Image.open("blackQueen.png64")
blackQueenTT=ImageTk.PhotoImage(blackQueen)
blueQueen=Image.open("blueQueen.png64")
blueQueenTT=ImageTk.PhotoImage(blueQueen)
blackKing=Image.open("blackKing.png64")
blackKingTT=ImageTk.PhotoImage(blackKing)
blueKing=Image.open("blueKing.png64")
blueKingTT=ImageTk.PhotoImage(blueKing)
blackRook=Image.open("rook1.png64")
blackRookTT=ImageTk.PhotoImage(blackRook)
blueRook=Image.open("blueRook.png64")
blueRookTT=ImageTk.PhotoImage(blueRook)
blackBishop=Image.open("bishop1.png64")
blackBishopTT=ImageTk.PhotoImage(blackBishop)
blueBishop=Image.open("blueBishop.png64")
blueBishopTT=ImageTk.PhotoImage(blueBishop)
bckTT=ImageTk.PhotoImage(Image.open("bck.png64"))
blkTT=ImageTk.PhotoImage(Image.open("blk.png64"))
mm=xxx()


def init_board():
 mm.kingInAction="blue"
 y=0
 while y<=canvasHeight: 
  canvasBoard.create_line(0, y, canvasWidth, y, fill="black")
  y=y+80
 x=0
 while x<=canvasWidth:
  canvasBoard.create_line(x, 0, x, canvasHeight, fill="black")
  x=x+80
 i=0;
 j=0;
 color1="grey"
 color2="white"
 while i<8:
  j=0
  g=color1
  color1=color2
  color2=g
  while j<8:
   canvasBoard.create_rectangle(i*80,j*80,(i+1)*80,(j+1)*80,fill=color1)
   canvasBoard.create_rectangle(i*80,(j+1)*80,(i+1)*80,(j+2)*80,fill=color2)
   j=j+2
  i=i+1
 


 canvasBoard.create_line(640,0,640,640,width=5,fill="black")
 canvasBoard.create_line(0,0,0,640,width=5,fill="black")
 canvasBoard.create_line(0,640,640,640,width=5,fill="black")
 canvasBoard.create_line(640+30,0,640+30,640+20,width=5,fill="black")
 x=0
 i=0
 while x<canvasWidth:
  imgId[1][i]=canvasBoard.create_image(10+15+x, 10+80, anchor=NW, image=blackPawnTT)
  imgId[6][i]=canvasBoard.create_image(10+15+x, 640-80-70, anchor=NW, image=bluePawnTT)
  x=x+80
  i=i+1
 imgId[0][1]=canvasBoard.create_image(15+80, 10, anchor=NW, image=blackKnightTT)
 imgId[0][6]=canvasBoard.create_image(640-80-80+15, 10, anchor=NW, image=blackKnightTT)
 imgId[7][1]=canvasBoard.create_image(15+80, 10+560, anchor=NW, image=blueKnightTT)
 imgId[7][6]=canvasBoard.create_image(640-80-80+15, 10+560, anchor=NW, image=blueKnightTT)
 imgId[0][3]=canvasBoard.create_image(15+10+240, 10, anchor=NW, image=blackQueenTT)
 imgId[7][3]=canvasBoard.create_image(15+10+240, 10+560, anchor=NW, image=blueQueenTT)
 imgId[0][4]=canvasBoard.create_image(15+320, 10, anchor=NW, image=blackKingTT)
 imgId[7][4]=canvasBoard.create_image(15+320, 10+560, anchor=NW, image=blueKingTT)
 imgId[0][0]=canvasBoard.create_image(10,10 , anchor=NW, image=blackRookTT)
 imgId[0][7]=canvasBoard.create_image(640-70, 10, anchor=NW, image=blackRookTT)
 imgId[7][0]=canvasBoard.create_image(10,10+560, anchor=NW, image=blueRookTT)
 imgId[7][7]=canvasBoard.create_image(640-70, 10+560, anchor=NW, image=blueRookTT)
 imgId[0][2]=canvasBoard.create_image(10+160-5,0 , anchor=NW, image=blackBishopTT)
 imgId[0][5]=canvasBoard.create_image(640-160-70-5, 0, anchor=NW, image=blackBishopTT)
 imgId[7][2]=canvasBoard.create_image(10+160-5,0+560 , anchor=NW, image=blueBishopTT)
 imgId[7][5]=canvasBoard.create_image(640-160-70-5, 0+560, anchor=NW, image=blueBishopTT)
 canvasBoard.create_image(640+130,260,anchor=NW,image=blkTT,tag="blk")
 canvasBoard.create_text(640+170,20,text="DC_CHESS",fill="black",font='bold')
 i=0
 m=8
 while i<8:
  canvasBoard.create_text(640+10,i*80+40,text=m,font="bold")
  canvasBoard.create_text(0+i*80+40,640+10,text=chr(97+i),font="bold")
  i=i+1
  m=m-1


 canvasBoard.bind('<Double-1>',selectPlayer)
 canvasBoard.bind('<Button-1>',movePlayer)
 mainloop()

init_board()
