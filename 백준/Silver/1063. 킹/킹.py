def check_valid(x,y):
    if abs(x-4.5)>=4 or abs(y-4.5)>=4:
        return False
    return True
king_pos,stone_pos,N=input().split()
king_x, king_y=ord(king_pos[0])-64, int(king_pos[1])
stone_x, stone_y=ord(stone_pos[0])-64, int(stone_pos[1])
for i in range(int(N)):
    direction=input()
    T=("T" in direction)
    B=("B" in direction)
    L=("L" in direction)
    R=("R" in direction)
    if check_valid(king_x - L +  R, king_y + T -  B):
        prev_x, prev_y=(king_x,king_y)
        king_x+=R-L
        king_y+=T-B
        if king_x==stone_x and king_y==stone_y:
            if check_valid(stone_x - L +  R, stone_y + T -  B):
                stone_x += - L +  R
                stone_y += + T -  B
            else:
                king_x,king_y=prev_x,prev_y
print(chr(king_x+64)+str(king_y))
print(chr(stone_x+64)+str(stone_y))