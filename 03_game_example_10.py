
class Remote():
    def isLeftPressed(self):
        pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

remote1 = Remote()
p1 = Player()
if remote1.isLeftPressed():
    p1.moveLeft()

