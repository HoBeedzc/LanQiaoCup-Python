class Score():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def __gt__(self,b):
        if self.score > b.score:
            return True
        elif self.score == b.score:
            if self.name < b.name:
                return True
        return False
    
    def __lt__(self,b):
        if self.score < b.score:
            return True
        elif self.score == b.score:
            if self.name > b.name:
                return True
        return False

    def show_name(self):
        print(self.name)

if __name__ == '__main__':
    n = int(input())
    all = []
    for i in range(n):
        a,b = input().split()
        b = int(b)
        all.append(Score(a,b))
    all.sort(reverse=True)
    for c in all:
        c.show_name()