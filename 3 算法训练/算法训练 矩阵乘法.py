class Matrix:
    def __init__(self,n,m):
        self.items = [0 for i in range(n*m)]
        self.row = n
        self.col = m

    def row_len(self):
        return self.row

    def col_len(self):
        return self.col

    def npr(self):#num_per_row
        return self.col

    def npc(self):#num_per_col
        return self.row

    def get_pos(self,x,y):
        return self.items[x*self.col + y]

    def set_pos(self,x,y,value):
        self.items[x*self.col + y] = value

    def set_row(self,x,valuelist):
        for i in range(self.col):
            self.items[x*self.col + i] = valuelist[i]

    def set_col(self,y,valuelist):
        for i in range(self.row):
            self.items[i*self.col + y] = valuelist[i]

    def inintialize(self,matlist):
        for i in range(self.row):
            for j in range(self.col):
                self.set_pos(i,j,matlist[i*self.col + j])

    def trans(self):  # 求转置矩阵
        trans = Matrix(self.col,self.row)
        for p1 in range(self.row):
            for p2 in range(self.col):
                trans.set_pos(p2, p1, self.get_pos(p1, p2))
        return trans

    def output(self):
        for t1 in range(self.row):
            for t2 in range(self.col):
                print("%d" % self.get_pos(t1, t2), end=' ')
            print()

    def plus(self,m2):#不做输入合法性检查
        res = Matrix(self.row,self.col)
        for i in range(self.row):  # 矩阵行数
            for j in range(self.col):  # 矩阵列数
                s = self.get_pos(i, j) + m2.get_pos(i, j)
                res.set_pos(i, j, s)
        return res

    def multiply(self,m2):#不做输入合法性检查
        res = Matrix(self.row,m2.col)
        for i in range(res.row_len()):
            for j in range(res.col_len()):
                s = 0
                for k in range(self.col):
                    s += self.get_pos(i,k)*m2.get_pos(k,j)
                res.set_pos(i,j,s)
        return res
if __name__ == "__main__":
    m,s,n = list(map(int,input().split()))
    m1 = Matrix(m,s)
    m2 = Matrix(s,n)
    for i in range(m):
        l = list(map(int,input().split()))
        m1.set_row(i,l)
    for i in range(s):
        l = list(map(int,input().split()))
        m2.set_row(i,l)
    m3 = m1.multiply(m2)
    m3.output()
