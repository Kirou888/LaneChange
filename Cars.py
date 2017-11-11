class Car:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.collisionbox = [[], []]

    def GetVel(self):
        return self.velocity

    def GetPos(self):
        return self.position

    def updatePos(self):
        self.collisionbox[0] = [self.position-1, self.position +1]
        self.position += self.velocity
        if self.position >=1000:
            self.collisionbox[0] = [0,0]
            self.collisionbox[1] = [self.position-1001, self.position-999]
        else:
            self.collisionbox[1] = [self.position-1, self.position+1]
    def CollisionBox(self):
        return self.collisionbox


class PlayerCar(Car):
    #def __init__(self, position, velocity):
     #   super.__init__(position, velocity)
    def updatePos(self):
        self.collisionbox[0] = [self.position - 1, self.position + 1]
        self.position += self.velocity
        self.collisionbox[1] = [self.position - 1, self.position + 1]

    def updateVeloc(self, inputvel):
        if (inputvel != 0):
            self.velocity = inputvel
