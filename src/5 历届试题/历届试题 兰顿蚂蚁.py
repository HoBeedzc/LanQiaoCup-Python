class Ant():
    def __init__(self,Map,x,y,dir):
        self.Map = Map
        self.xpos = x
        self.ypos = y
        self.dir = dir#传入一个数字即可，不要传class
    
    def turn_right(self):
        self.dir = (self.dir + 1)%4

    def turn_left(self):
        self.dir = (self.dir + 3)%4
    
    def go_ahead(self):
        if self.dir == 0:
            self.xpos -= 1
        elif self.dir == 1:
            self.ypos += 1
        elif self.dir == 2:
            self.xpos += 1
        else:
            self.ypos -= 1

    def white_go(self):
        self.Map[self.xpos][self.ypos] = 1
        self.turn_left()
        self.go_ahead()

    def black_go(self):
        self.Map[self.xpos][self.ypos] = 0
        self.turn_right()
        self.go_ahead()

    def go(self):
        if not self.Map[self.xpos][self.ypos]:
            self.white_go()
        else:
            self.black_go()

    def show_pos(self):
        print(self.xpos,self.ypos)

    def show_map(self):
        for i in self.Map:
            for j in i:
                print(j,end = " ")
            print()
        print()

if __name__ == "__main__":
    m,n = list(map(int,input().split()))
    Map = []
    all_dir = ['U','R','D','L']
    for i in range(m):
        Map.append(list(map(int,input().split())))
    x,y,dir,k = input().split()
    x = int(x)
    y = int(y)
    dir = all_dir.index(dir)
    k = int(k)
    ant = Ant(Map,x,y,dir)
    for i in range(k):
        ant.go()
    ant.show_pos()#111
