from ggame import App, ImageAsset, RectangleAsset, Sprite, LineStyle, Frame, Color

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)


class Board(Sprite):
    asset = ImageAsset("images/Board2.png")
    def __init__(self, position):
        super().__init__(Board.asset, position)

class exe(Sprite):
    asset = ImageAsset("images/X.png")
    def __init__(self, position):
        super().__init__(exe.asset, position)
        self.scale = .5

class owe(Sprite):
    asset = ImageAsset("images/O.png")
    def __init__(self, position):
        super().__init__(owe.asset, position)
        self.scale = .5

class horiz(Sprite):
    asset = RectangleAsset(450, 10, thinline, black)
    def __init__(self, position):
        super().__init__(horiz.asset, position)

class vert(Sprite):
    asset = RectangleAsset(10, 450, thinline, black)
    def __init__(self, position):
        super().__init__(vert.asset, position)
 

class diag1(Sprite):
    asset = RectangleAsset(10, 630, thinline, black)
    def __init__(self, position):
        super().__init__(diag1.asset, position)
        self.rotation = .785

class diag2(Sprite):
    asset = RectangleAsset(10, 630, thinline, black)
    def __init__(self, position):
        super().__init__(diag2.asset, position)
        self.rotation = -.785
        

class Game(App):
    def __init__(self):
        super().__init__()
        self.height = 700
        self.width = 1200
        print("Welcome to Tic Tac Toe")
        Board((0,0))
        Game.listenMouseEvent("click", self.spot)
        self.turns = 0
        self.if1 = 0
        self.if2 = 0
        self.if3 = 0
        self.if4 = 0
        self.if5 = 0
        self.if6 = 0
        self.if7 = 0
        self.if8 = 0
        self.if9 = 0
        self.s1 = 1
        self.s2 = 1
        self.s3 = 1
        self.s4 = 1
        self.s5 = 1
        self.s6 = 1
        self.s7 = 1
        self.s8 = 1
        self.s9 = 1
        self.winner = 0
        
    def spot(self, event):
        if event.x > 270 and event.x < 415 and event.y > 160 and event.y < 305:
            self.spot1(event)
        elif event.x > 415 and event.x < 565 and event.y > 160 and event.y < 305:
            self.spot2(event)
        elif event.x > 565 and event.x < 715 and event.y > 160 and event.y < 305:
            self.spot3(event)
        elif event.x > 270 and event.x < 415 and event.y > 305 and event.y < 455:
            self.spot4(event)
        elif event.x > 415 and event.x < 565 and event.y > 305 and event.y < 455:
            self.spot5(event)
        elif event.x > 565 and event.x < 715 and event.y > 305 and event.y < 455:
            self.spot6(event)
        elif event.x > 270 and event.x < 415 and event.y > 455 and event.y < 605:
            self.spot7(event)
        elif event.x > 415 and event.x < 565 and event.y > 455 and event.y < 605:
            self.spot8(event)
        elif event.x > 565 and event.x < 715 and event.y > 455 and event.y < 605:
            self.spot9(event)
        
    def spot1(self, event):
        if self.turns % 2 == 0 and self.if1 == 0 and self.winner == 0:
            exe((300,200))
            self.s1 = 5
            self.turns += 1
            self.if1 = 1
        elif self.turns % 2 == 1 and self.if1 == 0 and self.winner == 0:
            owe((300,200))
            self.s1 = 7
            self.turns += 1
            self.if1 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()
    def spot2(self, event):
        if self.turns % 2 == 0 and self.if2 == 0 and self.winner == 0:
            exe((450,200))
            self.s2 = 5
            self.turns +=1
            self.if2 = 1
        elif self.turns % 2 == 1 and self.if2 == 0 and self.winner == 0:
            owe((450,200))
            self.s2 = 7
            self.turns +=1
            self.if2 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()
    def spot3(self, event):
        if self.turns % 2 == 0 and self.if3 == 0 and self.winner == 0:
            exe((600,200))
            self.s3 = 5
            self.turns += 1
            self.if3 = 1
        elif self.turns % 2 == 1 and self.if3 == 0 and self.winner == 0:
            owe((600,200))
            self.s3 = 7
            self.turns += 1
            self.if3 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()
    def spot4(self, event):
        if self.turns % 2 == 0 and self.if4 == 0 and self.winner == 0:
            exe((300,350))
            self.s4 = 5
            self.turns += 1
            self.if4 = 1
        elif self.turns % 2 == 1 and self.if4 == 0 and self.winner == 0:
            owe((300,350))
            self.s4 = 7
            self.turns += 1
            self.if4 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()
    def spot5(self, event):
        if self.turns % 2 == 0 and self.if5 == 0 and self.winner == 0:
            exe((450,350))
            self.s5 = 5
            self.turns += 1
            self.if5 = 1
        elif self.turns % 2 == 1 and self.if5 == 0 and self.winner == 0:
            owe((450,350))
            self.s5 = 7
            self.turns += 1
            self.if5 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()
    def spot6(self, event):
        if self.turns % 2 == 0 and self.if6 == 0 and self.winner == 0:
            exe((600,350))
            self.s6 = 5
            self.turns += 1
            self.if6 = 1
        elif self.turns % 2 == 1 and self.if6 == 0 and self.winner == 0:
            owe((600,350))
            self.s6 = 7
            self.turns += 1
            self.if6 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()
    def spot7(self, event):
        if self.turns % 2 == 0 and self.if7 == 0 and self.winner == 0:
            exe((300,500))
            self.s7 = 5
            self.turns += 1
            self.if7 = 1
        elif self.turns % 2 == 1 and self.if7 == 0 and self.winner == 0:
            owe((300,500))
            self.s7 = 7
            self.turns += 1
            self.if7 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()
    def spot8(self, event):
        if self.turns % 2 == 0 and self.if8 == 0 and self.winner == 0:
            exe((450,500))
            self.s8 = 5
            self.turns += 1
            self.if8 = 1
        elif self.turns % 2 == 1 and self.if8 == 0 and self.winner == 0:
            owe((450,500))
            self.s8 = 7
            self.turns += 1
            self.if8 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()
    def spot9(self, event):
        if self.turns % 2 == 0 and self.if9 == 0 and self.winner == 0:
            exe((600,500))
            self.s9 = 5
            self.turns += 1
            self.if9 = 1
        elif self.turns % 2 == 1 and self.if9 == 0 and self.winner == 0:
            owe((600,500))
            self.s9 = 7
            self.turns += 1
            self.if9 = 1
        elif self.winner == 0:
            print("Please choose another space")
        self.checkwinner()

    def checkwinner(self):
        if self.s1 == 5 and self.s2 == 5 and self.s3 == 5:
            horiz((270,230))
            print("X Wins")
            self.winner = 1
            return
        elif self.s4 == 5 and self.s5 == 5 and self.s6 == 5:
            horiz((270,380))
            print("X Wins")
            self.winner = 1
            return
        elif self.s7 == 5 and self.s8 == 5 and self.s9 == 5:
            horiz((270,530))
            print("X Wins")
            self.winner = 1
            return
        elif self.s1 == 5 and self.s4 == 5 and self.s7 == 5:
            vert((340,160))
            print("X Wins")
            self.winner = 1
            return
        elif self.s2 == 5 and self.s5 == 5 and self.s8 == 5:
            vert((490,160))
            print("X Wins")
            self.winner = 1
            return
        elif self.s3 == 5 and self.s6 == 5 and self.s9 == 5:
            vert((640,160))
            print("X Wins")
            self.winner = 1
            return
        elif self.s1 == 5 and self.s5 == 5 and self.s9 == 5:
            diag1((270,160))
            print ("X Wins")
            self.winner = 1
            return
        elif self.s3 == 5 and self.s5 == 5 and self.s7 == 5:
            diag2((720,160))
            print ("X Wins")
            self.winner = 1
            return
        elif self.s1 == 7 and self.s2 == 7 and self.s3 == 7:
            horiz((270,250))
            print("O Wins")
            self.winner = 1
            return
        elif self.s4 == 7 and self.s5 == 7 and self.s6 == 7:
            horiz((270,400))
            print("O Wins")
            self.winner = 1
            return
        elif self.s7 == 7 and self.s8 == 7 and self.s9 == 7:
            horiz((270,550))
            print("O Wins")
            self.winner = 1
            return
        elif self.s1 == 7 and self.s4 == 7 and self.s7 == 7:
            vert((340,160))
            print("O Wins")
            self.winner = 1
            return
        elif self.s2 == 7 and self.s5 == 7 and self.s8 == 7:
            vert((490,160))
            print("O Wins")
            self.winner = 1
            return
        elif self.s3 == 7 and self.s6 == 7 and self.s9 == 7:
            horiz((640,400))
            print("O Wins")
            self.winner = 1
            return
        elif self.s1 == 7 and self.s5 == 7 and self.s9 == 7:
            diag1((270, 250))
            print ("O Wins")
            self.winner = 1
            return
        elif self.s3 == 7 and self.s5 == 7 and self.s7 == 7:
            diag2((720, 250))
            print ("O Wins")
            self.winner = 1
            return
        elif self.if1 == 1 and self.if2 == 1 and self.if3 == 1 and self.if4 == 1 and self.if5 == 1 and self.if6 == 1 and self.if7 == 1 and self.if8 == 1 and self.if9 == 1:
            print("Draw")
            self.winner = 1
            return
        

myapp = Game()
myapp.run()