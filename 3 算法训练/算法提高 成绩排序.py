class Score():
    def __init__(self,id,math,english,chinese):
        self.id = id
        self.math = math
        self.english = english
        self.chinese = chinese

    def __gt__(self,b):
        if self.math > b.math:
            return True
        elif self.math == b.math:
            if self.english > b.english:
                return True
            elif self.english == b.english:
                if self.chinese > b.chinese:
                    return True
                elif self.chinese == b.chinese:
                    if self.id < self.id:
                        return True
        return False
    
    def __lt__(self,b):
        if self.math < b.math:
            return True
        elif self.math == b.math:
            if self.english < b.english:
                return True
            elif self.english == b.english:
                if self.chinese < b.chinese:
                    return True
                elif self.chinese == b.chinese:
                    if self.id > self.id:
                        return True
        return False

    def show(self):
        print("{} {} {} {}".format(self.math,self.english,self.chinese,self.id))

if __name__ == "__main__":
    n = int(input())
    all = []
    for i in range(1,n+1):
        a,b,c = list(map(int,input().split()))
        all.append(Score(i,a,b,c))
    all.sort(reverse=True)
    for c in all:
        c.show()