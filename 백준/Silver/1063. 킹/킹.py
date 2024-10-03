def check_valid(x,y):
    if abs(x-4.5)>=4 or abs(y-4.5)>=4:
        return False
    return True

class King():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def move(self, direction):
        if direction=="T":
            self.y+=1
        elif direction=="B":
            self.y-=1
        elif direction=="L":
            self.x-=1
        elif direction=="R":
            self.x+=1
        elif direction=="LT":
            self.x-=1
            self.y+=1
        elif direction=="RT":
            self.x+=1
            self.y+=1
        elif direction=="LB":
            self.x-=1
            self.y-=1
        elif direction=="RB":
            self.x+=1
            self.y-=1
    def check_valid(self, direction):
        if direction=="T":
            if check_valid(self.x, self.y+1):
                return True
        elif direction=="B":
            if check_valid(self.x, self.y-1):
                return True
        elif direction=="L":
            if check_valid(self.x-1, self.y):
                return True
        elif direction=="R":
            if check_valid(self.x+1, self.y):
                return True
        elif direction=="LT":
            if check_valid(self.x-1, self.y+1):
                return True
        elif direction=="RT":
            if check_valid(self.x+1, self.y+1):
                return True
        elif direction=="LB":
            if check_valid(self.x-1, self.y-1):
                return True
        elif direction=="RB":
            if check_valid(self.x+1, self.y-1):
                return True
        return False

class Stone(King):
    pass

king_pos,stone_pos,N=input().split()
king=King(ord(king_pos[0])-64, int(king_pos[1]))
stone=Stone(ord(stone_pos[0])-64, int(stone_pos[1]))
for i in range(int(N)):
    direction=input()
    if king.check_valid(direction):
        prev_x, prev_y=(king.x,king.y)
        king.move(direction)
        if king.x==stone.x and king.y==stone.y:
            if stone.check_valid(direction):
                stone.move(direction)
            else:
                king.x,king.y=prev_x,prev_y
print(chr(king.x+64)+str(king.y))
print(chr(stone.x+64)+str(stone.y))
