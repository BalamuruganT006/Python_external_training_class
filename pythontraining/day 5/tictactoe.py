b=[' ']*9
w=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
p='X'
def show():print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}")
for _ in range(9):
    show()
    m=int(input(f"{p}'s move (1-9): "))-1
    if b[m]!=' ':print("Invalid");continue
    b[m]=p
    if any(b[x]==b[y]==b[z]==p for x,y,z in w):show();print(p,"wins!");break
    p='XO'[p=='X']
else:show();print("Draw!")
